combatant_list = []

class Combatant:
    def __init__(self, name, health):
        self.name = name
        self.health = health

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

Combat()
