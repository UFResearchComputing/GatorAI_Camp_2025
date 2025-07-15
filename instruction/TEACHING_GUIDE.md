# 👨‍🏫 **Educator's Teaching Guide**
## PyDew Valley - Complete Instructor Resource

---

## 📚 **Quick Start for Instructors**

### **Before Class Setup (5 minutes)**
1. Clone repository: `git clone https://github.com/UFResearchComputing/GatorAI_Camp_2025`
2. Test run: `python main.py` (dependencies auto-install)
3. Review roadmap: `PROJECT_ROADMAP.md`
4. Check individual file docs: `FILE_DOCUMENTATION.md`

### **Generate Visual Aids**
```bash
# Create architecture diagrams for presentation
python create_diagrams.py
```
This generates:
- `architecture_diagram.png` - File relationship overview
- `complexity_chart.png` - Learning progression guide

---

## 🎯 **Lesson Plan Templates - 10-Day Program**

### **WEEK 1: PYTHON FUNDAMENTALS (5 Days)**

### **Day 1: Python Setup and Game Introduction (4 hours total)**

#### **Morning Session (1 hour) - Environment Setup**
**Files:** `installer.py`

**Learning Objectives:**
- Set up development environment
- Understand package management
- Learn basic Python execution

**Activities:**
1. **Environment Setup** (30 min): Install IDE, Python, GitHub setup
2. **Demo** (15 min): Run `main.py`, show auto-installation
3. **Hello World** (15 min): Basic Python script demonstration

**Assessment Questions:**
- "What is an IDE and why do we use one?"
- "How does `installer.py` automatically install packages?"
- "What happens when we run `python main.py`?"

#### **Afternoon Session (2 hours) - Basic Concepts**
**Files:** `settings.py`, basic game overview

**Learning Objectives:**
- Understand variables, constants, and data types
- Learn about dictionaries and data structures
- Explore game file organization

**Activities:**
1. **Code Reading** (45 min): Explore `settings.py` structure
2. **Game Overview** (45 min): Introduce game framework and file locations
3. **Hands-on** (30 min): Modify constants (player speed, screen size)

**Evening Session (1 hour) - Customize Splash Screen Exercise**
- Modify "Hello, World!" splash screen
- Use variables to store player name or game title
- **Deliverable**: Push project to personal GitHub repository

---

### **Day 2: Sprites and Game Logic (4 hours total)**

#### **Morning Session (1 hour) - Loading Character Sprites**
**Files:** `sprites.py`, `support.py`

**Learning Objectives:**
- Understand image loading and positioning
- Learn about file operations
- Practice with sprite creation

**Activities:**
1. **Demo** (30 min): How sprites work in the game
2. **Code Reading** (20 min): Explore `sprites.py` structure
3. **Hands-on** (10 min): Modify sprite positions

#### **Afternoon Session (2 hours) - Conditionals and Functions**
**Files:** `player.py` (movement basics), `main.py`

**Learning Objectives:**
- Understand if statements and conditionals
- Learn function creation and organization
- Practice with basic movement logic

**Activities:**
1. **Conditionals Demo** (45 min): Button presses and game conditions
2. **Function Creation** (45 min): Simple functions like `move_character()`
3. **Movement Practice** (30 min): Modify player movement

**Evening Session (1 hour) - Add First Character Exercise**
- Add a single character sprite to the game
- Use Piskel to create unique sprites
- Experiment with character position and appearance
- **Deliverable**: Push project to personal GitHub repository

---

### **Day 3: Dialogue Trees and Interactions (4 hours total)**

#### **Morning Session (1 hour) - Dialogue Tree Concepts**
**Files:** `dialogue_system.py`

**Learning Objectives:**
- Understand branching conversation options
- Learn about data structures for dialogue
- Practice with lists and dictionaries

**Activities:**
1. **Dialogue Concepts** (30 min): What are dialogue trees?
2. **Data Structures** (20 min): Lists vs dictionaries for dialogue
3. **Code Reading** (10 min): Explore `dialogue_system.py`

#### **Afternoon Session (2 hours) - Loops and Navigation**
**Files:** Continue with `dialogue_system.py`

