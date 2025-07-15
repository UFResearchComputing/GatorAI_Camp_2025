# 💬 Creating Interactive Dialogue Trees for NPCs

## 📚 What You'll Learn
- What dialogue trees are and how they work
- How to store conversations in Python data structures
- Using loops and conditionals to navigate conversations
- Creating branching dialogue for your NPCs
- Building your own interactive conversation system

---

## 🌳 Introduction to Dialogue Trees

### What is a Dialogue Tree?
A **dialogue tree** is a branching set of conversation options that allows players to have interactive conversations with game characters. Think of it like a "Choose Your Own Adventure" book, but for conversations!

```
NPC: "Hello, traveler! Welcome to our village."
├─ Option 1: "Where am I?"
│  └─ NPC: "You're in Gator Valley, the friendliest farming community!"
├─ Option 2: "Who are you?" 
│  └─ NPC: "I'm the village blacksmith. I can upgrade your tools!"
└─ Option 3: "Goodbye"
   └─ NPC: "Safe travels, friend!"
```

### Why Use Dialogue Trees?
- **Interactive Storytelling**: Players feel involved in conversations
- **Character Development**: NPCs feel more alive and interesting
- **Game Mechanics**: Can unlock quests, shops, or information
- **Educational Value**: Great for learning programming concepts!

---

## 📊 Storing Dialogue in Data Structures

### Using Dictionaries (Basic Level)

Let's start with a simple dictionary to store our NPC's dialogue:

```python
# Simple dialogue dictionary
dialogue = {
    "greeting": "Hello, traveler! Welcome to our village.",
    "option1": "Where am I?",
    "option2": "Who are you?",
    "option3": "Goodbye",
    "response1": "You're in Gator Valley, the friendliest farming community!",
    "response2": "I'm the village blacksmith. I can upgrade your tools!",
    "response3": "Safe travels, friend!"
}

# How to access dialogue
print(dialogue["greeting"])  # Prints: Hello, traveler! Welcome to our village.
print(dialogue["option1"])   # Prints: Where am I?
```

### Using Lists for Options

We can use lists to store multiple options:

```python
# Storing dialogue with lists
npc_dialogue = {
    "greeting": "Hello, traveler! What brings you to my shop?",
    "options": [
        "What do you sell?",
        "Can you teach me about farming?", 
        "I'm just looking around."
    ],
    "responses": [
        "I sell the finest seeds and tools in the valley!",
        "Certainly! The key to good farming is patience and daily care.",
        "Feel free to browse! Let me know if you need anything."
    ]
}

# Display all options
for i, option in enumerate(npc_dialogue["options"]):
    print(f"{i + 1}. {option}")
```

---

## 🔄 Using Loops to Navigate Dialogue

### Simple Loop Example

Here's how to use a loop to show dialogue options:

```python
def simple_conversation():
    """A basic conversation using loops"""
    
    # Our NPC's dialogue data
    dialogue = {
        "greeting": "Greetings! I'm the village merchant.",
        "options": [
            "What do you have for sale?",
            "Tell me about this village.",
            "I need to go."
        ],
        "responses": [
            "I have seeds, tools, and rare artifacts! What interests you?",
            "Gator Valley is known for its magical soil and friendly people!",
            "Safe travels! Come back anytime!"
        ]
    }
    
    # Start the conversation
    print(f"🧙‍♂️ NPC: {dialogue['greeting']}\n")
    
    # Show options using a loop
    while True:
        print("What would you like to say?")
        for i, option in enumerate(dialogue["options"]):
            print(f"  {i + 1}. {option}")
        
        # Get player choice
        try:
            choice = int(input("\nEnter your choice (1-3): ")) - 1
            
            # Check if choice is valid
            if 0 <= choice < len(dialogue["options"]):
                print(f"\n👤 You: {dialogue['options'][choice]}")
                print(f"🧙‍♂️ NPC: {dialogue['responses'][choice]}\n")
                
                # Exit if player chooses to leave
                if choice == 2:  # "I need to go" option
                    break
            else:
                print("Please choose a valid option!\n")
                
        except ValueError:
            print("Please enter a number!\n")

# Try it out!
# simple_conversation()
```

### Adding Branches with Conditionals

Now let's make the conversation branch based on player choices:

