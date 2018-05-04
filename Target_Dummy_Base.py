from random import randint


class TargetDummy:
    def __init__(self):
        self.boss_health = 10000000
        self.is_running = True
        self.turn_counter = 0
        self.boss_armor = 0
        self.battle

    def battle(self):
        while self.is_running is True:
            self.turn_counter += 1
            self.player_turn()