**Learning Objectives:**
- Learn for loops for cycling through options
- Understand conversation branching logic
- Practice with user input handling

**Activities:**
1. **Loop Concepts** (45 min): For loops and iteration
2. **Branching Logic** (45 min): Using conditionals for conversation flow
3. **Input Handling** (30 min): Using `input()` for dialogue selection

**Evening Session (1 hour) - Implement Basic Conversation Exercise**
- Give newly added sprite a short conversation
- Use `input()` for dialogue selection and response branching
- **Deliverable**: Push project to personal GitHub repository

---

### **Day 4: Advanced Dialogue and Debugging (4 hours total)**

#### **Morning Session (1 hour) - Multi-step Dialogue**
**Files:** Enhanced `dialogue_system.py`

**Learning Objectives:**
- Create multi-step dialogue structures
- Understand sprite interaction with conversations
- Learn about the original "AI" (rule-based systems)

**Activities:**
1. **Complex Dialogue** (30 min): Multi-branch conversation structures
2. **Sprite Integration** (20 min): Tying actions to dialogue choices
3. **Expression Changes** (10 min): Changing sprites based on conversation

#### **Afternoon Session (2 hours) - Debugging and Organization**
**Files:** Code organization across multiple files

**Learning Objectives:**
- Learn debugging techniques with print() statements
- Understand error message interpretation
- Practice code organization in separate files

**Activities:**
1. **Debugging Techniques** (45 min): Using print() to track variables
2. **Error Reading** (45 min): Common syntax errors and solutions
3. **Code Organization** (30 min): Separating dialogue into functions/files

**Evening Session (1 hour) - Complex Dialogue Exercise + Project Planning**
- Create multi-branch dialogue for character
- Optional group brainstorming for final projects
- **Deliverable**: Push project to personal GitHub repository

---

### **Day 5: Project Finalization and Presentations (4 hours total)**

#### **Morning Session (1 hour) - Polish and Personalization**
**Files:** `overlay.py`, custom sprite work

**Learning Objectives:**
- Add custom sprites and animations
- Understand UI customization
- Practice with game polish techniques

**Activities:**
1. **Custom Graphics** (30 min): Creating and adding custom sprites
2. **UI Customization** (20 min): Modifying `overlay.py` for personal touches
3. **Animation** (10 min): Adding simple animations

#### **Afternoon Session (2 hours) - Testing and Show & Tell**
**Files:** Complete project testing

**Learning Objectives:**
- Learn systematic testing approaches
- Practice project presentation skills
- Understand code review processes

**Activities:**
1. **Testing** (45 min): Test all dialogue paths and sprite interactions
2. **Presentations** (60 min): Demonstrate modified games
3. **Code Review** (15 min): Highlight added features

**Evening Session (1 hour) - Reflection and Next Steps**
- Group discussion: Python learnings and challenges
- Review potential group projects
- Preview Week 2 AI concepts
- **Deliverable**: Push final Week 1 project to GitHub

---

### **WEEK 2: ARTIFICIAL INTELLIGENCE INTEGRATION (5 Days)**

### **Day 6: AI Concepts and Environment Setup (4 hours total)**

#### **Morning Session (1 hour) - AI Fundamentals**
**Files:** Overview materials

**Learning Objectives:**
- Understand AI, Machine Learning, and Deep Learning differences
- Learn about real-world AI applications
- Explore facial recognition concepts

**Activities:**
1. **AI Overview** (20 min): What is AI/ML/Deep Learning?
2. **Applications** (20 min): Real-world examples (image recognition, chatbots)
3. **Facial Recognition** (20 min): Face detection vs recognition vs expression

#### **Afternoon Session (2 hours) - Environment Setup**
**Files:** `emotion_detector.py`

**Learning Objectives:**
- Install AI libraries and dependencies
- Set up computer vision environment
- Understand data gathering and ethics

**Activities:**
1. **Library Installation** (45 min): Install opencv-python, face_recognition
2. **Computer Vision Setup** (45 min): Explore `emotion_detector.py`
3. **Ethics Discussion** (30 min): Privacy, consent, and responsible AI

**Evening Session (1 hour) - Test Face Detection**
- Verify AI library installations
- Test script for face detection from webcam/image
- Optional: Capture test images for training

