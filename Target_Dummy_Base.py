class TargetDummy:
    "Practice against a target dummy."
    def __init__(self):
        "Sets starting values and introduces variables for both hero and boss."
        self.boss_health = 10000000
        self.is_running = True
        self.boss_armor = 0
        # Player info goes here
        self.battle()

    def battle(self):
        "Repeatedly runs player_turn until the player quits."
        while self.is_running is True:
            self.turn_counter += 1
            self.player_turn()
