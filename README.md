# WoW-Pokemon-Style

A Pokemon-like game with characters inspired by World of Warcraft.

Baron Ashbury, Torvinn, Aarghh, and all abilities associated with all characters are owned by Blizzard Entertainment.

File Structure:
The game is played through character files, which represent certain heroes.

These are labelled with a name and do not end with the word "Base."

Currently, two such character files exist: Torvinn the Paladin and Aarghh the Warlock.

Within each character file are several encounters: classes labelled with the name of a boss.

Both character files have access to both existing bosses: the Training Dummy and the sadistic Baron Ashbury.

Files ending with the word "Base" contain the base code for a hero or boss.

These cannot be used to play the game.

Playing the Game:

Run one of the character files.  Enter the name of the class indicating the boss you wish to face, followed by ()

You and the boss will alternate turns.  On your turn, you will be prompted to enter a command.  Commands are listed below.  Capitalization does not matter.  
Entering an incorrect command, or the command for an ability you cannot use, will prompt you to enter another command.

Deplete the boss's health before they deplete yours!

Enter "quit" to prematurely end an encounter.

Torvinn the Paladin:

A strong melee warrior infused with holy power, able to take heavy punishment.

Crusader Strike: Strikes the enemy with your mace, dealing low damage reduced by armor.  This ability has no cooldown.

Avengers Shield: Throws a holy shield at the target, dealing high damage and ignoring armor.  This ability has a 5 round cooldown.

Consecration: Consecrates the ground, dealing light armor-piercing damage to the enemy every round for 5 rounds. This ability has a 4 round cooldown.

Shield of the Righteous: Infuses your shield with holy power, striking the enemy for medium damage ignoring armor.  Increases your armor for 2 rounds, causing you to take less damage. Armor gain is increased while Consecration is active.  Has a 10 round cooldown with 3 charges.

Flash of Light: Channels holy light, healing yourself for massive damage at the start of your next turn.  Costs 5 mana. You regenerate 1 mana per round.

Aarghh the Warlock:

A dark spellcaster who corrupts his enemies' souls and steals their very life.

Corruption: Corrupts the enemy, dealing light damage every round for 5 rounds. 

Agony: Inflicts agony on the enemy, dealing light damage every round for 6 rounds. Damage increases each time it deals damage, up to 4 additional damage.  Bonus is lost if the effect expires.  Damage has a chance to generate a soul shard.  

Unstable Affliction: Curses the enemy, dealing medium damage every round for 2 rounds.  Up to 5 instances can be active at once.  Costs 1 soul shard.

Drain Soul: Drains the target's life essense, dealing low damage to the enemy and high healing to you now and at the start of your next turn.  Costs 4 mana.  You regenerate 1 mana per round.

Life Tap: Sacrifices 2 of your hit points to restore 8 mana.

Healthstone: Consumes a Healthstone, healing you for a massive amount.  Usable once per encounter.

Training Dummy: TargetDummy()

Practice your skills on this dummy!  You will need to manually quit this encounter.

Baron Ashbury: BaronAshbury()

This sadistic undead noble enjoys toying with his victims.

Ashbury will sometimes asphyxiate you, interrupting your channels and reducing your health to 1.  On the following round, he will cast Stay of Execution, healing you for half of your maximum health.