---

### **Day 7: Facial Recognition Model Training (4 hours total)**

#### **Morning Session (1 hour) - Model Training Fundamentals**
**Files:** Training notebooks/scripts

**Learning Objectives:**
- Understand training vs validation vs test data
- Learn about facial expression datasets
- Practice with data labeling

**Activities:**
1. **Data Concepts** (30 min): Training/validation/test split
2. **Expression Dataset** (20 min): Small dataset of facial expressions
3. **Data Labeling** (10 min): Students capture labeled images

#### **Afternoon Session (2 hours) - Implementation**
**Files:** Training pipeline code

**Learning Objectives:**
- Follow model training walkthrough
- Understand how models learn from data
- Practice with model evaluation

**Activities:**
1. **Training Pipeline** (60 min): Code walkthrough for training models
2. **Model Evaluation** (45 min): Testing and accuracy measurement
3. **Model Saving** (15 min): Save trained model to file

**Evening Session (1 hour) - Train Personal Expression Model**
- Follow guided notebook/script to train model
- Test on personal images or sample photos
- Check and discuss accuracy results

---

### **Day 8: Large Language Models and APIs (4 hours total)**

#### **Morning Session (1 hour) - LLM Overview**
**Files:** API documentation and examples

**Learning Objectives:**
- Understand what Large Language Models are
- Learn about natural language capabilities
- Explore API providers and setup

**Activities:**
1. **LLM Concepts** (30 min): What are LLMs and how they're trained
2. **Capabilities** (20 min): Natural language response examples
3. **API Setup** (10 min): Overview of providers (OpenAI, etc.)

#### **Afternoon Session (2 hours) - API Integration**
**Files:** `ai_dialogue_manager.py`

**Learning Objectives:**
- Learn Python requests and JSON handling
- Understand API keys and authentication
- Practice with token usage and limits

**Activities:**
1. **API Setup** (45 min): Obtain API keys and basic setup
2. **Requests Library** (45 min): Python script for LLM endpoint requests
3. **Response Handling** (30 min): Parse JSON/text responses

**Evening Session (1 hour) - Generate Dialogue with LLM**
- Write Python script to send prompts to LLM
- Print console responses
- Generate dialogue lines or short stories
- Use original dialogue as context pre-prompts

---

### **Day 9: Game Integration - Facial Recognition + LLM (4 hours total)**

#### **Morning Session (1 hour) - Loading Models in Game**
**Files:** `emotion_detector.py`, game integration

**Learning Objectives:**
- Load saved model from Day 7 into game code
- Integrate webcam/image capture for real-time analysis
- Understand snapshot-based approach

**Activities:**
1. **Model Loading** (30 min): Load facial recognition model
2. **Webcam Integration** (20 min): Real-time capture and analysis
3. **Snapshot Approach** (10 min): Keypress to check expression

#### **Afternoon Session (2 hours) - Dynamic AI Responses**
**Files:** Integration of all AI components

**Learning Objectives:**
- Combine LLM API script with game logic
- Create dynamic prompts based on recognized expressions
- Design interaction flow and error handling

**Activities:**
1. **API Integration** (60 min): Combine expression detection with LLM calls
2. **Context-Aware Prompts** (45 min): Map expressions to conversation types
3. **Error Handling** (15 min): Handle API downtime or recognition failures

**Evening Session (1 hour) - Test AI-Enhanced Dialogue**
- Incorporate model + LLM calls into game dialogue function
- Group testing: one person as "player" (webcam), other monitors code
- Debug and refine the integration

---

### **Day 10: Final Demonstrations and Reflection (4 hours total)**

#### **Morning Session (1 hour) - Polish AI Features**
**Files:** Final project refinement

**Learning Objectives:**
- Refine dialogue flows and sprite reactions
- Add more expression-to-prompt logic
- Polish the overall AI integration

**Activities:**
1. **Dialogue Refinement** (30 min): Improve conversation flows
2. **Expression Logic** (20 min): Add more sophisticated mappings
3. **Final Testing** (10 min): Comprehensive system testing

#### **Afternoon Session (2 hours) - Final Presentations**
**Files:** Complete AI-enhanced projects