```python
def branching_conversation():
    """A conversation that branches based on player choices"""
    
    print("🧙‍♂️ Village Elder: Welcome, young farmer! I sense great potential in you.")
    
    # First conversation branch
    while True:
        print("\nWhat would you like to know?")
        print("1. How do I become a successful farmer?")
        print("2. What's the history of this village?")
        print("3. Are there any secrets here?")
        print("4. I should get back to work.")
        
        choice = input("\nYour choice: ")
        
        if choice == "1":
            print("\n👤 You: How do I become a successful farmer?")
            print("🧙‍♂️ Elder: Ah! The three pillars of farming:")
            print("   💧 Water your crops daily")
            print("   🌱 Plant seeds in the right season") 
            print("   ❤️ Care for your land with love")
            
            # Sub-conversation branch
            print("\nWould you like specific advice?")
            print("1. Tell me about crops")
            print("2. What about tools?")
            print("3. I understand, thank you")
            
            sub_choice = input("Your choice: ")
            if sub_choice == "1":
                print("\n🧙‍♂️ Elder: Start with corn and tomatoes - they're forgiving!")
            elif sub_choice == "2":
                print("\n🧙‍♂️ Elder: Visit the blacksmith to upgrade your tools!")
            
        elif choice == "2":
            print("\n👤 You: What's the history of this village?")
            print("🧙‍♂️ Elder: Long ago, a magical spring blessed this land...")
            print("   The soil here grows crops faster than anywhere else!")
            
        elif choice == "3":
            print("\n👤 You: Are there any secrets here?")
            print("🧙‍♂️ Elder: *whispers* Behind the old oak tree...")
            print("   There's a hidden chest with ancient seeds!")
            
        elif choice == "4":
            print("\n👤 You: I should get back to work.")
            print("🧙‍♂️ Elder: Go well, young farmer! May your crops flourish!")
            break
            
        else:
            print("\nThe elder looks confused. Please choose 1, 2, 3, or 4.")

# Try the branching conversation!
# branching_conversation()
```

---

## 🏗️ Building a Dialogue System Class

Let's create a reusable dialogue system that can handle complex conversations:

```python
class DialogueTree:
    """A reusable dialogue tree system for NPCs"""
    
    def __init__(self, npc_name, dialogue_data):
        self.npc_name = npc_name
        self.dialogue_data = dialogue_data
        self.current_node = "start"
        self.conversation_active = True
    
    def display_dialogue(self, text):
        """Display NPC dialogue with formatting"""
        print(f"\n🧙‍♂️ {self.npc_name}: {text}")
    
    def display_options(self, options):
        """Display player dialogue options"""
        print("\nWhat do you say?")
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option['text']}")
    
    def get_player_choice(self, num_options):
        """Get valid player choice"""
        while True:
            try:
                choice = int(input(f"\nChoose (1-{num_options}): ")) - 1
                if 0 <= choice < num_options:
                    return choice
                else:
                    print(f"Please choose between 1 and {num_options}!")
            except ValueError:
                print("Please enter a number!")
    
    def run_conversation(self):
        """Run the full conversation"""
        while self.conversation_active:
            current_data = self.dialogue_data[self.current_node]
            
            # Display NPC's dialogue
            self.display_dialogue(current_data["npc_text"])
            
            # Check if conversation should end
            if "options" not in current_data:
                self.conversation_active = False
                break
            
            # Display options and get choice
            options = current_data["options"]
            self.display_options(options)
            choice = self.get_player_choice(len(options))
            
            # Display player's chosen response
            chosen_option = options[choice]
            print(f"\n👤 You: {chosen_option['text']}")
            
            # Move to next dialogue node
            self.current_node = chosen_option["next"]
            
            # Handle special endings
            if self.current_node == "end":
                self.conversation_active = False

# Example dialogue data for the dialogue tree
blacksmith_dialogue = {
    "start": {
        "npc_text": "Welcome to my forge! The finest tools in the valley are made here.",
        "options": [
            {"text": "Can you upgrade my tools?", "next": "upgrade"},
            {"text": "What's the secret to good smithing?", "next": "secret"},
            {"text": "Just browsing, thanks.", "next": "browse"}
        ]
    },
    "upgrade": {
        "npc_text": "Of course! Bring me your tools and some metal, and I'll make them better than new!",
        "options": [
            {"text": "How much does it cost?", "next": "cost"},
            {"text": "What materials do you need?", "next": "materials"},
            {"text": "I'll come back later.", "next": "end"}
        ]
    },
    "secret": {
        "npc_text": "The secret? Patience, heat, and a touch of magic! Each strike must be purposeful.",
        "options": [
            {"text": "Magic? Really?", "next": "magic"},
            {"text": "Can you teach me?", "next": "teach"},
            {"text": "Interesting, thank you!", "next": "end"}
        ]
    },
    "browse": {
        "npc_text": "Feel free to look around! Everything here is handcrafted with pride.",
        # No options - conversation ends
    },
    "cost": {
        "npc_text": "Just 100 gold per tool, plus materials. A fair price for quality work!",
        "options": [
            {"text": "That's reasonable!", "next": "end"},
            {"text": "Too expensive for me.", "next": "expensive"}
        ]
    },
    "materials": {
        "npc_text": "I need iron ore for most tools, sometimes rare gems for special upgrades.",
        "options": [
            {"text": "Where can I find iron ore?", "next": "iron_location"},
            {"text": "What about those rare gems?", "next": "gems"},
            {"text": "Got it, thanks!", "next": "end"}
        ]
    },
    "magic": {
        "npc_text": "Well... maybe not real magic, but there's definitely an art to it!",
        "options": [
            {"text": "I knew it was just skill!", "next": "end"},
            {"text": "Or maybe there IS magic here...", "next": "end"}
        ]
    },
    "teach": {
        "npc_text": "Ha! It took me 20 years to master this craft. But I can share some basic tips!",
        # Conversation ends with teaching
    },
    "expensive": {
        "npc_text": "I understand. When you've saved up, come back! Quality lasts forever.",
        # Conversation ends
    },
    "iron_location": {
        "npc_text": "Check the caves east of here. Bring a good pickaxe - the ore is deep!",
        # Conversation ends
    },
    "gems": {
        "npc_text": "Rare gems... I've heard rumors of a hidden mine, but it's just legend.",
        "options": [
            {"text": "Tell me about this legend!", "next": "legend"},
            {"text": "Maybe someday I'll find it.", "next": "end"}
        ]
    },
    "legend": {
        "npc_text": "They say deep in the forest, where the old oak grows, treasure awaits the worthy.",
        # Conversation ends with mystery
    }
}

# Example of using the dialogue system
def test_dialogue_system():
    """Test our dialogue tree with the blacksmith"""
    blacksmith = DialogueTree("Master Smith Magnus", blacksmith_dialogue)
    blacksmith.run_conversation()

# Uncomment to try it:
# test_dialogue_system()
```

