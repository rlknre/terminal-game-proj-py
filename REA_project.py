'''
CMSC 12: Foundation of Computer Science (Laboratory)

Project
    This exercise is intended for CMSC 12 Project Making

Problem Description:
    Create a one-player turn-based fighting game, with a computer opponent,
    wherein the user must inflict damage to their enemy until either
    player reaches zero health. The game must contain a leaderbaord
    and saving feature.

@author Ralph Kenneth Rea
@date 2022-01-11 12:00
'''

import sys      # for system specific parameters
import random   # random for generating random integers
import time     # retrieved info regarding using the time import
# from www.programiz.com/python-programming/time


def Print_Introduction():
    print('''
    ____________________________________________________________
   /  |                                                         |`
   ```|                  G R E E T I N G S !                    |`
      |                                                         |`
      |      The guild extends its deepest gratitude for your   |`
      |    interest in joining the guild. To formally begin     |`
      |    your adventure with us, may we have the honor to     |`
      |    learn the name you go by in your journeys?           |`
      |                                                         |`
      |                                      - The Guild        |`
      |   ______________________________________________________|___
      |  /                                                         /
      |_/_________________________________________________________/
    ''')    # retrieved from: www.asciiart.eu/art-and-design/borders


def Print_Ending():
    print('''
         _______________________________________________________
        /  |                                                    |`
        ```|                                                    |`
           |   Thank you! The Guild wishes you safe travels.    |`
           |                                                    |`
           |   _________________________________________________|___
           |  /                                                    /
           |_/____________________________________________________/
    ''')


def Print_Loading():
    intro1 = ('''
       Greetings {} ! We are looking forward to working with you.'''
              .format(user))

    # creates a typewriting effect
    for element in intro1:
        time.sleep(0.02)
        sys.stdout.write(element)
        sys.stdout.flush()
    # retrieved from: https://www.codegrepper.com/
    # code-examples/python/python+typewriter+effect

    time.sleep(1.5)
    intro2 = ('''
       Please wait for a little moment before we take you to the
       Guild Room. Thank you so much adventurer!

    ==================================================================''')

    # time.sleep adds lag time before next execution
    for element in intro2:
        time.sleep(0.02)
        sys.stdout.write(element)
        sys.stdout.flush()
    time.sleep(2.5)


def Game_Menu():
    print('''

                     =============================
                          G U I L D   R O O M
                     =============================

    |     This is the guild room where adventurers get to meet       |
    |     one another. At this time, you are only allowed inside     |
    |     the practice grounds.                                      |
    |                                                                |
    |     Select a class and see which fighting style suits you      |
    |     well. You will be sparring with a training dummy that      |
    |     only counters once you attack.                             |
    |                                                                |
    |         ----------- Select a Player Class -----------          |

               [1] Swordwielder: Might with the iron light
               [2] Sorcerer: Arcane strikes are not in vain
               [3] Shielder: Defense is for the benevolence

    |     Once you are done. You will be ranked according to your    |
    |     remaining health points. You have the option to reset      |
    |     all progress or leave and let the next player fight.       |

                       [8] Leaderboard Rankings
                       [9] Restart ALL progress
                       [0] Exit the Guild Room
                        ''')


def Game_Intro(c):
    # utilize player for the whole code
    global player_class
    player_class = c

    if c == "1":
        player_class = "Swordwielder"
    elif c == "2":
        player_class = "Sorcerer"
    elif c == "3":
        player_class = "Shielder"

    # verification part
    introduction = ('''
    =================================================================

                     -----------------------------
                    P R E P A R A T I O N   R O O M
                     -----------------------------

          Greetings {name} ({player}). You are about to enter
          the fighting field. If you wish to change your player
          class or have decided to leave momentarily, now is the
          time to decide.

                         [1] Enter the Field
                         [9] Change Player Class
                         [0] Exit the Guild Room

    =================================================================
    '''.format(player=player_class, name=user))
    print(introduction)


def Damage_Output():
    # returns random value for damage
    global action
    action = random.randint(4, 6)

    if action == 4:
        return random.randint(25, 50)
    if action == 5:
        return random.randint(20, 40)
    if action == 6:
        return random.randint(15, 30)