**Learning Objectives:**
- Demonstrate AI-enhanced NPCs effectively
- Present technical accomplishments clearly
- Engage in meaningful discussion about AI

**Activities:**
1. **Presentations** (90 min): Show expression recognition + LLM responses
2. **Group Discussion** (30 min): Successes, challenges, real-world AI considerations

**Evening Session (1 hour) - Reflection and Future Learning**
- Topics: scale, bias, privacy, ethics in AI
- Areas for exploration: reinforcement learning, advanced computer vision
- Share one AI learning, one challenge, one future interest area
- Optional: Feedback forms or understanding quizzes
- **Final Deliverable**: Complete AI-enhanced game project

---

## 🎮 **Hands-On Exercise Library**

### **🔰 Beginner Exercises**

#### **Exercise 1.1: Speed Modifications**
**File:** `settings.py`
**Objective:** Learn about constants and game feel
```python
# In settings.py, modify:
PLAYER_SPEED = 300  # Make player faster
TOOL_USE_DELAY = 200  # Faster tool usage
```
**Discussion:** How does speed affect gameplay?

#### **Exercise 1.2: Starting Resources**
**File:** `player.py`
**Objective:** Understand inventory systems
```python
# In player.py __init__, modify:
self.money = 1000  # More starting money
self.item_inventory = {
    "wood": 50,    # More wood
    "apple": 50,   # More apples
    # ... etc
}
```

#### **Exercise 1.3: New Controls**
**File:** `player.py`
**Objective:** Learn input handling
```python
# Add to player.py input() method:
if keys[pygame.K_r]:  # R key for running
    self.speed = 400  # Temporary speed boost
```

### **🔸 Intermediate Exercises**

#### **Exercise 2.1: New Sprite Type**
**File:** `sprites.py`
**Objective:** Practice inheritance
```python
class Rock(Generic):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups, LAYERS['main'])
        # Add custom rock behavior
```

#### **Exercise 2.2: Custom Plant**
**File:** `soil.py`
**Objective:** Understand growth mechanics
```python
# Add new plant type with different growth time
GROW_SPEED = {
    'corn': 1,
    'tomato': 0.7,
    'wheat': 1.5,  # New slow-growing crop
}
```

#### **Exercise 2.3: UI Enhancement**
**File:** `overlay.py`
**Objective:** Learn UI design
```python
# Add money display to overlay
money_surf = self.font.render(f"${self.player.money}", False, 'White')
self.display_surface.blit(money_surf, (10, 10))
```

### **🔶 Advanced Exercises**

#### **Exercise 3.1: Weather Effects**
**File:** `sky.py`, `level.py`
**Objective:** Complex system interaction
- Add snow weather type
- Make weather affect plant growth
- Add seasonal color changes

#### **Exercise 3.2: AI Personality**
**File:** `ai_dialogue_manager.py`
**Objective:** AI customization
```python
# Modify system prompt for different NPC personalities
character_prompts = {
    "trader": "You are a grumpy but helpful merchant...",
    "farmer": "You are a wise, experienced farmer...",
    "child": "You are an excited, curious child..."
}
```

#### **Exercise 3.3: Emotion-Responsive Gameplay**
**File:** `level.py`, `emotion_detector.py`
**Objective:** AI-game integration
- Make NPCs respond differently based on detected emotion
- Adjust game difficulty based on player mood
- Add emotion-triggered events

---

## 📊 **Assessment Strategies**

### **Formative Assessment (During Class)**

#### **Code Reading Comprehension**
- Show code snippet, ask "What does this do?"
- Predict output before running code
- Identify the purpose of specific functions

#### **Debug Challenges**
- Present broken code, ask students to fix
- Common issues: indentation, variable names, logic errors
- Time-boxed troubleshooting sessions

#### **Concept Mapping**
- Draw relationships between classes
- Trace data flow through systems
- Identify dependencies between files

### **Summative Assessment (End of Day/Week)**

#### **Code Modification Projects**
**Beginner Level:**
- Change game constants and observe effects
- Add new tools or seeds
- Modify UI elements

**Intermediate Level:**
- Create new sprite types
- Implement new game mechanics
- Design custom UI screens

