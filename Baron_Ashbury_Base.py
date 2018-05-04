from random import randint


class BaronAshbury:
    def __init__(self):
        self.boss_health = 200
        self.is_running = True
        self.turn_counter = 0
        self.boss_cooldown = randint(4, 6)
        self.boss_armor = 2
        self.soe = False
        # Player info goes here
        self.soe_amount = self.player_health / 2
        self.player_max = self.player_health
        self.battle()

    def battle(self):
        while self.is_running is True:
            print("Baron Ashbury has " + str(self.boss_health) + " HP remaining.")
            self.turn_counter += 1
            self.player_turn()
            if self.boss_health < 1 and self.is_running is True:
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
        elif self.soe is True:
            self.stay_of_execution()
        else:
            self.boss_melee()

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
        self.player_health += self.soe_amount
        if self.player_health > self.player_max:
            self.player_health = self.player_max
        self.soe = False

    def boss_melee(self):
        damage = 8 - self.player_armor + randint(1, 4)
        self.player_health -= damage
        print("Baron Ashbury Melee hit you " + str(damage) + " Physical.")


BaronAshbury()
