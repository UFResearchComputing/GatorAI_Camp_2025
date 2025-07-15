#!/usr/bin/env python3
"""
🎮 Interactive Dialogue Tree Practice
===================================
A hands-on script for students to experiment with dialogue trees
and create their own NPC conversations.

Educational Goals:
- Practice with dictionaries and lists
- Learn conditional statements and loops
- Understand how dialogue systems work
- Create interactive storytelling experiences
"""

import os
import json
from typing import Dict, List, Any


class DialogueTree:
    """A simple dialogue tree system for educational purposes"""
    
    def __init__(self, npc_name: str, dialogue_data: Dict[str, Any]):
        self.npc_name = npc_name
        self.dialogue_data = dialogue_data
        self.current_node = "start"
        self.conversation_active = True
        self.conversation_history = []
    
    def display_dialogue(self, text: str):
        """Display NPC dialogue with nice formatting"""
        print(f"\n🧙‍♂️ {self.npc_name}: {text}")
        self.conversation_history.append(f"NPC: {text}")
    
    def display_options(self, options: List[Dict[str, str]]):
        """Display player dialogue options"""
        print(f"\n💭 What do you say to {self.npc_name}?")
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option['text']}")
    
    def get_player_choice(self, num_options: int) -> int:
        """Get valid player choice with error handling"""
        while True:
            try:
                choice = input(f"\n➤ Choose (1-{num_options}): ")
                choice_num = int(choice) - 1
                if 0 <= choice_num < num_options:
                    return choice_num
                else:
                    print(f"❌ Please choose between 1 and {num_options}!")
            except ValueError:
                print("❌ Please enter a number!")
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                exit()
    
    def run_conversation(self):
        """Run the complete conversation"""
        print(f"\n🎬 Starting conversation with {self.npc_name}...")
        print("=" * 50)
        
        while self.conversation_active:
            if self.current_node not in self.dialogue_data:
                print(f"❌ Error: Cannot find dialogue node '{self.current_node}'")
                break
                
            current_data = self.dialogue_data[self.current_node]
            
            # Display NPC's dialogue
            self.display_dialogue(current_data["npc_text"])
            
            # Check if conversation should end
            if "options" not in current_data or not current_data["options"]:
                print("\n🎭 Conversation ended.")
                self.conversation_active = False
                break
            
            # Display options and get choice
            options = current_data["options"]
            self.display_options(options)
            choice = self.get_player_choice(len(options))
            
            # Display player's chosen response
            chosen_option = options[choice]
            print(f"\n👤 You: {chosen_option['text']}")
            self.conversation_history.append(f"You: {chosen_option['text']}")
            
            # Move to next dialogue node
            next_node = chosen_option.get("next", "end")
            self.current_node = next_node
            
            # Handle special endings
            if self.current_node == "end":
                print(f"\n🎭 {self.npc_name} nods and the conversation ends.")
                self.conversation_active = False
        
        print("=" * 50)
        return self.conversation_history