---

## 🎯 Exercise: Create Your Own NPC Conversation

Now it's your turn! Create a dialogue tree for the NPC you added in the previous tutorial.

### Step 1: Plan Your Conversation

Before coding, plan out your dialogue tree on paper:

```
Your NPC: [Opening greeting]
├─ Option 1: [First question]
│  └─ Response 1: [Answer + maybe more options]
├─ Option 2: [Second question]  
│  └─ Response 2: [Answer + maybe more options]
└─ Option 3: [Goodbye]
   └─ Response 3: [Farewell]
```

### Step 2: Create Your Dialogue Data

Fill in this template with your NPC's personality:

```python
# Replace with your NPC's dialogue
my_npc_dialogue = {
    "start": {
        "npc_text": "YOUR_OPENING_GREETING_HERE",
        "options": [
            {"text": "YOUR_FIRST_OPTION", "next": "response1"},
            {"text": "YOUR_SECOND_OPTION", "next": "response2"},
            {"text": "YOUR_GOODBYE_OPTION", "next": "end"}
        ]
    },
    "response1": {
        "npc_text": "YOUR_FIRST_RESPONSE",
        "options": [
            {"text": "FOLLOW_UP_QUESTION", "next": "followup1"},
            {"text": "THANKS_FOR_INFO", "next": "end"}
        ]
    },
    "response2": {
        "npc_text": "YOUR_SECOND_RESPONSE",
        # Add more options or end conversation
    },
    "followup1": {
        "npc_text": "YOUR_FOLLOWUP_RESPONSE",
        # This could lead to more branches!
    }
}
```

### Step 3: Test Your Conversation

```python
# Test your dialogue
def test_my_npc():
    my_npc = DialogueTree("Your NPC Name", my_npc_dialogue)
    my_npc.run_conversation()

# Run the test
test_my_npc()
```

---

## 🌟 Creative Ideas for NPC Conversations

### Different NPC Personalities

1. **The Wise Elder**
   - Shares farming wisdom
   - Tells village history
   - Gives mysterious hints

