from random import randint


class TargetDummy:
    def __init__(self):
        self.boss_health = 10000000
        self.is_running = True
        self.turn_counter = 0
        self.boss_armor = 0
        self.player_health = 40
        self.player_armor = 3
        self.avengers_cooldown = 0
        self.shield_active = 0
        self.shield_cooldown = 10
        self.shields_availible = 3
        self.shield = False
        self.consecrate_cooldown = 0
        self.consecration = 0
        self.channel = False
        self.player_mana = 20
        self.battle()

    def battle(self):
        while self.is_running is True:
            self.turn_counter += 1
            self.player_turn()

    def player_turn(self):
        has_acted = False
        self.start_of_player_turn()
        while has_acted is False:
            action = input("Select an ability to perform: ")
            if action.lower() == "crusader strike":
                self.crusader_strike()
                has_acted = True
            elif action.lower() == "avengers shield":
                if self.avengers_cooldown == 0:
                        self.avengers_shield()
                        has_acted = True
                else:
                    print("That ability is on cooldown.")
            elif action.lower() == "shield of the righteous":
                if self.shields_availible > 0:
                    self.shield_of_the_righteous()
                    has_acted = True
                else:
                    print("That ability is on cooldown.")
            elif action.lower() == "consecration":
                if self.consecrate_cooldown == 0:
                    self.consecration += 5
                    self.consecrate_cooldown = 4
                    has_acted = True
                else:
                    print("That ability is on cooldown.")
            elif action.lower() == "flash of light":
                if self.player_mana > 4:
                    self.flash_of_light()
                    has_acted = True
                else:
                    print("Not enough mana.")
            elif action.lower() == "quit":
                self.is_running = False
                has_acted = True
            else:
                print("Not a valid command.")
        if self.shield_active > 0:
            self.player_armor = 5
            if self.consecration > 0:
                self.player_armor += 1
            self.shield = True


    def crusader_strike(self):
        damage = 5 - self.boss_armor + randint(1, 4)
        self.boss_health -= damage
        print("Your Crusader Strike hit Boss " + str(damage) + " Physical.")


    def avengers_shield(self):
        damage = 7 + randint(1, 4)
        self.boss_health -= damage
        print("Your Avenger's Shield hit Boss " + str(damage) + " Holy.")
        self.avengers_cooldown = 5


    def shield_of_the_righteous(self):
        damage = 5 + randint(1, 4)
        self.boss_health -= damage
        print("Your Shield of the Righteous hit Boss " + str(damage) + " Holy.")
        self.shield_active += 2
        self.shields_availible -= 1


    def consecration_attack(self):
        damage = randint(1, 4)
        self.boss_health -= damage
        print("Your Consecration hit Boss " + str(damage) + " Holy.")
        self.consecration -= 1


    def flash_of_light(self):
        self.channel = True
        self.player_mana -= 5


    def start_of_player_turn(self):
        if self.shield is True:
                    self.player_armor = 3
                    self.shield = False
        if self.channel is True:
            heal_amount = randint(14, 18)
            self.player_health += heal_amount
            print("Your Flash of Light healed you " + str(heal_amount) + " Holy.")
            self.channel = False
            if self.player_health > 40:
                self.player_health = 40
            print("You have " + str(self.player_health) + " HP remaining.")
        if self.consecration > 0:
            self.consecration_attack()
        if self.avengers_cooldown > 0:
            self.avengers_cooldown -= 1
        if self.consecrate_cooldown > 0:
            self.consecrate_cooldown -= 1
        if self.player_mana < 20:
            self.player_mana += 1
            if self.player_mana > 20:
                self.player_mana = 20
        if self.shield_cooldown > 0:
            self.shield_cooldown -= 1
        if self.shield_active > 0:
            self.shield_active -= 1
        if self.shield_cooldown == 0 and self.shields_availible < 3:
            self.shields_availible += 1
            self.shield_cooldown = 10
        print("You have " + str(self.player_mana) + " mana remaining.")
        print("You have " + str(self.shields_availible) + " charges of Shield of the Righteous availible.")


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
        self.channel = False
        self.player_mana = 20
        self.battle()

    def battle(self):
        while self.is_running is True:
            print("Baron Ashbury has " + str(self.boss_health) + " HP remaining.")
            if self.channel is True:
                heal_amount = randint(14, 18)
                self.player_health += heal_amount
                print("Your Flash of Light healed you " + str(heal_amount) + " Holy.")
                self.channel = False
                if self.player_health > 40:
                    self.player_health = 40
            self.turn_counter += 1
            self.player_turn()
            if self.shield_active > 0:
                self.player_armor = 5
                if self.consecration > 0:
                    self.player_armor += 1
                self.shield = True
            if self.boss_health < 1:
                print("Baron Ashbury defeated after " + str(self.turn_counter) + " turns!")
                self.is_running = False
            else:
                self.boss_turn()
            if self.shield is True:
                self.player_armor = 3
                self.shield = False
            if self.player_health < 1:
                print("Torvinn was slain by Baron Ashbury.")
                self.is_running = False

    def boss_turn(self):
        self.boss_cooldown -= 1
        if self.boss_cooldown == 0:
            self.asphyxiate()
        elif self.soe is True:
            self.stay_of_execution()
        else:
            self.boss_melee()

    def player_turn(self):
        has_acted = False
        self.start_of_player_turn()
        while has_acted is False:
            action = input("Select an ability to perform: ")
            if action.lower() == "crusader strike":
                self.crusader_strike()
                has_acted = True
            elif action.lower() == "avengers shield":
                if self.avengers_cooldown == 0:
                    self.avengers_shield()
                    has_acted = True
                else:
                    print("That ability is on cooldown.")
            elif action.lower() == "shield of the righteous":
                if self.shields_availible > 0:
                    self.shield_of_the_righteous()
                    has_acted = True
                else:
                    print("That ability is on cooldown.")
            elif action.lower() == "consecration":
                if self.consecrate_cooldown == 0:
                    self.consecration += 5
                    self.consecrate_cooldown = 4
                    has_acted = True
                else:
                    print("That ability is on cooldown.")
            elif action.lower() == "flash of light":
                if self.player_mana > 4:
                    self.flash_of_light()
                    has_acted = True
                else:
                    print("Not enough mana.")
            elif action.lower() == "quit":
                self.is_running = False
                has_acted = True
            else:
                print("Not a valid command.")

    def crusader_strike(self):
        damage = 5 - self.boss_armor + randint(1, 4)
        self.boss_health -= damage
        print("Your Crusader Strike hit Baron Ashbury " + str(damage) + " Physical.")

    def avengers_shield(self):
        damage = 7 + randint(1, 4)
        self.boss_health -= damage
        print("Your Avenger's Shield hit Baron Ashbury " + str(damage) + " Holy.")
        self.avengers_cooldown = 5

    def shield_of_the_righteous(self):
        damage = 5 + randint(1, 4)
        self.boss_health -= damage
        print("Your Shield of the Righteous hit Baron Ashbury " + str(damage) + " Holy.")
        self.shield_active += 2
        self.shields_availible -= 1

    def consecration_attack(self):
        damage = randint(1, 4)
        self.boss_health -= damage
        print("Your Consecration hit Baron Ashbury " + str(damage) + " Holy.")
        self.consecration -= 1

    def flash_of_light(self):
        self.channel = True
        self.player_mana -= 5

    def asphyxiate(self):
        print("Baron Ashbury says: This is just too easy.")
        print("Baron Ashbury asphyxiates his foes!")
        self.player_health = 1
        self.boss_cooldown = randint(4, 6)
        self.channel = False
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

    def start_of_player_turn(self):
        if self.consecration > 0:
            self.consecration_attack()
        if self.avengers_cooldown > 0:
            self.avengers_cooldown -= 1
        if self.consecrate_cooldown > 0:
            self.consecrate_cooldown -= 1
        if self.player_mana < 20:
            self.player_mana += 1
            if self.player_mana > 20:
                self.player_mana = 20
        if self.shield_cooldown > 0:
            self.shield_cooldown -= 1
        if self.shield_active > 0:
            self.shield_active -= 1
        if self.shield_cooldown == 0 and self.shields_availible < 3:
            self.shields_availible += 1
            self.shield_cooldown = 10
        print("You have " + str(self.player_health) + " HP remaining.")
        print("You have " + str(self.player_mana) + " mana remaining.")
        print("You have " + str(self.shields_availible) + " charges of Shield of the Righteous availible.")
