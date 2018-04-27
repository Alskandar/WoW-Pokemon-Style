from random import randint
combatant_list = []

class Combatant:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Torvinn:
    def __init__(self):
        self.health = 40
        self.armor = 3
        self.foe = input("Enter the name of your opponent: ")
        if self.foe.lower() == "baron ashbury":
            self.opponent = "Baron Ashbury"
            self.foe = "Baron Ashbury"
            self.boss = True

    def turn(self):
        self.has_acted = False
        self.avengers_cooldown -= 1
        while has_acted == False:
            action = input("Select an ability to perform: ")
            if action.lower() == "crusader strike":
                self.player.crusader_strike()
                self.has_acted = True
            elif action.lower() == "avengers shield":
                if avengers_cooldown <= 0:
                    self.player.avengers_shield()
                    self.has_acted = True
                else:
                    print("That ability is on cooldown.")
            elif action.lower() == "shield of the righteous":
                self.player.shield_of_the_righteous()
            elif action.lower() == "consecration":
                self.player.consecration()
            elif action.lower() == "flash of light":
                self.player.flash_of_light()
                
    def crusader_strike(self):
        damage = 5 - self.opponent.armor + RandInt(1, 4)
        self.BaronAshbury.boss_health -= damage
        print("Your Crusader Strike hit " + self.foe + " " + damage + " Physical.")

    def avengers_shield(self):
        damage = 6 + RandInt(1, 3)
        self.BaronAshbury.boss_health -= damage
        print("Your Avenger's Shield hit " + self.foe + " " + damage + " Holy.")
        self.avengers_cooldown = 3

class Combat:
    def __init__(self):
        self.is_running = True
        player_1 = self.choose_character()
        player_2 = self.choose_character()
        while self.is_running == True:
            defender = player_2
            attacker = player_1
            print("Player 1's turn!")
            action = self.take_input()
            if action == "attack":
                self.attack()

    def take_input(self):
        print("Enter the ability you wish to perform.")
        return input("")

    def attack(self):
        damage = 3
        self.init.player_2.health -= damage
        damage = str(damage)
        print(attacker + " deals " + damage + " to " + defender + "!")
        print(defender + "'s health is " +defender.health + ".")

    def choose_character(self):
        pretty_list = pretty_print_list()
        print("Available characters: " + pretty_list)
        charname = input("Select a character: ")
        for c in combatant_list:
            if charname == c.name:
                return c

def pretty_print_list():
    pretty_list = ""
    for c in combatant_list:
        pretty_list += c.name
        if c == combatant_list[-1]:
            bananas = 7
        else:
            pretty_list += ", "
    return pretty_list
        

Torvinn = Combatant("Torvinn", 40)
combatant_list.append(Torvinn)
Aarghh = Combatant("Aarghh", 25)
combatant_list.append(Aarghh)

#Combat()