def User_Attacks():
    # returns attack name based on damage
    if c == "1":
        # swordwielder attacks
        if action == 4:
            return "Strike"
        elif action == 5:
            return "Slash"
        elif action == 6:
            return "Stab"

    elif c == "2":
        # sorcerer attacks
        if action == 4:
            return "Fireball"
        elif action == 5:
            return "Water Whip"
        elif action == 6:
            return "Shockwave"

    elif c == "3":
        # shielder attacks
        if action == 4:
            return "Counter"
        elif action == 5:
            return "Smash"
        elif action == 6:
            return "Bump"


def Enemy_Damage():
    # returns random value for enemy damage
    global counter
    counter = random.randint(7, 9)

    if counter == 7:
        return random.randint(25, 50)
    if counter == 8:
        return random.randint(20, 40)
    if counter == 9:
        return random.randint(15, 30)


def Enemy_Attacks():
    # returns attack name based on enemy damage
    if counter == 7:
        return "punched"
    elif counter == 8:
        return "kicked"
    elif counter == 9:
        return "grappled"


def Sort_Rankings():        # sorts dictionary values (descending order)
    return dict(sorted(rank.items(), key=lambda item: item[1], reverse=True))

    # retrieved from: https://thispointer.com/sort-a-dictionary-by-
    # in-python-in-descending-ascending-order/


def Gameplay():
    # available for global retrieval
    global player_HP
    player_HP = max(0, 125)
    enemy_HP = max(0, 125)

    # game introduction
    game = ('''

           ==================================================

                     -----------------------------
                    P R A C T I C E  G R O U N D S
                     -----------------------------

                          FIGHT! ({player})
                 ======================================
                 ||                                  ||
                 ||        HEALTH: 125/125           ||
                 ||        DUMMY: 125/125            ||
                 ||                                  ||
                 ||       [1] Fight                  ||
                 ||       [0] Change Player Class    ||
                 ||                                  ||
                 ======================================
    '''.format(player=player_class))
    print(game)

    # condt: interate until one health bar reaches zero
    while (player_HP > 0) or (enemy_HP > 0):

        # initialize values for easier call
        enemyLost = Damage_Output()
        youLost = Enemy_Damage()
        youAttack = User_Attacks()
        enemyAttacks = Enemy_Attacks()

        # input option for the fighting gameplay
        move = input("Choice: ")
        if move == "1":
            enemy_HP = enemy_HP - enemyLost

            # condt: if enemy health reaches negative
            if enemy_HP < 0:
                enemy_HP = max(enemy_HP, 0)

                # print winning message
                winner = ('''

           ==================================================

                             HEALTH: {hp}/125
                  You used {you}! It inflicted {dmg1} damage.

                     ------------------------------

                             DUMMY: {ehp}/125
                   The training dummy cannot fight back.

                        Congratulations adventurer!

           ==================================================
                     [9] Heal and Restart the fight
                     [0] Quit. Return to Guild Room
    =================================================================
            '''.format(hp=player_HP, ehp=enemy_HP,
                       dmg1=enemyLost, you=youAttack))

                print(winner)
                Add_Ranking()   # add to dictionary

            else:  # condt: player's health bar first reached zero
                player_HP = player_HP - youLost
                if player_HP < 0:
                    player_HP = max(player_HP, 0)

                    # print losing message
                    loser = ('''

           ==================================================

                           HEALTH: {hp}/125
                 You used {you}! It inflicted {dmg1} damage.

                     ------------------------------

                     The training dummy fought back!
                           DUMMY: {ehp}/125
                   It {enemy} you, dealing {dmg2} damage.

                    Enemy won. That was a fine match!

           ==================================================
                     [9] Heal and Restart the fight
                     [0] Quit. Return to Guild Room
    =================================================================
            '''.format(hp=player_HP, ehp=enemy_HP, dmg1=enemyLost,
                       dmg2=youLost, you=youAttack, enemy=enemyAttacks))
                    print(loser)

            # option choices after one fight game
            if enemy_HP == 0 or player_HP == 0:
                aftergame = input("Choice: ")
                if aftergame == "9":
                    Gameplay()
                elif aftergame == "0":
                    print("Teleporting back to the Guild Room.")
                    break
                else:
                    print("Invalid! Teleporting back to the Guild Room.")
                    break

            # fighting round
            gameon = ('''

           ==================================================
                     P R A C T I C E  G R O U N D S
                     ------------------------------

                           HEALTH: {hp}/125
                 You used {you}! It inflicted {dmg1} damage.
                          Keep the pressure on!

                     ------------------------------

                     The training dummy fought back!
                           DUMMY: {ehp}/125
                   It {enemy} you, dealing {dmg2} damage.

                         [1] Fight
                         [0] Quit. Return to Guild Room
    =================================================================
            '''.format(hp=player_HP, ehp=enemy_HP,
                       dmg1=enemyLost, dmg2=youLost,
                       you=youAttack, enemy=enemyAttacks))

            print(gameon)

            # another loop breaker just in case
            if (player_HP == 0) or (enemy_HP == 0):
                break

        elif move == "9":
            Gameplay()
        elif move == "0":
            print("Teleporting back to the Guild Room.")
            break
        else:
            print("Invalid! Teleporting back to the Guild Room.")
            break


