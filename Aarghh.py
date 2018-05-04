from random import randint


class TargetDummy:
    "Practice against a target dummy."
    def __init__(self):
        "Sets starting values and introduces variables for both hero and boss."
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
        self.agony_damage = 0
        self.agonized = 0
        self.channel = False
        self.unstable = [0, 0, 0, 0, 0]
        print("Training begins!")
        self.battle()

    def battle(self):
        "Repeatedly runs the player_turn function until the player quits."
        while self.is_running is True:
            self.turn_counter += 1
            self.player_turn()

    def player_turn(self):
        "Allows the player to take one of their actions."
        has_acted = False
        self.start_of_player_turn()
        while has_acted is False:
            "A loop that repeatedly prompts the player to enter a command until they enter the correct code for an ability."
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
                    for n in range(5):
                        if self.unstable[n] == 0:
                            self.unstable[n] += 2
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
        "Damages the enemy and heals you."
        damage_amount = 2 + randint(1, 2)
        self.boss_health -= damage_amount
        heal_amount = 2 * damage_amount
        self.player_health += heal_amount
        if self.player_health > 25:
            self.player_health = 25
        print("Your Drain Soul hit Boss " + str(damage_amount) + " Shadow.")
        print("Your Drain Soul healed you " + str(heal_amount) + " Shadow.")

    def agony(self):
        "Damages the enemy, increases Agony damage and sometimes creates 1 soul shard."
        amount = 1 + self.agony_damage + randint(1, 2)
        self.boss_health -= amount
        print("Your Agony hit Boss " + str(amount) + " Shadow.")
        if self.agony_damage < 4:
            self.agony_damage += 1
        self.agonized -= 1
        shard_gen = randint(1, 4)
        if shard_gen == 1 and self.soul_shards < 6:
            self.soul_shards += 1

    def corruption(self):
        "Damages the enemy."
        amount = 2 + randint(1, 2)
        self.boss_health -= amount
        print("Your Corruption hit Boss " + str(amount) + " Shadow.")
        self.corrupted -= 1

    def healthstone(self):
        "Uses a Healthstone and heals the player."
        amount = 12 + randint(1, 3)
        self.player_health += amount
        if self.player_health > 25:
            self.player_health = 25
        print("Your Healthstone healed you " + str(amount) + " Shadow.")
        self.healthstones -= 1

    def life_tap(self):
        "Increases mana and damages the player."
        self.player_mana += 8
        if self.player_mana > 20:
            self.player_mana = 20
        self.player_health -= 2
        print("Your Life Tap hit you 2 Shadow.")

    def unstable_affliction(self):
        "Damaging effect of Unstable Affliction."
        amount = 4 + randint(1, 2)
        self.boss_health -= amount
        print("Your Unstable Affliction hit Boss " + str(amount) + " Shadow.")

    def start_of_player_turn(self):
        "Automatically runs the damaging functions when appropriate."
        if self.corrupted > 0:
            self.corruption()
        if self.agonized > 0:
            self.agony()
        else:
            self.agony_count = 0
        if self.channel is True:
            self.drain_soul()
            self.channel = False
        for i in range(5):
            if self.unstable[i] > 0:
                self.unstable_affliction()
                self.unstable[i] -= 1
        if self.player_mana < 20:
            self.player_mana += 1
        print("You have " + str(self.player_health) + " HP remaining.")
        print("You have " + str(self.player_mana) + " mana remaining.")
        print("You have " + str(self.soul_shards) + " soul shards.")


