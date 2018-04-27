from Basic_File import Torvinn
from random import randint

class BaronAshbury:
    def __init__(self):
        self.boss_health = 100
        self.is_running = True
        self.turn_counter = 0
        self.boss_cooldown = 5
        self.player = Torvinn()
        self.soe_amount = self.player.health/2
        self.Torvinn.opponent.health = boss_health
        self.Torvinn.opponent.armor = 2
        self.battle()

    def battle(self):
        while self.is_running == True:
            print("Baron Ashbury has " + self.boss_health + " HP remaining.")
            print("You have " + self.player.health + " HP remaining.")
            self.turn_counter += 1
            self.player.turn()
            self.boss_turn()
            if self.boss_health < 1:
                print("Baron Ashbury defeated after " + self.turn_counter + " turns!")
                self.is_running = False
            elif self.player.health < 1:
                print("Torvinn was slain by Baron Ashbury.")
                self.is_running = False
            end = input("If you want to leave, enter 'quit': ")
            if end.lower == "quit":
                self.is_running = False

    def boss_turn(self):
        self.boss_cooldown -= 1
        if self.boss_cooldown == 0:
            self.asphyxiate()
        elif self.soe == True:
            self.stay_of_execution()
        else:
            self.boss_melee()

    def asphyxiate(self):
        print("Baron Ashbury says: This is just too easy.")
        print("Baron Ashbury asphyxiates his foes!")
        self.player.health = 1
        self.boss_cooldown = 5
        self.soe = True

    def stay_of_execution(self):
        print("Baron Ashbury says: I'll keep you alive to witness your screams.")
        print("Baron Ashbury delays your execution!")
        self.player.health += self.soe_amount
        self.soe = False

    def boss_melee(self):
        damage = 8 - self.player.armor + RandInt(1, 4)
        self.player.health -= damage
        print("Baron Ashbury Melee hit you " + damage + " Physical.")

BaronAshbury()
