from random import randint


class BaronAshbury:
    def __init__(self):
        self.boss_health = 200
        self.is_running = True
        self.turn_counter = 0
        self.boss_cooldown = randint(4, 6)
        self.boss_armor = 2
        self.soe = False
        self.player_health = 40
        self.player_armor = 3
        self.avengers_cooldown = 0
        self.shield_active = 0
        self.shield_cooldown = 10
        self.shields_availible = 3
        self.shield = False
        self.consecrate_cooldown = 0
        self.consecration = 0
        self.heal = False
        self.player_mana = 20
        from Torvinn_Base import self.player_turn, crusader_strike, avengers_shield, shield_of_the_righteous, consecration_attack, flash_of_light, start_of_player_turn
        self.battle()

    def battle(self):
        while self.is_running == True:
            print("Baron Ashbury has " + str(self.boss_health) + " HP remaining.")
            self.turn_counter += 1
            self.player_turn()
            if self.boss_health < 1:
                print("Baron Ashbury defeated after " + str(self.turn_counter) + " turns!")
                self.is_running = False
            else:
                self.boss_turn()
            if self.player_health < 1:
                print("Player was slain by Baron Ashbury.")
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
        self.player_health = 1
        self.boss_cooldown = randint(4,6)
        self.soe = True

    def stay_of_execution(self):
        print("Baron Ashbury says: I'll keep you alive to witness your screams.")
        print("Baron Ashbury delays your execution!")
        self.player_health += 10
        self.soe = False

    def boss_melee(self):
        damage = 8 - self.player_armor + randint(1, 4)
        self.player_health -= damage
        print("Baron Ashbury Melee hit you " + str(damage) + " Physical.")          

BaronAshbury()
