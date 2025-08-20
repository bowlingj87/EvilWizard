import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        self.gold = 1000 # Starting gold for each character

    def attack(self, opponent):
        damage = random.randint(1, self.attack_power)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def heal(self):
        self.health += 20
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for 20 health!")  
    
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

#****************************************Subclasses***********************************
# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Deadly Strke")
        print("2. Vampiric Strike")
        action = input("\nWhich ability do you want to use?")

        if action == "1":
            damage = self.attack_power * 2.5
            opponent.health -= damage
            print(f"\n{self.name} strikes {opponent.name} and does {damage} damage!")
        elif action == "2": 
             damage= self.attack_power
             opponent.health -= damage # Do damage to the opponent equal to damage. 
             self.health += damage * 0.5 #Heal self equal for an ammount equal to damage. 
        # check if our current health exceeds our max health. 
        if self.health > self.max_health:
            self.health = self.max_health #If it does, forcibly set it to max health.
            print(f"\n{self.name} attacks {opponent.name} and does {damage} damage and heals for the same amount!")
            print(f"{self.name} now has {self.health} health.")
    
# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power

    def special_ability(self, opponent):
        print("\nMage Abilities:")
        print("1. Fireball")
        print("2. Mana Shield")
        action = input("Choose ability: ")

        if action == "1":
            damage = self.attack_power * 2
            opponent.health -= damage
            print(f"{self.name} casts Fireball at {opponent.name} for {damage} damage!")
        elif action == "2":
            self.health += 30
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"{self.name} uses Mana Shield and restores 30 health!")
# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)  # Balanced health and attack power

    def special_ability (self,opponent):
        print("\nAbilities:")
        print("1. Backstab")
        print("2. Steal")
        action = input("\nWhich ability do you want to use?") 

        if action == "1":
           damage = self.attack_power * 2
           opponent.health -= damage
           print(f"\n{self.name} sneaks behind {opponent.name} and stabs hi in the back for {damage} damage!")   
        elif action == "2":
             amount_to_steal = 100
             opponent.gold -= amount_to_steal
             self.gold += amount_to_steal
             print(f"\n{self.name} sneaks up on {opponent.name} and steals {amount_to_steal} gold!")

class Sorcerer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=40)

    def special_ability(self, opponent):
        print("\nSorcerer Abilities:")
        print("1. Spellcast")
        print("2. Shield")
        action = input("Choose ability: ")

        if action == "1":
            damage = self.attack_power * 2.5
            opponent.health -= damage
            print(f"{self.name} casts a powerful spell on {opponent.name} for {damage} damage!")
        elif action == "2":
            block = 20
            self.health += block
            if self.health > self.max_health:
                self.health = self.max_health   
            print(f"{self.name} uses Shield and restores {block} health!")

            # Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue")  
    print("4. Sorcerer")  
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Rogue(name)
    elif class_choice == '4':
       return Sorcerer(name)   # Replace with actual class name
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal() 
            continue
        elif choice == '4':
            player.display_stats()
            continue
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            print(f"\n--- {wizard.name}'s Turn --- ")
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()