**Advanced Level:**
- Integrate new AI features
- Build complex system interactions
- Optimize performance or add new architecture

#### **Portfolio Development**
- Students maintain a journal of modifications
- Document what they learned from each change
- Share interesting discoveries with class

---

## 🛠️ **Troubleshooting Guide**

### **Common Installation Issues**

#### **Missing Python/Pip**
```bash
# Check Python installation
python --version
python -m pip --version

# If missing, install from python.org
```

#### **Camera Access Issues**
```python
# In game_settings.py, disable camera if needed
DEFAULT_SETTINGS = {
    "enable_camera": False,  # Disable for testing
    # ... rest of settings
}
```

#### **OpenAI API Issues**
```python
# In ai_dialogue_manager.py, check:
# 1. API key is set
# 2. Network connection
# 3. Rate limits not exceeded
```

### **Common Code Issues**

#### **Indentation Errors**
- Python is sensitive to spaces/tabs
- Use VS Code's auto-formatting
- Show invisible characters to debug

#### **Import Errors**
- Check file names match exactly
- Ensure all required files are present
- Verify working directory

#### **Game Performance**
- Lower frame rate if needed: `clock.tick(30)`
- Disable AI features for slower computers
- Reduce sprite counts for testing

---

## 📈 **Learning Outcome Tracking**

### **Week 1 Objectives Checklist**

#### **Day 1 Outcomes**
- [ ] Can explain basic Python syntax
- [ ] Understands imports and modules
- [ ] Can modify simple constants
- [ ] Recognizes basic class structure

#### **Day 2 Outcomes**
- [ ] Understands game loop concept
- [ ] Can trace function calls
- [ ] Implements simple modifications
- [ ] Debugs basic syntax errors

#### **Day 3 Outcomes**
- [ ] Explains object-oriented concepts
- [ ] Creates new game objects
- [ ] Understands system interactions
- [ ] Implements complex modifications

### **Week 2 AI Objectives**

#### **Day 1 AI Outcomes**
- [ ] Understands machine learning basics
- [ ] Can explain computer vision concepts
- [ ] Recognizes AI applications in games
- [ ] Discusses AI ethics and implications

#### **Day 2 AI Integration**
- [ ] Modifies AI prompts effectively
- [ ] Understands API integration
- [ ] Creates context-aware responses
- [ ] Implements emotion-based features

---

## 💡 **Extension Activities**

### **For Advanced Students**

#### **Performance Optimization**
- Profile code to find bottlenecks
- Implement object pooling
- Optimize sprite rendering

#### **New Feature Development**
- Multiplayer networking
- Save/load game states
- Achievement systems
- Quest mechanics

#### **AI Research Projects**
- Train custom emotion models
- Implement different AI APIs
- Create AI-generated content
- Build recommendation systems

### **For Struggling Students**

#### **Simplified Exercises**
- Change only numbers/strings
- Use visual debugging tools
- Pair programming with stronger students
- Focus on one concept at a time

#### **Visual Learning Aids**
- Flowcharts for game logic
- Diagrams showing class relationships
- Step-by-step code execution traces
- Interactive debugging sessions

---

## 📝 **Lesson Reflection Questions**

### **For Students**
1. What was the most challenging concept today?
2. How does this code relate to games you've played?
3. What would you change about this game?
4. How could AI improve this game experience?
5. What other applications could this code have?

### **For Instructors**
1. Which concepts needed more explanation?
2. What exercises were most effective?
3. How can we better support struggling students?
4. What real-world connections resonated most?
5. How can we improve the next lesson?

---

## 🎯 **Success Metrics**

### **Engagement Indicators**
- Students asking "what if" questions
- Voluntary code exploration outside exercises
- Peer teaching and collaboration
- Excitement about sharing discoveries

### **Learning Indicators**
- Confident code reading and explanation
- Successful debugging of unfamiliar issues
- Creative solutions to open-ended problems
- Transfer of concepts to new contexts

### **Retention Indicators**
- References to previous concepts
- Building on earlier exercises
- Connecting classroom learning to personal interests
- Continued exploration after class

---

*This guide provides a comprehensive framework for teaching Python and AI concepts through game development. Adjust timing and complexity based on your specific student needs and constraints.*
