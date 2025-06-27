import cv2
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from PIL import Image
import pytorch_lightning as pl
import os
import requests
import threading
import time


# =============================================================================
# DEFINE THE CNN MODEL ARCHITECTURE
# =============================================================================
# This class must be defined so we can load the saved model weights.
class EmotionCNN(pl.LightningModule):
    """Compact CNN for emotion recognition (must match the training notebook)."""

    def __init__(self, num_classes=6, learning_rate=0.001):
        super().__init__()
        self.save_hyperparameters()
        self.learning_rate = learning_rate
        self.num_classes = num_classes
        self.conv1 = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
        )
        self.conv3 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
        )
        self.global_avg_pool = nn.AdaptiveAvgPool2d(1)
        self.classifier = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, num_classes),
        )

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.global_avg_pool(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x


class EmotionDetector(threading.Thread):
    """
    Runs real-time emotion detection in a separate thread to avoid blocking the game loop.
    """

    def __init__(self, emotions_deque):
        super().__init__()
        self.daemon = True  # Thread will close when the main program exits
        self._stopper = threading.Event()
        self.emotions_deque = emotions_deque
        self.model = None
        self.emotion_names = []
        self.face_cascade = None

    def stop(self):
        self._stopper.set()

    def _load_model(self):
        """Loads the trained emotion recognition model."""
        model_path = os.path.join("ai_materials", "emotion_model.pth")
        if not os.path.exists(model_path):
            print(f"❌ Error: Model file not found at {model_path}")
            return False

        try:
            checkpoint = torch.load(
                model_path, map_location=torch.device("cpu"), weights_only=False
            )
            self.model = EmotionCNN(num_classes=checkpoint["num_classes"])
            self.model.load_state_dict(checkpoint["model_state_dict"])
            self.model.eval()
            self.emotion_names = checkpoint["emotion_names"]
            print(f"✅ Emotion model loaded successfully.")
            return True
        except Exception as e:
            print(f"❌ Error loading emotion model: {e}")
            return False

    def _load_face_detector(self):
        """Loads the Haar Cascade face detector from OpenCV."""
        HAAR_CASCADE_FILENAME = "haarcascade_frontalface_default.xml"
        if not os.path.exists(HAAR_CASCADE_FILENAME):
            print(f"📥 Downloading face detector: {HAAR_CASCADE_FILENAME}...")
            url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
            response = requests.get(url)
            if response.status_code == 200:
                with open(HAAR_CASCADE_FILENAME, "wb") as f:
                    f.write(response.content)
                print("✅ Download complete.")
            else:
                print(
                    f"❌ Failed to download face detector. Status code: {response.status_code}"
                )
                return False

        self.face_cascade = cv2.CascadeClassifier(HAAR_CASCADE_FILENAME)
        if self.face_cascade.empty():
            print("❌ Face detector could not be loaded.")
            return False

        print(f"✅ Face detector loaded successfully.")
        return True

    def run(self):
        """The main loop for the emotion detection thread."""
        if not self._load_model() or not self._load_face_detector():
            print("⚠️ Emotion detection thread stopping due to loading errors.")
            return

        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("❌ Error: Could not open webcam.")
            return

        transform = transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize(mean=[0.5], std=[0.5])]
        )

        print("🚀 Starting emotion detection thread...")
        while not self._stopper.is_set():
            ret, frame = cap.read()
            if not ret:
                time.sleep(0.1)
                continue

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray_frame, 1.1, 5)

            if len(faces) > 0:
                # For simplicity, we only process the largest face found
                faces = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)
                x, y, w, h = faces[0]

                face_roi = gray_frame[y : y + h, x : x + w]

                if face_roi.size == 0:
                    continue

                resized_face = cv2.resize(face_roi, (48, 48))
                image = Image.fromarray(resized_face)
                image_tensor = transform(image).unsqueeze(0)

                with torch.no_grad():
                    output = self.model(image_tensor)
                    pred_idx = torch.argmax(output, dim=1).item()
                    emotion = self.emotion_names[pred_idx]
                    self.emotions_deque.append(emotion)

            # A short sleep to prevent the thread from consuming 100% CPU
            time.sleep(0.1)

        cap.release()
        print("✅ Emotion detection thread stopped.")