# Example dialogue data for students to learn from
EXAMPLE_DIALOGUES = {
    "friendly_farmer": {
        "start": {
            "npc_text": "Howdy there, newcomer! Welcome to our little farming community!",
            "options": [
                {"text": "Thank you! I'm excited to start farming.", "next": "excited"},
                {"text": "What kind of crops grow well here?", "next": "crops"},
                {"text": "Any advice for a beginner?", "next": "advice"},
                {"text": "I should get going.", "next": "end"}
            ]
        },
        "excited": {
            "npc_text": "That's the spirit! Farming is hard work, but there's nothing more rewarding than watching your plants grow.",
            "options": [
                {"text": "What should I plant first?", "next": "first_crop"},
                {"text": "How do I take care of my plants?", "next": "plant_care"},
                {"text": "Thanks for the encouragement!", "next": "end"}
            ]
        },
        "crops": {
            "npc_text": "Corn and tomatoes are perfect for beginners! They're forgiving and grow quickly in our magical soil.",
            "options": [
                {"text": "Magical soil?", "next": "magic_soil"},
                {"text": "Where can I get seeds?", "next": "seeds"},
                {"text": "Good to know, thanks!", "next": "end"}
            ]
        },
        "advice": {
            "npc_text": "Sure thing! Remember the three golden rules: water daily, plant in season, and be patient!",
            "options": [
                {"text": "What do you mean by 'plant in season'?", "next": "seasons"},
                {"text": "How often is 'daily' watering?", "next": "watering"},
                {"text": "Great advice, thank you!", "next": "end"}
            ]
        },
        "first_crop": {
            "npc_text": "Start with corn! It's hardy, grows fast, and sells well. Perfect for learning the basics.",
            "options": [
                {"text": "How long does corn take to grow?", "next": "corn_time"},
                {"text": "Any special care for corn?", "next": "corn_care"},
                {"text": "I'll try corn first!", "next": "end"}
            ]
        },
        "magic_soil": {
            "npc_text": "Legend says a nature spirit blessed our land long ago. Plants grow twice as fast here!",
            "options": [
                {"text": "Do you really believe that?", "next": "believe"},
                {"text": "That explains the lush fields!", "next": "end"}
            ]
        },
        "believe": {
            "npc_text": "After 30 years of farming here, I've seen enough magic to believe in miracles!",
        },
        "corn_time": {
            "npc_text": "In our blessed soil? About 4 days! Normally it would take weeks elsewhere.",
        }
    },
    
    "mysterious_witch": {
        "start": {
            "npc_text": "Ah, a new soul ventures into my domain... What brings you to seek the ancient knowledge?",
            "options": [
                {"text": "I'm just exploring.", "next": "exploring"},
                {"text": "Ancient knowledge? Tell me more!", "next": "knowledge"},
                {"text": "Are you a real witch?", "next": "witch_question"},
                {"text": "Sorry, wrong house!", "next": "wrong_house"}
            ]
        },
        "exploring": {
            "npc_text": "Exploration is the path to wisdom. But beware - some secrets are better left undisturbed...",
            "options": [
                {"text": "What kind of secrets?", "next": "secrets"},
                {"text": "I'll be careful.", "next": "careful"},
                {"text": "Now I'm really curious!", "next": "curious"}
            ]
        },
        "knowledge": {
            "npc_text": "The old ways of farming, when plants and people lived in harmony... Would you learn?",
            "options": [
                {"text": "Yes, teach me!", "next": "teach"},
                {"text": "Is it dangerous?", "next": "dangerous"},
                {"text": "Maybe another time.", "next": "end"}
            ]
        },
        "teach": {
            "npc_text": "Very well... The first secret: speak to your plants. They listen, and they remember kindness.",
            "options": [
                {"text": "Plants can really hear us?", "next": "plants_hear"},
                {"text": "What's the second secret?", "next": "second_secret"},
                {"text": "I'll try talking to my crops!", "next": "end"}
            ]
        },
        "plants_hear": {
            "npc_text": "All living things are connected. Your intentions flow through the earth to their roots.",
        },
        "second_secret": {
            "npc_text": "Patience, young one. Secrets must be earned through practice and respect for the earth.",
        }
    }
}


def show_menu():
    """Display the main menu"""
    print("\n" + "=" * 60)
    print("🎮 DIALOGUE TREE PRACTICE SYSTEM")
    print("=" * 60)
    print("1. 🌱 Talk to the Friendly Farmer")
    print("2. 🔮 Visit the Mysterious Witch") 
    print("3. ✨ Create Your Own NPC Dialogue")
    print("4. 📚 View Dialogue Structure Help")
    print("5. 💾 Save Your Custom Dialogue")
    print("6. 📁 Load Custom Dialogue")
    print("7. 🚪 Exit")
    print("=" * 60)


def create_custom_dialogue():
    """Help students create their own dialogue tree"""
    print("\n🎨 CREATE YOUR OWN NPC DIALOGUE")
    print("=" * 40)
    
    npc_name = input("📝 What's your NPC's name? ")
    if not npc_name.strip():
        npc_name = "Custom NPC"
    
    print(f"\n🎭 Creating dialogue for {npc_name}...")
    print("💡 Tip: Type 'end' for any 'next' field to end the conversation")
    
    dialogue_data = {}
    current_node = "start"
    
    while True:
        print(f"\n📍 Creating dialogue node: '{current_node}'")
        
        # Get NPC's dialogue text
        npc_text = input(f"💬 What does {npc_name} say? ")
        if not npc_text.strip():
            npc_text = "Hello there!"
        
        # Get player options
        options = []
        print("\n🔀 Now add player response options (enter empty line to finish):")
        
        option_num = 1
        while True:
            option_text = input(f"  Option {option_num}: ")
            if not option_text.strip():
                break
                
            next_node = input(f"    Where does this lead? (node name or 'end'): ")
            if not next_node.strip():
                next_node = "end"
                
            options.append({"text": option_text, "next": next_node})
            option_num += 1
        
        # Save this node
        dialogue_data[current_node] = {
            "npc_text": npc_text,
            "options": options
        }
        
        # Ask if they want to create more nodes
        if not options or all(opt["next"] == "end" for opt in options):
            break
            
        # Find next nodes to create
        next_nodes = [opt["next"] for opt in options if opt["next"] != "end" and opt["next"] not in dialogue_data]
        
        if not next_nodes:
            break
            
        print(f"\n🔗 You need to create these dialogue nodes: {', '.join(next_nodes)}")
        create_more = input("Continue creating nodes? (y/n): ").lower().startswith('y')
        
        if not create_more:
            break
            
        current_node = next_nodes[0]
    
    print(f"\n✅ Custom dialogue for {npc_name} created!")
    
    # Test the dialogue
    test_now = input("🧪 Would you like to test it now? (y/n): ").lower().startswith('y')
    if test_now:
        dialogue_tree = DialogueTree(npc_name, dialogue_data)
        dialogue_tree.run_conversation()
    
    return npc_name, dialogue_data


