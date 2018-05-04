from random import randint
# Deal with odd last line
# Find out why Unstable Affliction doesn't work


class TargetDummy:
    "Practice against a target dummy."
    def __init__(self):
        "Sets starting values and introduces variables."
        self.boss_health = 10000000
        self.is_running = True
        self.turn_counter = 0
        self.boss_armor = 0
        self.player_health = 25
        self.player_armor = 1
        self.player_mana = 20
        self.corrupted = 0
        self.soul_shards = 3
        self.healthstones = 1
        self.agony_count = 0
        self.agonized = 0
        self.channel = False
        self.unstable = [0, 0, 0, 0, 0]
        print("Training begins!")
        self.battle()

    def battle(self):
        "Creates the round cycle."
        while self.is_running is True:
            self.turn_counter += 1
            self.player_turn()

    def player_turn(self):
        "Allows the player to act."
        has_acted = False
        self.start_of_player_turn()
        while has_acted is False:
            action = input("Select an ability to perform.")
            if action.lower() == "drain soul":
                if self.player_mana > 3:
                    self.drain_soul()
                    self.channel = True
                    self.player_mana -= 4
                    has_acted = True
                else:
                    print("Not enough mana.")
            elif action.lower() == "agony":
                self.agonized = 6
                has_acted = True
            elif action.lower() == "corruption":
                self.corrupted = 5
                has_acted = True
            elif action.lower() == "unstable affliction":
                if self.soul_shards > 0:
                    for n in self.unstable:
                        if n == 0:
                            n += 2
                            self.soul_shards -= 1
                            break
                    has_acted = True
                else:
                    print("Not enough soul shards.")
            elif action.lower() == "healthstone":
                if self.healthstones > 0:
                    self.healthstone()
                    has_acted = True
                else:
                    print("No healthstones availible.")
            elif action.lower() == "life tap":
                self.life_tap()
                has_acted = True
            elif action.lower() == "quit":
                self.is_running = False
                has_acted = True
            else:
                print("Not a valid command.")

    def drain_soul(self):
        "Damaging and healing effect of Drain Soul."
        amount = 4 + randint(1, 2)
        self.boss_health -= amount
        self.player_health += amount
        if self.player_health > 25:
            self.player_health = 25
        print("Your Drain Soul hit Boss " + str(amount) + " Shadow.")
        print("Your Drain Soul healed you " + str(amount) + " Shadow.")

    def agony(self):
        "Damaging effect of Agony."
        amount = 2 + self.agony_count + randint(1, 2)
        self.boss_health -= amount
        print("Your Agony hit Boss " + str(amount) + " Shadow.")
        if self.agony_count < 6:
            self.agony_count += 1
        print(self.agony_count)
        self.agonized -= 1
        shard_gen = randint(1, 4)
        "Generates Soul Shards."
        if shard_gen == 1 and self.soul_shards < 6:
            self.soul_shards += 1

    def corruption(self):
        "Damaging effect of Corruption."
        amount = 2 + randint(1, 2)
        self.boss_health -= amount
        print("Your Corruption hit Boss " + str(amount) + " Shadow.")
        self.corrupted -= 1

    def healthstone(self):
        "Healthstone activation."
        amount = 12 + randint(1, 3)
        self.player_health += amount
        if self.player_health > 25:
            self.player_health = 25
        print("Your Healthstone healed you " + str(amount) + " Shadow.")
        self.healthstones -= 1

    def life_tap(self):
        "Activates Life Tap."
        self.player_mana += 8
        if self.player_mana > 20:
            self.player_mana = 20
        self.player_health -= 2
        print("Your Life Tap hit you 2 Shadow.")

    def unstable_affliction(self):
        "Causes Unstable Affliction to deal damage."
        amount = 7 + randint(1, 2)
        self.boss_health -= amount
        print("Your Unstable Affliction hit Boss " + str(amount) + " Shadow.")

    def start_of_player_turn(self):
        "Manages effect durations."
        if self.corrupted > 0:
            self.corruption()
        if self.agonized > 0:
            self.agony()
        else:
            self.agony_count = 0
        if self.channel is True:
            self.drain_soul()
            self.channel = False
        for n in self.unstable:
            if n > 0:
                self.unstable_affliction()
                n -= 1
        if self.player_mana < 20:
            self.player_mana += 1
        print("You have " + str(self.player_health) + " HP remaining.")
        print("You have " + str(self.player_mana) + " mana remaining.")
        print("You have " + str(self.soul_shards) + " soul shards.")