class BaronAshbury:
    "Fight against Baron Ashbury."
    def __init__(self):
        "Sets starting values and introduces variables for both hero and boss."
        self.boss_health = 200
        self.is_running = True
        self.turn_counter = 0
        self.boss_cooldown = randint(5, 7)
        self.boss_armor = 2
        self.soe = False
        self.player_health = 25
        self.player_armor = 1
        self.player_mana = 20
        self.corrupted = 0
        self.soul_shards = 3
        self.healthstones = 1
        self.agony_damage = 0
        self.agonized = 0
        self.channel = False
        self.unstable = [0, 0, 0, 0, 0]
        self.soe_amount = self.player_health / 2
        self.player_max = self.player_health
        print("Baron Ashbury yells: Tally ho! The hunt begins!")
        self.battle()

    def battle(self):
        "Repeats the player's turn and the boss' turn until someone's health is depleted."
        while self.is_running is True:
            self.turn_counter += 1
            self.player_turn()
            if self.boss_health < 1:
                if self.is_running is True:
                    print("Baron Ashbury defeated after " + str(self.turn_counter) + " turns!")
                    print("Baron Ashbury yells: Killed by a lowly commoner. How droll...")
                    self.is_running = False
            else:
                self.boss_turn()
            if self.player_health < 1:
                print("Aarghh was slain by Baron Ashbury.")
                print("Baron Ashbury yells: There was no sport in that kill.")
                self.is_running = False

    def player_turn(self):
        "Allows the player to take one of their actions."
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
                    for n in range(5):
                        if self.unstable[n] == 0:
                            self.unstable[n] += 2
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
        "Damages the enemy and heals the player."
        damage_amount = 2 + randint(1, 2)
        self.boss_health -= damage_amount
        heal_amount = 2 * damage_amount
        self.player_health += heal_amount
        if self.player_health > 25:
            self.player_health = 25
        print("Your Drain Soul hit Baron Ashbury " + str(damage_amount) + " Shadow.")
        print("Your Drain Soul healed you " + str(heal_amount) + " Shadow.")

    def agony(self):
        "Damages the enemy, increases Agony damage and sometimes creates a soul shard."
        amount = 1 + self.agony_damage + randint(1, 2)
        self.boss_health -= amount
        print("Your Agony hit Baron Ashbury " + str(amount) + " Shadow.")
        if self.agony_damage < 4:
            self.agony_damage += 1
        self.agonized -= 1
        shard_gen = randint(1, 4)
        if shard_gen == 1 and self.soul_shards < 6:
            self.soul_shards += 1

    def corruption(self):
        "Damages the enemy."
        amount = 2 + randint(1, 2)
        self.boss_health -= amount
        print("Your Corruption hit Baron Ashbury " + str(amount) + " Shadow.")
        self.corrupted -= 1

    def unstable_affliction(self):
        "Damages the enemy."
        amount = 4 + randint(1, 2)
        self.boss_health -= amount
        print("Your Unstable Affliction hit Baron Ashbury " + str(amount) + " Shadow.")

    def healthstone(self):
        "Consumes a Healthstone and heals the player."
        amount = 12 + randint(1, 3)
        self.player_health += amount
        if self.player_health > 25:
            self.player_health = 25
        print("Your Healthstone healed you " + str(amount) + " Shadow.")
        self.healthstones -= 1

    def life_tap(self):
        "Damages the player and grants mana."
        self.player_mana += 8
        self.player_health -= 2
        if self.player_mana > 20:
            self.player_mana = 20
        print("Your Life Tap hit you 2 Shadow.")

    def start_of_player_turn(self):
        "Runs damaging functions when appropriate."
        if self.corrupted > 0:
            self.corruption()
        if self.agonized > 0:
            self.agony()
        else:
            self.agony_count = 0
        if self.channel is True:
            self.drain_soul()
            self.channel = False
        for i in range(5):
            if self.unstable[i] > 0:
                self.unstable_affliction()
                self.unstable[i] -= 1
        if self.player_mana < 20:
            self.player_mana += 1
        if self.boss_health < 1 and self.is_running is True:
            "Ends the game if the boss' health is depleted."
            print("Baron Ashbury defeated after " + str(self.turn_counter) + " turns!")
            print("Baron Ashbury yells: Killed by a lowly commoner. How droll...")
            self.is_running = False
        else:
            print("Baron Ashbury has " + str(self.boss_health) + " HP remaining.")
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
        "Reduces the player to 1 HP and interrupts channels."
        print("Baron Ashbury yells: This is just too easy...")
        print("Baron Ashbury casts Asphxiation!")
        self.player_health = 1
        self.boss_cooldown = randint(5, 7)
        self.channel = False
        self.soe = True

    def stay_of_execution(self):
        "Heals the player for half of their maximum HP."
        print("Baron Ashbury yells: HA! Let's at least keep it interesting!")
        print("Baron Ashbury casts Stay of Execution!")
        self.player_health += self.soe_amount
        if self.player_health > self.player_max:
            self.player_health = self.player_max
        self.soe = False

    def boss_melee(self):
        "Damages the player."
        damage = 8 - self.player_armor + randint(1, 4)
        self.player_health -= damage
        print("Baron Ashbury Melee hit you " + str(damage) + " Physical.")