def show_dialogue_help():
    """Show students how dialogue structures work"""
    print("\n📚 DIALOGUE STRUCTURE HELP")
    print("=" * 50)
    print("""
🌳 How Dialogue Trees Work:
--------------------------
A dialogue tree is like a flowchart of conversation. Each "node" 
represents a moment in the conversation with:

• NPC's dialogue text
• Player's response options  
• Where each option leads next

📋 Basic Structure:
------------------
{
    "start": {
        "npc_text": "What the NPC says",
        "options": [
            {"text": "Player option 1", "next": "response1"},
            {"text": "Player option 2", "next": "response2"},
            {"text": "Goodbye", "next": "end"}
        ]
    },
    "response1": {
        "npc_text": "NPC's reply to option 1",
        "options": [
            {"text": "Follow-up question", "next": "followup"},
            {"text": "Thanks!", "next": "end"}
        ]
    }
}

🎯 Tips for Good Dialogues:
---------------------------
• Give NPCs distinct personalities
• Include 3-5 options per node (not too many!)
• Always include a "goodbye" option
• Make conversations feel natural
• Add branching paths for replay value

🔗 Node Connections:
-------------------
• "start" - Always the first node
• "end" - Ends the conversation
• Custom names - Connect to other nodes
• Make sure all referenced nodes exist!

✨ Creative Ideas:
-----------------
• Mood-based responses
• Information gathering
• Quest giving
• Personality quirks
• Local lore and stories
""")


def save_dialogue(name, dialogue_data):
    """Save custom dialogue to a file"""
    try:
        filename = f"custom_dialogue_{name.lower().replace(' ', '_')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({
                "name": name,
                "dialogue": dialogue_data
            }, f, indent=2, ensure_ascii=False)
        print(f"✅ Dialogue saved as {filename}")
    except Exception as e:
        print(f"❌ Error saving dialogue: {e}")


def load_dialogue():
    """Load custom dialogue from a file"""
    print("\n📁 Available dialogue files:")
    dialogue_files = [f for f in os.listdir('.') if f.startswith('custom_dialogue_') and f.endswith('.json')]
    
    if not dialogue_files:
        print("❌ No custom dialogue files found.")
        return None, None
    
    for i, filename in enumerate(dialogue_files, 1):
        print(f"  {i}. {filename}")
    
    try:
        choice = int(input(f"\nChoose file (1-{len(dialogue_files)}): ")) - 1
        if 0 <= choice < len(dialogue_files):
            filename = dialogue_files[choice]
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data["name"], data["dialogue"]
        else:
            print("❌ Invalid choice.")
            return None, None
    except (ValueError, FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        print(f"❌ Error loading dialogue: {e}")
        return None, None


def main():
    """Main program loop"""
    print("🎉 Welcome to the Dialogue Tree Practice System!")
    print("🎓 Perfect for learning how NPCs communicate in games!")
    
    custom_dialogues = {}
    
    while True:
        show_menu()
        choice = input("\n➤ Choose an option (1-7): ")
        
        try:
            if choice == "1":
                farmer = DialogueTree("Friendly Farmer Bob", EXAMPLE_DIALOGUES["friendly_farmer"])
                farmer.run_conversation()
                
            elif choice == "2":
                witch = DialogueTree("Mysterious Witch Hazel", EXAMPLE_DIALOGUES["mysterious_witch"])
                witch.run_conversation()
                
            elif choice == "3":
                name, dialogue = create_custom_dialogue()
                if name and dialogue:
                    custom_dialogues[name] = dialogue
                    
            elif choice == "4":
                show_dialogue_help()
                
            elif choice == "5":
                if not custom_dialogues:
                    print("❌ No custom dialogues to save. Create one first!")
                else:
                    print("\n💾 Custom dialogues available:")
                    names = list(custom_dialogues.keys())
                    for i, name in enumerate(names, 1):
                        print(f"  {i}. {name}")
                    
                    save_choice = int(input(f"\nWhich one to save? (1-{len(names)}): ")) - 1
                    if 0 <= save_choice < len(names):
                        name = names[save_choice]
                        save_dialogue(name, custom_dialogues[name])
                    
            elif choice == "6":
                name, dialogue = load_dialogue()
                if name and dialogue:
                    custom_dialogues[name] = dialogue
                    test_tree = DialogueTree(name, dialogue)
                    test_tree.run_conversation()
                    
            elif choice == "7":
                print("\n👋 Thanks for practicing dialogue trees!")
                print("🚀 Now go create amazing NPCs in your games!")
                break
                
            else:
                print("❌ Please choose a number between 1 and 7.")
                
        except ValueError:
            print("❌ Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
        
        input("\n⏸️  Press Enter to continue...")


if __name__ == "__main__":
    main()
