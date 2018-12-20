import sys
import os
import time
import curses

class Player:
    def __init__(self, name):
        self.name = name
        self.maxHealth = 1000
        self.health = self.maxHealth
        self.attack = 100
        self.gold = 0
        self.pots = 0
        self.level = 1
        self.exp = 0
        self.expNextLevel = 10
        self.totalExp = 0

def main():
    stdscr = curses.initscr()
    curses.curs_set(0)
    os.system('cls')
    strLength = 0
    d1 = """\n    The Gladiator of Slawnell\n
    Please select one of the options below """
    for char in d1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.08)
    print ("""
    1.) NEW GAME
    2.) LOAD GAME
    3.) QUIT """)
    curses.flushinp()
    option = input("    ->")
    if option == "1":
        intro()
    elif option == "2":
        load()
    elif option == "3":
        sys.exit()
    else:
        print ("please select 1,2,or 3")
        main()

def intro():
    os.system('cls')
    strLength = 0
    d1 = """\n
    Dr.Bees: *clears throat*" Hello there! Welcome to Slawnell!
             I'm Dr. Bees the record keeper of this fine town.
             I track progress and information on everything and anything about all who pass through here.
             However, by the heavy bags on your back i can tell you didn't come here to listen to me
             talk about myself all day now did you? So then. What is your name traveler?" """
    for char in d1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.03)
    characterCreate ()

def characterCreate():
    print ("""

    TYPE IN YOUR CHARACTER'S NAME BELOW\n
     """)
    curses.flushinp()
    charName = input("  ->")
    global playerIG
    playerIG = Player(charName)
    intro1()

def load():
    os.system('cls')
    main()

def intro1():
    os.system('cls')
    d1 = """\n
    Dr.Bees: "Ah %s is it? let me see if i have you on record...
             Yes yes, here you are. You must have come here once before.
             This is all the information I have on you for the moment." """ %playerIG.name
    d2 = """
    Dr.Bees: "(and thankfully no criminal record... yet.)
             Now now, don't look so discouraged
             you can always come back to me whenever you want to update your record." """
    d3 = """
    Dr.Bees: "As you may recall Slawnell is a very sucessful town with tons of ways to earn gold
             and well... spend it OHOHO! Someone as youthful and strong as yourself
             may do well in our local arena as an entertainer. Now don't worry we aren't barbarians
             here we don't battle each other, rather our guards capture the lowly monsters
             we find on our roads harrassing travelers such as yourself and then well...
             repurpose them!
             As long as you mind your vitality and wits, I Dr.bees am sure you won't fail!" """
    d4 = """
    Dr.Bees: "After you have earned some gold go visit the shop to buy potions and
             new equpiment. The tier of your equipment will determine
             the kinds of enemies you face in the arena so be prepared." """
    d5 = """
    Dr.Bees: "Once you are good and tired from battle feel free to rest at Slawnell's Inn.
             Remember if your body doesn't heal properly your strength won't improve.
             Infact, you may find yourself weaker than you once were! What a fucking waste!" """
    d6 = """
    Dr.Bees: "I believe I have yammered on enough.
             please go on ahead into town and once again Welcome to Slawnell!" """
    for char in d1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.03)
    print ("""


             Health: %i/%i
             Attack: %i
             Gold: %i
             Potions: %i
             Level: %i
             Exp: %i
             Exp to next Level: %i
             Total exp: %i
             """ %(playerIG.health, playerIG.maxHealth, playerIG.attack, playerIG.gold, playerIG.pots, playerIG.level, playerIG.exp, playerIG.expNextLevel, playerIG.totalExp))
    cont = input ('  ->')
    os.system('cls')
    curses.flushinp()
    for char in d2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.03)
    cont = input ('  ->')
    os.system('cls')
    curses.flushinp()
    for char in d3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.03)
    cont = input ('  ->')
    os.system('cls')
    curses.flushinp()
    for char in d4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.03)
    cont = input ('  ->')
    os.system('cls')
    curses.flushinp()
    for char in d5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.03)
    cont = input ('  ->')
    os.system('cls')
    curses.flushinp()
    for char in d6:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.03)
    cont = input ('  ->')
    curses.flushinp()

main()
