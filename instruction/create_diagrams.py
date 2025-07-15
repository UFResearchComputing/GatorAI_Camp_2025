"""
PyDew Valley - Interactive Architecture Visualizer
================================================
This script generates a visual representation of the game's architecture
and file dependencies for educational purposes.

Run this script to see how the game files interact with each other!
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np


def create_architecture_diagram():
    """Create a visual representation of the game architecture"""

    # Create figure and axis
    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Define colors for different categories
    colors = {
        "core": "#FF6B6B",  # Red - Core Framework
        "mechanics": "#4ECDC4",  # Teal - Game Mechanics
        "ui": "#45B7D1",  # Blue - User Interface
        "ai": "#96CEB4",  # Green - AI Features
        "utils": "#FECA57",  # Yellow - Utilities
        "audio": "#FF9FF3",  # Pink - Audio/Settings
    }

    # Define file positions and categories
    files = {
        # Core Framework (Top)
        "main.py": {"pos": (5, 9), "cat": "core", "size": (1.5, 0.6)},
        "level.py": {"pos": (3, 7.5), "cat": "core", "size": (1.2, 0.5)},
        "player.py": {"pos": (7, 7.5), "cat": "core", "size": (1.2, 0.5)},
        # Game Mechanics (Left side)
        "sprites.py": {"pos": (1, 6), "cat": "mechanics", "size": (1, 0.4)},
        "soil.py": {"pos": (1, 5), "cat": "mechanics", "size": (1, 0.4)},
        "sky.py": {"pos": (1, 4), "cat": "mechanics", "size": (1, 0.4)},
        "transition.py": {"pos": (1, 3), "cat": "mechanics", "size": (1, 0.4)},
        # User Interface (Right side)
        "overlay.py": {"pos": (9, 6), "cat": "ui", "size": (1, 0.4)},
        "character_screen.py": {"pos": (9, 5), "cat": "ui", "size": (1, 0.4)},
        "main_menu.py": {"pos": (9, 4), "cat": "ui", "size": (1, 0.4)},
        "trader_menu.py": {"pos": (9, 3), "cat": "ui", "size": (1, 0.4)},
        "settings_menu.py": {"pos": (9, 2), "cat": "ui", "size": (1, 0.4)},
        # AI Features (Middle)
        "emotion_detector.py": {"pos": (4, 5.5), "cat": "ai", "size": (1.3, 0.4)},
        "dialogue_system.py": {"pos": (6, 5.5), "cat": "ai", "size": (1.3, 0.4)},
        "ai_dialogue_manager.py": {"pos": (5, 4.5), "cat": "ai", "size": (1.5, 0.4)},
        # Utilities (Bottom)
        "settings.py": {"pos": (2, 1.5), "cat": "utils", "size": (1, 0.4)},
        "support.py": {"pos": (4, 1.5), "cat": "utils", "size": (1, 0.4)},
        "timer.py": {"pos": (6, 1.5), "cat": "utils", "size": (1, 0.4)},
        "installer.py": {"pos": (8, 1.5), "cat": "utils", "size": (1, 0.4)},
        # Audio/Settings
        "game_settings.py": {"pos": (5, 2.5), "cat": "audio", "size": (1.2, 0.4)},
    }

    # Draw file boxes
    for filename, info in files.items():
        x, y = info["pos"]
        width, height = info["size"]
        color = colors[info["cat"]]

        # Create rounded rectangle
        box = FancyBboxPatch(
            (x - width / 2, y - height / 2),
            width,
            height,
            boxstyle="round,pad=0.02",
            facecolor=color,
            edgecolor="black",
            linewidth=1,
            alpha=0.8,
        )
        ax.add_patch(box)

        # Add text
        ax.text(
            x,
            y,
            filename.replace(".py", ""),
            ha="center",
            va="center",
            fontsize=8,
            weight="bold",
            color="white",
        )

    # Define key dependencies (simplified for clarity)
    dependencies = [
        ("main.py", "level.py"),
        ("main.py", "player.py"),
        ("main.py", "main_menu.py"),
        ("main.py", "character_screen.py"),
        ("level.py", "sprites.py"),
        ("level.py", "soil.py"),
        ("level.py", "sky.py"),
        ("level.py", "overlay.py"),
        ("level.py", "trader_menu.py"),
        ("level.py", "dialogue_system.py"),
        ("player.py", "timer.py"),
        ("player.py", "settings.py"),
        ("dialogue_system.py", "ai_dialogue_manager.py"),
        ("emotion_detector.py", "game_settings.py"),
    ]

    # Draw dependency arrows
    for source, target in dependencies:
        if source in files and target in files:
            x1, y1 = files[source]["pos"]
            x2, y2 = files[target]["pos"]

            # Calculate arrow position (from edge to edge)
            dx = x2 - x1
            dy = y2 - y1
            length = np.sqrt(dx**2 + dy**2)

            if length > 0:
                # Normalize and scale
                dx_norm = dx / length
                dy_norm = dy / length

                # Start and end points (adjusted for box sizes)
                start_x = x1 + dx_norm * files[source]["size"][0] / 2
                start_y = y1 + dy_norm * files[source]["size"][1] / 2
                end_x = x2 - dx_norm * files[target]["size"][0] / 2
                end_y = y2 - dy_norm * files[target]["size"][1] / 2

                ax.annotate(
                    "",
                    xy=(end_x, end_y),
                    xytext=(start_x, start_y),
                    arrowprops=dict(arrowstyle="->", color="gray", lw=1, alpha=0.6),
                )

    # Add title
    ax.text(
        5,
        9.7,
        "PyDew Valley - Game Architecture Diagram",
        ha="center",
        va="center",
        fontsize=16,
        weight="bold",
    )

    # Create legend
    legend_elements = [
        mpatches.Patch(color=colors["core"], label="Core Framework"),
        mpatches.Patch(color=colors["mechanics"], label="Game Mechanics"),
        mpatches.Patch(color=colors["ui"], label="User Interface"),
        mpatches.Patch(color=colors["ai"], label="AI Features"),
        mpatches.Patch(color=colors["utils"], label="Utilities"),
        mpatches.Patch(color=colors["audio"], label="Audio/Settings"),
    ]

    ax.legend(handles=legend_elements, loc="upper left", bbox_to_anchor=(0, 1))

    # Add educational notes
    notes = [
        "🎯 Arrows show dependencies (who imports whom)",
        "📚 Start learning with Core Framework files",
        "🔧 Utilities are used by most other files",
        "🤖 AI features are optional advanced topics",
        "🎵 Audio/Settings manage persistent configuration",
    ]

    for i, note in enumerate(notes):
        ax.text(
            0.1, 0.4 - i * 0.06, note, transform=ax.transAxes, fontsize=9, alpha=0.8
        )

    plt.tight_layout()
    return fig


def create_complexity_chart():
    """Create a complexity/learning progression chart"""

    fig, ax = plt.subplots(1, 1, figsize=(14, 8))

    # File complexity data (complexity score, educational value, prerequisites)
    files_data = {
        "installer.py": {"complexity": 1, "concepts": 2, "line_count": 26},
        "settings.py": {"complexity": 1, "concepts": 4, "line_count": 150},
        "timer.py": {"complexity": 2, "concepts": 3, "line_count": 50},
        "support.py": {"complexity": 2, "concepts": 4, "line_count": 80},
        "game_settings.py": {"complexity": 2, "concepts": 5, "line_count": 200},
        "main_menu.py": {"complexity": 2, "concepts": 4, "line_count": 180},
        "character_screen.py": {"complexity": 2, "concepts": 3, "line_count": 100},
        "trader_menu.py": {"complexity": 3, "concepts": 5, "line_count": 200},
        "overlay.py": {"complexity": 2, "concepts": 4, "line_count": 150},
        "sprites.py": {"complexity": 3, "concepts": 6, "line_count": 300},
        "sky.py": {"complexity": 2, "concepts": 4, "line_count": 150},
        "transition.py": {"complexity": 2, "concepts": 3, "line_count": 50},
        "soil.py": {"complexity": 3, "concepts": 6, "line_count": 400},
        "main.py": {"complexity": 3, "concepts": 7, "line_count": 200},
        "player.py": {"complexity": 4, "concepts": 8, "line_count": 600},
        "level.py": {"complexity": 4, "concepts": 9, "line_count": 550},
        "dialogue_system.py": {"complexity": 3, "concepts": 6, "line_count": 300},
        "emotion_detector.py": {"complexity": 5, "concepts": 8, "line_count": 266},
        "ai_dialogue_manager.py": {"complexity": 4, "concepts": 6, "line_count": 200},
    }

    # Extract data for plotting
    names = list(files_data.keys())
    complexities = [files_data[name]["complexity"] for name in names]
    concepts = [files_data[name]["concepts"] for name in names]
    sizes = [files_data[name]["line_count"] for name in names]

    # Create scatter plot
    scatter = ax.scatter(
        complexities,
        concepts,
        s=[s / 2 for s in sizes],
        alpha=0.6,
        c=complexities,
        cmap="viridis",
    )

    # Add file names as labels
    for i, name in enumerate(names):
        ax.annotate(
            name.replace(".py", ""),
            (complexities[i], concepts[i]),
            xytext=(5, 5),
            textcoords="offset points",
            fontsize=8,
            alpha=0.8,
        )

    ax.set_xlabel("Code Complexity (1=Simple, 5=Advanced)", fontsize=12)
    ax.set_ylabel("Educational Concepts Covered", fontsize=12)
    ax.set_title(
        "PyDew Valley - File Complexity vs Educational Value\n(Bubble size = Lines of Code)",
        fontsize=14,
        weight="bold",
    )

    # Add grid
    ax.grid(True, alpha=0.3)

    # Add colorbar
    cbar = plt.colorbar(scatter)
    cbar.set_label("Complexity Level", rotation=270, labelpad=20)

    # Add learning path annotations
    beginner_files = ["installer.py", "settings.py", "timer.py", "support.py"]
    intermediate_files = ["main.py", "player.py", "sprites.py", "overlay.py"]
    advanced_files = ["level.py", "emotion_detector.py", "dialogue_system.py"]

    # Add learning path boxes
    ax.text(
        0.02,
        0.98,
        "🔰 BEGINNER PATH\n" + "\n".join([f"• {f}" for f in beginner_files]),
        transform=ax.transAxes,
        fontsize=9,
        va="top",
        bbox=dict(boxstyle="round", facecolor="lightgreen", alpha=0.7),
    )

    ax.text(
        0.02,
        0.65,
        "🔸 INTERMEDIATE PATH\n" + "\n".join([f"• {f}" for f in intermediate_files]),
        transform=ax.transAxes,
        fontsize=9,
        va="top",
        bbox=dict(boxstyle="round", facecolor="lightblue", alpha=0.7),
    )

    ax.text(
        0.02,
        0.35,
        "🔶 ADVANCED PATH\n" + "\n".join([f"• {f}" for f in advanced_files]),
        transform=ax.transAxes,
        fontsize=9,
        va="top",
        bbox=dict(boxstyle="round", facecolor="lightcoral", alpha=0.7),
    )

    plt.tight_layout()
    return fig


if __name__ == "__main__":
    print("🎮 Generating PyDew Valley Architecture Diagrams...")

    # Create architecture diagram
    print("📊 Creating architecture diagram...")
    arch_fig = create_architecture_diagram()
    arch_fig.savefig("architecture_diagram.png", dpi=300, bbox_inches="tight")
    print("✅ Architecture diagram saved as 'architecture_diagram.png'")

    # Create complexity chart
    print("📈 Creating complexity/learning chart...")
    comp_fig = create_complexity_chart()
    comp_fig.savefig("complexity_chart.png", dpi=300, bbox_inches="tight")
    print("✅ Complexity chart saved as 'complexity_chart.png'")

    print("\n🎯 Educational Usage:")
    print("• Use architecture_diagram.png to show students how files connect")
    print("• Use complexity_chart.png to plan learning progression")
    print("• Larger bubbles = more code to study")
    print("• Higher complexity = more advanced concepts")
    print("• Higher concept count = more educational value")

    plt.show()