2. **The Friendly Shopkeeper**
   - Discusses merchandise  
   - Shares local gossip
   - Offers special deals

3. **The Curious Child**
   - Asks lots of questions
   - Shares innocent observations
   - Wants to help with farming

4. **The Grumpy Hermit**
   - Initially unfriendly
   - Warms up over time
   - Has valuable knowledge

### Advanced Conversation Features

1. **Mood System**: NPC responses change based on weather or time
2. **Memory**: NPCs remember previous conversations
3. **Relationship Levels**: Unlock new dialogue as friendship grows
4. **Conditional Dialogue**: Different options based on player inventory or achievements

### Sample: The Village Teacher

```python
teacher_dialogue = {
    "start": {
        "npc_text": "Hello there! I'm the village teacher. Are you here to learn about farming?",
        "options": [
            {"text": "Yes, I'm new to farming!", "next": "beginner"},
            {"text": "I'm already experienced.", "next": "advanced"},
            {"text": "What do you teach exactly?", "next": "subjects"}
        ]
    },
    "beginner": {
        "npc_text": "Wonderful! The first lesson is: plants need water, sunlight, and love!",
        "options": [
            {"text": "How often should I water?", "next": "watering"},
            {"text": "What should I plant first?", "next": "first_crops"},
            {"text": "Thanks for the basics!", "next": "end"}
        ]
    },
    "advanced": {
        "npc_text": "Excellent! Perhaps you'd like to learn about crop rotation or soil quality?",
        "options": [
            {"text": "Tell me about crop rotation", "next": "rotation"},
            {"text": "How do I improve soil quality?", "next": "soil"},
            {"text": "I'm always learning!", "next": "end"}
        ]
    },
    "subjects": {
        "npc_text": "I teach farming basics, advanced techniques, and the science behind plant growth!",
        "options": [
            {"text": "Science behind plants?", "next": "science"},
            {"text": "That sounds comprehensive!", "next": "end"}
        ]
    },
    # Add more dialogue nodes...
}
```

---

## 🔗 Integrating with Your NPC System

### Connecting to Game NPCs

To connect your dialogue trees to the NPCs you created in the previous tutorial, you can modify the NPC interaction method:

```python
# In your NPC character class
class YourNPCName(Generic):
    def __init__(self, pos, groups):
        super().__init__(pos, placeholder, groups, LAYERS['main'])
        
        # Add dialogue tree
        self.dialogue_tree = DialogueTree("NPC Name", your_dialogue_data)
    
    def start_conversation(self):
        """Start a conversation with this NPC"""
        self.dialogue_tree.run_conversation()

# In level.py interaction handling
def toggle_your_npc(self):
    """Start dialogue with your NPC"""
    self.your_npc.start_conversation()
```

### Using with the AI Dialogue System

You can also create a hybrid approach that uses the AI dialogue system for some responses and your custom tree for structured interactions:

```python
def hybrid_conversation(self):
    """Combine AI dialogue with structured trees"""
    # Start with AI dialogue
    self.dialogue_system.start_dialogue("your_npc_id", 
                                       player_context={...})
    
    # Then transition to structured dialogue tree
    self.your_npc.start_conversation()
```

---

## 🎓 What You've Learned

Congratulations! You now know how to:

✅ **Understand dialogue trees** and how they create interactive conversations
✅ **Store dialogue data** using Python dictionaries and lists  
✅ **Use loops and conditionals** to navigate conversations
✅ **Create branching dialogue** that responds to player choices
✅ **Build a reusable dialogue system** for any NPC
✅ **Plan and implement** your own NPC conversations

### Next Steps

1. **Create multiple NPCs** with different conversation styles
2. **Add personality** through dialogue choices and responses
3. **Implement memory** so NPCs remember past conversations
4. **Create quest systems** using dialogue trees
5. **Add conditional dialogue** based on game state

Your NPCs will feel more alive and engaging with these interactive conversation systems!

---

## 📝 Assignment Ideas for Students

### Beginner Level
1. Create a simple 3-option dialogue for a pet NPC
2. Make a shopkeeper who explains their goods
3. Design a helpful villager who gives farming tips

### Intermediate Level  
1. Create a 5+ branch conversation with multiple paths
2. Add a quest giver who remembers if quests are completed
3. Design an NPC whose mood changes based on weather

### Advanced Level
1. Create interconnected NPCs who reference each other
2. Build a relationship system with evolving dialogue
3. Design a mystery storyline revealed through multiple conversations

Happy coding! 🚀