class BaronAshbury:
    "Fight against Baron Ashbury."
    def __init__(self):
        "Sets starting values and variables."
        self.boss_health = 200
        self.is_running = True
        self.turn_counter = 0
        self.boss_cooldown = randint(4, 6)
        self.boss_armor = 2
        self.soe = False
        self.player_health = 25
        self.player_armor = 1
        self.player_mana = 20
        self.corrupted = 0
        self.soul_shards = 3
        self.healthstones = 1
        self.agony_count = 0
        self.agonized = 0
        self.channel = False
        self.unstable = [0, 0, 0, 0, 0]
        self.soe_amount = self.player_health / 2
        self.player_max = self.player_health
        self.battle()

    def battle(self):
        "Sets the structure of the encounter."
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

    def player_turn(self):
        "Allows the player to act."
        has_acted = False
        self.start_of_player_turn()
        while has_acted is False and self.is_running is True:
            action = input("Select an ability to perform.")
            if action.lower() == "drain soul":
                if self.player_mana > 3:
                    self.drain_soul()
                    self.channel = True
                    self.player_mana -= 4
                    has_acted = True
                else:
                    print("Not enough mana.")
            elif action.lower() == "agony":
                self.agonized = 6
                has_acted = True
            elif action.lower() == "corruption":
                self.corrupted = 5
                has_acted = True
            elif action.lower() == "unstable affliction":
                if self.soul_shards > 0:
                    for n in self.unstable:
                        if n == 0:
                            n += 2
                            self.soul_shards -= 1
                            break
                    has_acted = True
                else:
                    print("Not enough soul shards.")
            elif action.lower() == "healthstone":
                if self.healthstones > 0:
                    self.healthstone()
                    has_acted = True
                else:
                    print("No healthstones availible.")
            elif action.lower() == "life tap":
                self.life_tap()
                has_acted = True
            elif action.lower() == "quit":
                self.is_running = False
                has_acted = True
            else:
                print("Not a valid command.")

    def drain_soul(self):
        "Drain Soul damaging/healing effect."
        amount = 4 + randint(1, 2)
        self.boss_health -= amount
        self.player_health += amount
        if self.player_health > 25:
            self.player_health = 25
        print("Your Drain Soul hit Boss " + str(amount) + " Shadow.")
        print("Your Drain Soul healed you " + str(amount) + " Shadow.")

    def agony(self):
        "Agony damaging effect."
        amount = 2 + self.agony_count + randint(1, 2)
        self.boss_health -= amount
        print("Your Agony hit Boss " + str(amount) + " Shadow.")
        if self.agony_count < 6:
            self.agony_count += 1
        self.agonized -= 1
        shard_gen = randint(1, 4)
        "Generates Soul Shards."
        if shard_gen == 1 and self.soul_shards < 6:
            self.soul_shards += 1

    def corruption(self):
        "Corruption damaging effect."
        amount = 2 + randint(1, 2)
        self.boss_health -= amount
        print("Your Corruption hit Boss " + str(amount) + " Shadow.")
        self.corrupted -= 1

    def healthstone(self):
        "Activates Healthstone."
        amount = 12 + randint(1, 3)
        self.player_health += amount
        if self.player_health > 25:
            self.player_health = 25
        print("Your Healthstone healed you " + str(amount) + " Shadow.")
        self.healthstones -= 1

    def life_tap(self):
        "Activates Life Tap."
        self.player_mana += 8
        self.player_health -= 2
        if self.player_mana > 20:
            self.player_mana = 20
        print("Your Life Tap hit you 2 Shadow.")

    def start_of_player_turn(self):
        "Manages durations."
        if self.corrupted > 0:
            self.corruption()
        if self.agonized > 0:
            self.agony()
        else:
            self.agony_count = 0
        if self.channel is True:
            self.drain_soul()
            self.channel = False
        for n in self.unstable:
            if n > 0:
                self.unstable_affliction()
                n -= 1
        if self.player_mana < 20:
            self.player_mana += 1
        if self.boss_health < 1 and self.is_running is True:
            print("Baron Ashbury defeated after " + str(self.turn_counter) + " turns!")
            self.is_running = False
        else:
            print("You have " + str(self.player_health) + " HP remaining.")
            print("You have " + str(self.player_mana) + " mana remaining.")
            print("You have " + str(self.soul_shards) + " soul shards.")

    def boss_turn(self):
        "The boss acts."
        self.boss_cooldown -= 1
        if self.boss_cooldown == 0:
            self.asphyxiate()
        elif self.soe is True:
            self.stay_of_execution()
        else:
            self.boss_melee()

    def asphyxiate(self):
        "Ashyxiation activates."
        print("Baron Ashbury says: This is just too easy.")
        print("Baron Ashbury asphyxiates his foes!")
        self.player_health = 1
        self.boss_cooldown = randint(4, 6)
        self.channel = False
        self.soe = True

    def stay_of_execution(self):
        "Stay of Execution activates."
        print("Baron Ashbury says: I'll keep you alive to witness your screams.")
        print("Baron Ashbury delays your execution!")
        self.player_health += self.soe_amount
        if self.player_health > self.player_max:
            self.player_health = self.player_max
        self.soe = False

    def boss_melee(self):
        "The boss' melee attack."
        damage = 8 - self.player_armor + randint(1, 4)
        self.player_health -= damage
        print("Baron Ashbury Melee hit you " + str(damage) + " Physical.")