def Loading_Screen():
    print('''

                  L O A D I N G   G U I L D   R O O M

    ==================================================================
          NOTE: Due to a magical imbalance in the region, using
          the wrong input in choosing an option might teleport
          you back to the Guild Room. Sorry for the inconvenience.
    ==================================================================
    ''')


def Add_Ranking():
    # if winner: input user to ranking dictionary and directory
    if user not in rank.keys():
        rank[user] = player_HP
        print("The Guild will remember your bravery. Recorded.")

    else:   # condt: new health is higher than the previous
        if rank[user] < player_HP:
            rank[user] = player_HP
            print("The Guild will remember your bravery. Recorded.")
        else:
            print("The Guild will only record your highest HP")


def Save_Ranking():
    # opens file for writing
    save_Handle = open("Guild Ranking.csv", "w+")

    order = 1
    # iterate until order number is more than dict.length
    while order < (len(rank) + 1):
        for key, value in rank.items():
            place = str(order) + "."
            name = str(key)
            points = str(value)
            save_Handle.write(place + " " + name + " with "
                              + points + " health points " + "\n")
            order = order + 1
    save_Handle.close()


def Load_Ranking():
    # open file for reading
    read_Handle = open("Guild Ranking.csv", "r+")
    rank.clear()

    # retrieve only the users' names and health
    for line in read_Handle:
        data = line[0:-1].split(" ")
        name = data[1]
        rank[name] = int(data[3])
    read_Handle.close()


def Show_Rankings():
    print('''
            ==================================================

                     -----------------------------
                         L E A D E R B O A R D
                     -----------------------------

             Welcome to the Hall of Fame. Meet the adventurers
             who have won the battle with the least amount of
             damage among the rest.

                 ======================================
                   ''')

    order = 1
    # only iterate until three times
    for key, value in rank.items():
        if order != 4:
            print('''                      {}. {} (Health Points: {})'''
                  .format(order, key, value), end="\n")
        order = order + 1
    # key = name, value = health points

    print('''
             =================================================''')
    input("\nPress enter to return to the Guild Room.")
    # no required input, this is only to create a pause


def Clear_Rankings():
    print('''
    ==================================================================

                             W A R N I N G
                     ------------------------------
              This will reset the leaderboard? Are you sure?
                          [1] Yes  |  [0] No

    ==================================================================''')
    print("\nNo traces of previous fights will remain. Are you sure?")

    # input choice for the ranking option
    choice = input("Choice: ")
    if choice == "0":
        print("Teleporting back to the Guild Room.")

    elif choice == "1":
        print("The leaderboard is cleared. A clean slate.")
        print("Teleporting back to the Guild Room.")
        rank.clear()        # delete dictionary elements

        # erase all input in import file
        erase_Handle = open("Guild Ranking.csv", "r+")
        erase_Handle.truncate(0)
        erase_Handle.close()

    else:
        print("Invalid! Teleporting back to the Guild Room.")


# here is the program flow outline
rank = {}           # prepare the dictionary
Load_Ranking()      # for points and players

# initial start of the program
Print_Introduction()
user = input('''       We must call you... ''')
Print_Loading()

# program loops around until input = 0
while True:
    Loading_Screen()
    time.sleep(4.5)     # lag time for effect
    Game_Menu()         # the main menu

    c = input("Choose your destiny: ")
    if c == "1" or c == "2" or c == "3":
        Game_Intro(c)
        option = input("Choice: ")
        if option == "1":
            Gameplay()
            rank = Sort_Rankings()
            Save_Ranking()
        elif option == "9":
            Game_Intro(c)
        elif option == "0":
            break
        else:
            print("Invalid! Teleporting back to the Guild Room.")
            continue
    elif c == "8":
        Show_Rankings()
    elif c == "9":
        Clear_Rankings()
    elif c == "0":
        break
    else:
        print("Invalid! Teleporting back to the Guild Room")

# ending remark for the program
Print_Ending()
