import random

# Character Class
class Character:
    def __init__(self, name, char_class, hp, attack, defense):
        self.name = name
        self.char_class = char_class
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.hp -= actual_damage
        print(f"{self.name} ({self.char_class}) takes {actual_damage} damage! HP: {self.hp}/{self.max_hp}")

    def is_alive(self):
        return self.hp > 0

# Player Classes
classes = {
    "Warrior": {"hp": 120, "attack": 15, "defense": 10},
    "Mage": {"hp": 80, "attack": 25, "defense": 5},
    "Rogue": {"hp": 90, "attack": 20, "defense": 7},
    "Paladin": {"hp": 110, "attack": 18, "defense": 12},
    "Archer": {"hp": 85, "attack": 22, "defense": 6},
}

# Enemy Setup
enemy_list = [
    Character(name="Goblin", char_class="Scout", hp=50, attack=10, defense=3),
    Character(name="Orc", char_class="Brute", hp=80, attack=15, defense=5),
    Character(name="Dark Mage", char_class="Caster", hp=60, attack=25, defense=2),
]

# Function to choose a class
def choose_class():
    print("\nChoose your class:")
    for idx, char_class in enumerate(classes, 1):
        stats = classes[char_class]
        print(f"{idx}. {char_class} (HP: {stats['hp']}, Attack: {stats['attack']}, Defense: {stats['defense']})")

    choice = int(input("\nEnter the number of your choice: "))
    selected_class = list(classes.keys())[choice - 1]
    stats = classes[selected_class]
    return Character(name="Hero", char_class=selected_class, hp=stats["hp"], attack=stats["attack"], defense=stats["defense"])

# Starting Menu
def start_menu():
    print("=== Welcome to the RPG Adventure ===")
    print("1. Start Game\n2. Exit")
    choice = input("\nEnter your choice: ")

    if choice == "1":
        return choose_class()
    elif choice == "2":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice. Try again.")
        return start_menu()

# Battle System
def player_turn():
    print("\n-- Your Turn --")
    print("1. Attack\n2. Defend\n")
    choice = input("Choose your action: ")

    if choice == "1":
        print(f"\nYou attack the {enemy.name} ({enemy.char_class})!")
        enemy.take_damage(player.attack)
    elif choice == "2":
        print("\nYou defend, reducing incoming damage!")

def enemy_turn():
    print("\n-- Enemy's Turn --")
    if enemy.is_alive():
        print(f"The {enemy.name} ({enemy.char_class}) attacks!")
        player.take_damage(enemy.attack)

# Main Game Loop
def battle(player):
    global enemy
    enemy = random.choice(enemy_list)
    print(f"A wild {enemy.name} ({enemy.char_class}) appears!")
    while player.is_alive() and enemy.is_alive():
        player_turn()
        if not enemy.is_alive():
            print(f"\nYou defeated the {enemy.name}!")
            break
        enemy_turn()
        if not player.is_alive():
            print("\nYou have been defeated...")

if __name__ == "__main__":
    player = start_menu()
    battle(player)
