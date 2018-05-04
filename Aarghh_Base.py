        # Add these to setup
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


    def player_turn(self):
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
        amount = 4 + randint(1, 2)
        self.boss_health -= amount
        self.player_health += amount
        if self.player_health > 25:
            self.player_health = 25
        print("Your Drain Soul hit Boss " + str(amount) + " Shadow.")
        print("Your Drain Soul healed you " + str(amount) + " Shadow.")

    def agony(self):
        amount = 2 + self.agony_count + randint(1, 2)
        self.boss_health -= amount
        print("Your Agony hit Boss " + str(amount) + " Shadow.")
        if self.agony_count < 6:
            self.agony_count += 1
        self.agonized -= 1
        shard_gen = randint(1, 4)
        if shard_gen == 1 and self.soul_shards < 6:
            self.soul_shards += 1

    def corruption(self):
        amount = 2 + randint(1, 2)
        self.boss_health -= amount
        print("Your Corruption hit Boss " + str(amount) + " Shadow.")
        self.corrupted -= 1

    def healthstone(self):
        amount = 12 + randint(1, 3)
        self.player_health += amount
        if self.player_health > 25:
            self.player_health = 25
        print("Your Healthstone healed you " + str(amount) + " Shadow.")
        self.healthstones -= 1

    def life_tap(self):
        self.player_mana += 8
        self.player_health -= 2
        if self.player_mana > 20:
            self.player_mana = 20
        print("Your Life Tap hit you 2 Shadow.")

    def unstable_affliction(self):
        amount = 7 + randint(1, 2)
        self.boss_health -= amount
        print("Your Unstable Affliction hit Boss " + str(amount) + " Shadow.")

    def start_of_player_turn(self):
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
        if self.boss_health < 1:
            #Print the line saying you defeated the boss here
        else:
            print("You have " + str(self.player_health) + " HP remaining.")
            print("You have " + str(self.player_mana) + " mana remaining.")
            print("You have " + str(self.soul_shards) + " soul shards.")
