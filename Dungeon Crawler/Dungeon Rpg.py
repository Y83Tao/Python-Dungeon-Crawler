import turtle
from turtle import Turtle, Shape, Screen
from tkinter import PhotoImage
import time
import os
import sys
import cmd
import textwrap
import random

#Dungeon Crawler by Yun Tao
#This is perferablly played on window's terminal rather IDLE
#When you die the program should crash for a shocking look<<<<<<
#Starting screen:

#Setting up screeen and shapes

screen = turtle.Screen()
screen.setup(720, 720)
screen.bgcolor("black")

def gamesequence(screen):
       introduction()
       classtype(screen)
       Stage1introduction()
       freemode()
       turtle.done()

def startingscreen(screen):
       os.system('cls')
       os.system("mode con cols=75 lines=25")

       os.system("mode con cols=75 lines=25")
       print("==============================")
       print("====== Dungeon Crawler  ======")
       print("==============================")
       print("By: Yun Tao")
       print("")
       print("[1] Play ")
       print("[2] About ")
       print("[3] Quit ")
       print("Culminating Project")
       start = int(input())
       if start == 1:
              os.system('cls')
              os.system("mode con cols=75 lines=25")
              os.system("mode con cols=75 lines=25")
              gamesequence(screen)
       elif start == 2:
              os.system('cls')
              os.system("mode con cols=75 lines=25")
              os.system("mode con cols=75 lines=25")
              writeup("""A dungeon crawler that took ages
to make! Made sure this uses
modules that already exists
in python. Hope that this
game good!""", 0.03)
              print("")
              print("Continue ['e]")
              next = input()
              startingscreen(screen)
       elif start == 3:
              print("You cant exit u fool")
              print("Type anything to go back")
              back = input()
              startingscreen(screen)             
       else:
              print("Please type a valid input")
              print("Type anything to go back")
              back = input()
              startingscreen(screen)
#Setting up dialogue text setup with the delay that resembles an rpg style dialogue
def writeup(sentence, timestuff):
       for character in sentence:
              sys.stdout.write(character)
              sys.stdout.flush()
              time.sleep(timestuff)
#adding fog of war stages for stage 2
#adding fog of war stages for stage 1
#screen.addshape("Stage1fog1.gif")
#######################################################################
for i in range(12):
       b = i + 1
       if b == 13:
              break
       screen.addshape("Stage2fog" + str(b) + ".gif")
stg2fog1 = turtle.Turtle()
stg2fog2 = turtle.Turtle()
stg2fog3 = turtle.Turtle()
stg2fog4 = turtle.Turtle()
stg2fog5 = turtle.Turtle()
stg2fog6 = turtle.Turtle()
stg2fog7 = turtle.Turtle()
stg2fog8 = turtle.Turtle()
stg2fog9 = turtle.Turtle()
stg2fog10 = turtle.Turtle()
stg2fog11 = turtle.Turtle()
stg2fog12 = turtle.Turtle()
fogvariablesstg2 =  [stg2fog1, stg2fog2, stg2fog3, stg2fog4, stg2fog5, stg2fog6, stg2fog7,
stg2fog8, stg2fog9, stg2fog10, stg2fog11, stg2fog12]
stg2nums = 13
for i in range(12):
       stg2nums = stg2nums - 1
       secondstgnum = stg2nums - 1
       if stg2nums == 0:
              break
       fogvariablesstg2[secondstgnum].shape("Stage2fog" + str(stg2nums) + ".gif")


for i in range(7, -1, -1):
       if i == 0:
              break
       screen.addshape("Stage1fog" + str(i) + ".gif")
fog1 = turtle.Turtle()
fog2 = turtle.Turtle()
fog3 = turtle.Turtle()
fog4 = turtle.Turtle()
fog5 = turtle.Turtle()
fog6 = turtle.Turtle()
fog7 = turtle.Turtle()
fogvariables = [fog1, fog2, fog3, fog4, fog5, fog6, fog7]
for i in range(6, -1, -1):
       b = i + 1
       if i == -1:
              break
       else:
              fogvariables[i].shape("Stage1fog" + str(b) + ".gif")
screen.addshape("black moon.gif")
titleimage = turtle.Turtle()

#Character stats Character stats Character stats Character stats Character stats Character stats
Playerhealth = 100
Playerdamage = 10
Playerdefense = 0.1
Scrolldamagemultiplier = 0.1 
Potioneffect = 1
Criticaldamage = 2

#Items Items Items Items Items Items Items Items Items Items Items Items Items Items Items Items
Potion_of_health = 0
Firescroll = 0
Essence_of_attack = 0
Essence_of_critical_strike = 0
LeatherHelm = 1
LeatherChestplate = 1
IronHelm = 0
IronChestplate = 0
DragonHelm = 0
DragonChestplate = 0
BasicBow = 0
IronBow = 0
FireBow = 0
WoodenSword = 0
IronSword = 0
DragonSword = 0
WoodenWand = 0
EnchantedWand = 0
WarWand = 0

def Potion_of_healing():
       global Potion_of_health
       global Potioneffect
       global Playerhealth
       if "Potion_of_health" in inventory:
              Playerhealth += (30 * Potioneffect)
              writeup("Healed 30 health points!", 0.04)
              inventory.remove("Potion_of_health")
       else:
              print("You do not have any potions!")
def Scroll_of_dmg():
       global Firescroll
       global scrolldamagemultiplier
       if Firescroll > 0:
              return True
def Essence_of_attack_upgrade():
       global Essence_of_attack
       global Playerdamage
       if "Essence_of_attack" in inventory:
              Playerdamage += 5
              writeup("You gained +5 attack damage!", 0.04)
              print("")
              writeup("Damage = " + str(Playerdamage), 0.04)
              inventory.remove("Essence_of_attack")

              
       
       
#Inventory Inventory Inventory Inventory Inventory Inventory Inventory Inventory Inventory Inventory
              
Equipment = ["LeatherHelm", "LeatherChestplate", "WoodenSword"]
inventory = ["Firescroll", "Potion_of_health"]
Blackorbs = 15
powerattack = 2
ultimate = 0

def inventorydisplay():
       global Equipment
       global inventory
       print("======================")
       print("Equipment = " + str(Equipment))
       print("Inventory = " + str(inventory))
def inventorycheck():
       global Playerdamage
       global Playerhealth
       global Playerdefense
       if "LeatherHelm" in Equipment:
              Playerdefense += 0.05
       if "IronHelm" in Equipment:
              Playerdefense += 0.1
       if "DragonHelm" in Equipment:
              Playerdefense += 0.15
       if "LeatherChestplate" in Equipment:
              Playerdefense += 0.1
       if "IronChestplate" in Equipment:
              Playerdefense += 0.15
       if "DragonChestplate" in Equipment:
              Playerdefense += 0.2
       if "WoodenSword" in Equipment:
              Playerdamage += 10
       if "IronSword" in Equipment:
              Playerdamage += 20
       if "DragonSword" in Equipment:
              Playerdamage += 50
       if "BasicBow" in Equipment:
              Playerdamage += 15
       if "IronBow" in Equipment:
              Playerdamage += 30
       if "FireBow" in Equipment:
              Playerdamage += 65
       if "WoodenWand" in Equipment:
              Playerdamage += 20
       if "EnchantedWand" in Equipment:
              Playerdamage += 40
       if "WarWand" in Equipment:
              Playerdamage += 75
def inventoryremovecheck():
       global Playerdamage
       global Playerhealth
       global Playerdefense
       if "LeatherHelm" in Equipment:
              Playerdefense -= 0.05
       if "IronHelm" in Equipment:
              Playerdefense -= 0.1
       if "DragonHelm" in Equipment:
              Playerdefense -= 0.15
       if "LeatherChestplate" in Equipment:
              Playerdefense -= 0.1
       if "IronChestplate" in Equipment:
              Playerdefense -= 0.15
       if "DragonChestplate" in Equipment:
              Playerdefense -= 0.2
       if "WoodenSword" in Equipment:
              Playerdamage -= 10
       if "IronSword" in Equipment:
              Playerdamage -= 20
       if "DragonSword" in Equipment:
              Playerdamage -= 50
       if "BasicBow" in Equipment:
              Playerdamage -= 15
       if "IronBow" in Equipment:
              Playerdamage -= 30
       if "FireBow" in Equipment:
              Playerdamage -= 65
       if "WoodenWand" in Equipment:
              Playerdamage -= 20
       if "EnchantedWand" in Equipment:
              Playerdamage -= 40
       if "WarWand" in Equipment:
              Playerdamage -= 75


def equipmentnavigation():
       os.system('cls')
       os.system("mode con cols=75 lines=25")
       print("================")
       inventoryindex = []
       for i in range(len(Equipment)):
              writeup("[" + str(i) + "] - " + str(Equipment[i]), 0.01)
              print("")
              inventoryindex.append(int(i))
       print("[Unequip] = [index number]")
       print("[Exit] = [Just 'p']")
       choicelol = input()
       if choicelol == "p":
              exit
       elif len(choicelol) > 1:
              print("Please input a valid response")
              print("Continue ['e']")
              navigationcontinue = input()
              equipmentnavigation()
       elif str(choicelol) in alphabet:
              print("Please input a valid response")
              print("Continue ['e']")
              navigationcontinue = input()
              equipmentnavigation()
       elif int(choicelol) > len(Equipment):
              print("Please input a valid response")
              print("Continue ['e']")
              navigationcontinue = input()
              equipmentnavigation()
       elif int(choicelol) in inventoryindex:
              inventory.append(Equipment[(int(choicelol))])
              del Equipment[(int(choicelol))]
              equipmentnavigation()
       else:
              print("Please input a valid response")
              equipmentnavigation()
def inventorynavigation():
       os.system('cls')
       os.system("mode con cols=75 lines=25")
       print("=================")
       print("Inventory:")
       indexes = []
       for i in range(len(inventory)):
              writeup("[" + str(i) + "] - " + str(inventory[i]), 0.01)
              print("")
              indexes.append(int(i))
       print("[Inspect] [i]")
       print("[Use] [o]")
       print("[Exit] [just 'p']")
       print("Usage ; [index, purpose] e.g ['0, i']")
       usage(input(), indexes)

def easierwayofdoinginventorycheck(item, statement, typeof, itemsnot1, itemsnot2, itemsnot3, optioninventorynum, indexes, choices):
              if inventory[optioninventorynum] == item:
                     if choices == "i":
                            os.system("cls")
                            writeup(statement, 0.03)
                            print("")
                            print("Continue ['e']")
                            continuee = input()
                            inventorynavigation()
                     elif choices == "o":
                            os.system("cls")
                            if itemsnot1 not in Equipment and itemsnot2 not in Equipment and itemsnot3 not in Equipment:
                                   inventory.remove(item)
                                   Equipment.append(item)
                                   inventorynavigation()
                            else:
                                   print("Another " + str(typeof) + " is currently in place!")
                                   print("")
                                   print("Continue ['e']")
                                   continuee = input()                            
                                   inventorynavigation()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '']
def usage(optioninventory, indexes):
       if optioninventory == "p":
              freemode()
       elif (len(optioninventory)) < 4:
              print("please print a valid choice")
              usage(input(), indexes)
       elif optioninventory[0] in alphabet: 
              print("please print a valid choice")
              usage(input(), indexes)
       elif (int(optioninventory[0])) > (len(inventory)):
              print("please print a valid choice")
              usage(input(), indexes)
       optioninventorynum = int(optioninventory[0])
       choices = optioninventory[3]
       if (len(optioninventory)) == 5:
              if optioninventory[0] not in alphabet and optioninventory[1] not in alphabet:
                     optioninventorynum = int(str(optioninventory[0]) + str(optioninventory[1]))
                     choices = str(optioninventory[4])
       if optioninventorynum in indexes:
              if inventory[optioninventorynum] == "Potion_of_health":
                     if choices == "i":
                            os.system("cls")
                            writeup("""A magical potion with magical powers!
effects:
+30 Health Points""", 0.03)
                            print("")
                            print("Continue ['e']")
                            continuee = input()
                            inventorynavigation()
                     elif choices == "o":
                            os.system("cls")
                            Potion_of_healing()
                            print("")
                            print("Continue ['e']")
                            continuee = input()                            
                            inventorynavigation()
              if inventory[optioninventorynum] == "Firescroll":
                     os.system("cls")
                     if choices == "i":
                            writeup(""" A fire scroll that summons fire!
Effects:
Deals 65 damage""", 0.04)
                            print("")
                            print("Continue ['e']")
                            continuee = input()
                            inventorynavigation()
                     elif choices == "o":
                            os.system('cls')
                            os.system("mode con cols=75 lines=25")
                            writeup("Cannot use unless in battle!", 0.04)
                            print("")
                            print("Continue ['e']")
                            continuee = input()  
                            inventorynavigation()
              if inventory[optioninventorynum] == "Essence_of_attack":
                     if choices == "i":
                            os.system("cls")
                            writeup("""A glowing red orb that is ment to be consumed!
Effects:
Base attack +5""", 0.03)
                            print("")
                            print("Continue ['e']")
                            continuee = input()
                            inventorynavigation()
                     elif choices == "o":
                            os.system("cls")
                            Essence_of_attack_upgrade()
                            print("")
                            print("Continue ['e']")
                            continuee = input()                            
                            inventorynavigation()
              if inventory[optioninventorynum] == "Key":
                     os.system("cls")
                     if choices == "i":
                            writeup("""A golden key that is used for unlocking
specific doors""", 0.04)
                            print("")
                            print("Continue ['e']")
                            continuee = input()
                            inventorynavigation()
                     elif choices == "o":
                            os.system('cls')
                            os.system("mode con cols=75 lines=25")
                            writeup("Cannot use unless interacting with door", 0.04)
                            print("")
                            print("Continue ['e']")
                            continuee = input()  
                            inventorynavigation()
              if inventory[optioninventorynum] == "LeatherHelm":
                     if choices == "i":
                            os.system("cls")
                            writeup("""Fine piece of leather that protects your head!
Effects:
Defense +0.05""", 0.03)
                            print("")
                            print("Continue ['e']")
                            continuee = input()
                            inventorynavigation()
                     elif choices == "o":
                            os.system("cls")
                            if "IronHelm" not in Equipment and "DragonHelm" not in Equipment and "LeatherHelm" not in Equipment:
                                   inventory.remove("LeatherHelm")
                                   Equipment.append("LeatherHelm")
                                   inventorynavigation()
                            else:
                                   print("Another helmet is currently in place!")
                                   print("")
                                   print("Continue ['e']")
                                   continuee = input()                            
                                   inventorynavigation()
              if inventory[optioninventorynum] == "LeatherChestplate":
                     if choices == "i":
                            os.system("cls")
                            writeup("""Fine piece of leather that protects your chest!
Effects:
Defense +0.1""", 0.03)
                            print("")
                            print("Continue ['e']")
                            continuee = input()
                            inventorynavigation()
                     elif choices == "o":
                            os.system("cls")
                            if "IronChestplate" not in Equipment and "DragonChestplate" not in Equipment and "LeatherChestplate" not in Equipment:
                                   inventory.remove("LeatherChestplate")
                                   Equipment.append("LeatherChestplate")
                                   inventorynavigation()
                            else:
                                   print("Another helmet is currently in place!")
                                   print("")
                                   print("Continue ['e']")
                                   continuee = input()                            
                                   inventorynavigation()
              easierwayofdoinginventorycheck("IronChestplate", """I fine piece of iron that protects your skin!
effects:
Defense +0.15""", "chestpiece", "DragonChestplate", "LeatherChestplate", "IronChestplate", optioninventorynum, indexes, choices)
              easierwayofdoinginventorycheck("DragonChestplate", """A fine piece of dragonscales that protects your skin!
effects:
Defense +0.2""", "chestpiece", "DragonChestplate", "LeatherChestplate", "IronChestplate", optioninventorynum, indexes, choices)
              easierwayofdoinginventorycheck("IronHelm", """A fine piece of iron that protects your face!
effects:
Defense +0.1""", "chestpiece", "DragonHelm", "LeatherHelm", "IronHelm", optioninventorynum, indexes, choices)
              easierwayofdoinginventorycheck("DragonHelm", """A fine piece of dragonscale that protects your face!
effects:
Defense +0.15""", "chestpiece", "DragonHelm", "LeatherHelm", "IronHelm", optioninventorynum, indexes, choices)
              easierwayofdoinginventorycheck("WoodenSword", """A oak crafted sword, typically used for training.
effects:
Damage +10""", "sword", "IronSword", "DragonSword", "WoodenSword", optioninventorynum, indexes, choices)
              easierwayofdoinginventorycheck("DragonSword", """A dragonscale-crafted sword, typically used for slaying
large beasts.
effects:
Damage +50""", "sword", "IronSword", "DragonSword", "WoodenSword", optioninventorynum, indexes, choices)
              easierwayofdoinginventorycheck("IronSword", """A iron-crafted sword, typically used for fighting your average enemie.
effects:
Damage +20""", "sword", "IronSword", "DragonSword", "WoodenSword", optioninventorynum, indexes, choices)
              easierwayofdoinginventorycheck("BasicBow", """A basic or weak bow, typically used for archery.
effects:
Damage +15""", "bow", "FireBow", "BasicBow", "IronBow", optioninventorynum, indexes, choices)
              easierwayofdoinginventorycheck("IronBow", """A well crafted or iron Bpw, typically used to pierce iron
plated enemies.
effects:
Damage +30""", "bow", "FireBow", "BasicBow", "IronBow", optioninventorynum, indexes, choices)
              easierwayofdoinginventorycheck("FireBow", """A strong bow with fire, typically used for slaying beasts from
the sky.
effects:
Damage +65""", "bow", "FireBow", "BasicBow", "IronBow", optioninventorynum, indexes, choices)
              easierwayofdoinginventorycheck("WoodenWand", """A wooden-crafted wand, typically used for practicing
sorcery.
effects:
Damage +20""", "wand", "WoodenWand", "EnchantedWand", "WarWand", optioninventorynum, indexes, choices)
              easierwayofdoinginventorycheck("EnchantedWand", """A oak-crafted wand that glows with pride, typically
used in sorcery battles.
effects:
Damage +40""", "wand", "WoodenWand", "EnchantedWand", "WarWand", optioninventorynum, indexes, choices)
              easierwayofdoinginventorycheck("WarWand", """A dark-oak-crafted wand, typically used for performing
devastating black magic.
effects:
Damage +75""", "wand", "WoodenWand", "EnchantedWand", "WarWand", optioninventorynum, indexes, choices)

                                   
       else:
              print("please print a valid choice")
              usage(input(), indexes)

def blackorbnavi():
       global Blackorbs
       global Playerdamage
       global Playerdefense
       os.system('cls')
       os.system("mode con cols=75 lines=25")
       print("==========================")
       writeup("Black Orbs = " + str(Blackorbs) + "/30", 0.02)
       print("")
       print("==========================")
       writeup("""Orbs are used to upgrade your base stats, once
there is a sufficent amount you can consume
the orbs.""", 0.01)
       print("")
       print("")
       print("['e'] Consume Orbs")
       print("[just 'p'] Leave")
       choicekms = input()
       if choicekms == "e":
              os.system('cls')
              os.system("mode con cols=75 lines=25")
              if Blackorbs >= 30:
                     Playerdamage += 5
                     Playerdefense += 0.02
                     os.system('cls')
                     os.system("mode con cols=75 lines=25")
                     writeup("You consumed the orb!", 0.02)
                     print("")
                     writeup("+5 Atk, +%2 def", 0.02)
                     print("")
                     Blackorbs -= 30
                     print("Continue ['e']")
                     lollikeitmatter = input()
                     blackorbnavi()
              else:
                     writeup("Not enough orbs!", 0.02)
                     print("Continue ['e']")
                     lollikeitmatter = input()
                     blackorbnavi()
       else:
              freemode()


 #Class setup   Class setup  Class setup  Class setup  Class setup  Class setup  Class setup  Class setup  Class setup  Class setup      

def classtype(screen):
       global character
       global Playerdamage
       global Playerdefense
       os.system('cls')
       os.system("mode con cols=75 lines=25")
       writeup("Hello " + str(name) + ", a great adventure awaits." , 0.04)
       print("")
       writeup("""You will now pick a class that will define the way you
play!""", 0.04)
       time.sleep(0.05)
       print("")
       writeup("Pick one of the following classes:", 0.04)
       print("")
       writeup("""[1] - Knight [Defense 30] [Attack 10] 
[2] - Archer [Defense 20] [Attack 20] 
[3] - Wizard [Defense 10] [Attack 30]""", 0.02)
       print("")
       writeup("""The variables above are the base stats of
each class, whereas the health always starts
at 100""", 0.04)
       print("")
       class_choice = int(input(": "))        
       if class_choice == 1:
              character = "Knight.gif"
              screen.addshape(character)
              createcharacter()
              Playerdamage = 10
              Playerdefense = 0.3
       elif class_choice == 2:
              character = "Archer.gif"
              screen.addshape(character)
              createcharacter()
              Playerdamage = 20
              Playerdefense = 0.2
       elif class_choice == 3:
              character = "Wizard.gif"
              screen.addshape(character)
              createcharacter()
              Playerdamage = 30
              Playerdefense = 0.1

def introduction():
       os.system('cls')
       os.system("mode con cols=75 lines=25")
       global name
       writeup("Welcome Adventurer! Your Journey Beings here....", 0.04)
       print("")
       writeup("What is you name?", 0.04)
       name = input(": ")
              
def createcharacter():
       global knight
#Setting up image scalings
       larger = PhotoImage(file=character).subsample(9, 9)
       screen.addshape("larger", Shape("image", larger))
#Starting Position
       knight = Turtle("larger")
       knight.penup()
       knight.setx(160)
       knight.sety(187)

#Starting bit
titleimage.shape("black moon.gif")
titleimage.hideturtle()
screen.textinput("Setup", """Please move terminal and turtle on two ends of the screen.
IMPORTANT: Please use the windows
terminal rather than IDLE for the most
optimal experience.
Press enter when done""")

#Map TIles set

#Stage 1
#X = 1-19 Y = 1-17
#Starting tile is 15 17
stagelevel = 1
Ycord = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V"]
Xcord = ["1", "2","3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
yp = 0
xp = 15
playerpos =  "A16"
walls = ['V14', 'V15', 'V16', 'V17','A14', 'A18', 'B14', 'B18', 'C14', 'C16', 'C17', 'C18', 'C1', 'C2', 'C5', 'C6', 'C9',
         'C10', 'C11', 'D20', 'D7', 'D8', 'D13', 'D19', 'E20', 'E7', 'E8', 'E13', 'E19', 'E19', 'F20', 'F7', 'F8', 'F19', 'G20',
         'G7', 'G8', 'G13', 'G19', 'H20', 'H13', 'H12', 'H13', 'H14', 'H15', 'H16', 'H17', 'H18', 'H19', 'I20', 'I7', 'I8', 'I9', 'I10',
         'I11', 'I12', 'I13', 'I17', 'J20', 'J7', 'J11', 'J12', 'J13', 'J20', 'J17', 'J18' 'K20', 'K7', 'K11', 'K19', 'K20', 'L20', 'L7', 'L11', 'L19', 'M20',
         'M7', 'M8', 'M10', 'M11', 'M19', 'N20', 'N19', 'O20', 'O19', 'P20', 'P7', 'P8', 'P10', 'P11', 'P19', 'Q20', 'Q1', 'Q6', 'Q9',
         'Q11', 'Q19', 'R2', 'R3', 'R4', 'R5', 'R12', 'R13', 'R14', 'R15', 'R16', 'R17', 'R18', 'O12', 'N12', 'C3', 'C4']
end1 = ['B3', 'B4'] #ending cords

#Stage 2 walls and smallwalls
walls2 = ['A5', 'A6', 'A8', 'A9',' A10', 'A11', 'A12', 'A13', 'A17', 'A18', 'A19', 'B3', 'B4', 'B7', 'B12', 'B13', 'B14', 'B15',
          'B16', 'B20', 'C2', 'C20', 'D2', 'D20', 'E1', 'E13', 'E20', 'F1', 'F13', 'F20', 'G1', 'G20', 'H1', 'H16', 'H17', 'H18',
          'H20', 'I2', 'I4', 'I5', 'I20', 'I18', 'J2', 'J4', 'J5', 'J6', 'J7', 'J20', 'K2', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'K11',
          'K12', 'K13', 'K14', 'K19', 'K20', 'L2', 'L4', 'L5', 'L6', 'L19', 'L20', 'M1', 'M4', 'M5', 'M6', 'M9', 'M14', 'M20', 'N1',
          'N5', 'N9', 'N14', 'N19', 'N20', 'O1', 'O5', 'O9', 'O14', 'O19', 'O20', 'P2', 'P10', 'P11', 'P15', 'P19', 'P20', 'Q2',
          'Q10', 'Q16', 'Q20', 'R2', 'R20', 'S2', 'S3', 'S4', 'S9', 'S10', 'S16', 'S20', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11',
          'T15', 'T16', 'T17', 'T18', 'T19', 'T20', 'L3', 'O13', 'R16', 'M16', 'I15', 'O16']

smallwall = ['O13O12', 'N13N12', 'O12P12', 'M13M12', 'M12L12', 'M10L10', 'M8L8', 'O4P4', 'O7P7', 'O8P8',
             'P8Q8', 'O16N16', 'O17N17', 'O17N16', 'O18N18', 'L16L15', 'K16K15', 'K16J16', 'K17J17',
             'K17K18', 'L17L18', 'M8L7', 'K16J15', 'N18O17', 'Q8P7', 'O8P7', 'R5R4', 'P5P4', 'P4O3', 'Q9Q8', 'R9R8',
             'F4G3', 'F3G3', 'F2G2', 'F4G4', 'F5G5', 'F5F6', 'E6E5', 'D6E5', 'D5E5', 'D5D4', 'C5C4', 'E8D8', 'E9D9',
             'J15J16', 'J14J15', 'J12J13', 'D6E6', 'I13H13', 'I13I12', 'J12J13', 'J15J14', 'J16J15', 'G18G19', 'F19F18',
             'E18E19', 'D18E18', 'D17E17', 'D17D16', 'D15D16', 'C15C16', 'D14D13', 'D12E12', 'E10D10', 'D9D10',
             'C10C9', 'B9B10', 'D6E6', 'E12D12', 'G16G15', 'F15F16', 'H14I14', 'H15I15']

#movement
def down():
       knight.setheading(270)
       knight.forward(25)

def up():
       knight.setheading(90)
       knight.forward(25)

def right():
       knight.setheading(0)
       knight.forward(25)

def left():
       knight.setheading(180)
       knight.forward(25)
#movement check movement check movement check movement check movement check movement check 
valid = 0
playerposfordisplay = 0
def check():
       global valid
       global playerposfordisplay
       playerpos =  Ycord[yp] + Xcord[xp]
       playerposfordisplay = Ycord[yp] + Xcord[xp]
       if stagelevel == 1:
              if playerpos not in walls:
                     valid = True
              else:
                     valid = False
       elif stagelevel == 2:
              if playerpos not in walls2:
                     smallwallcheck = Ycord[yp] + Xcord[xp] + Ycord[previousyp] + Xcord[previousxp]
                     smallwallcheckreverse = Ycord[previousyp] + Xcord[previousxp] + Ycord[yp] + Xcord[xp]
                     print(smallwallcheck)
                     if smallwallcheck not in smallwall and smallwallcheckreverse not in smallwall: 
                            valid = True
                     else:
                            valid = False
              else:
                     valid = False

def encountercheck():
       print("")

#Fog of war encounter tiles:
#stage1
fogremove = ['C15', 'F13', 'H7', 'L9', 'N12', 'O12']
fogindex = ["Stage1fog1.gif", "stage1fog2.gif", "Stage1fog3.gif", "Stage1fog4.gif", "Stage1fog5.gif", "Stage1fog6.gif"]
st1fog = -1
st2fogs = 0
st2fogsindex = -1
fogremove2 = ['R10', 'L7', 'M11', 'R16', 'M16', 'I15', 'D19', 'C16', 'E15', 'G13', 'H13']
def fogchange():
       global st1fog
       global st2fogs
       global st2fogsindex
       playerpos =  Ycord[yp] + Xcord[xp]
       if stagelevel == 1:
              if playerpos in fogremove:
                     st1fog += 1
                     if 'O12' in fogremove or 'N12' in fogremove:
                            if playerpos == "O12" or playerpos == "N12":
                                   fogremove.remove('O12')
                                   fogremove.remove('N12')
                            else:
                                   fogremove.remove(playerpos)
                     else:
                            fogremove.remove(playerpos)
                     fogvariables[st1fog].hideturtle()
       elif stagelevel == 2:
              if playerpos in fogremove2:
                     st2fogs += 1
                     st2fogsindex += 1
                     if 'G13' in fogremove2 or 'H13' in fogremove2:
                            if playerpos == 'G13' or playerpos == 'H13' or playerpos == 'G14':
                                   fogremove2.remove('G13')
                                   fogremove2.remove('H13')
                                   fogvariablesstg2[st2fogsindex].hideturtle()
                                   fogvariablesstg2[(st2fogsindex + 1)].hideturtle()
                                   freemode()
                            else:
                                   fogremove2.remove(playerpos)
                                   fogvariablesstg2[st2fogsindex].hideturtle()
                                   freemode()
                     fogremove2.remove(playerpos)
                     fogvariablesstg2[st2fogsindex].hideturtle()
                     
                     #################

def stagecheck():
       global stagelevel
       global playerpos
       global yp
       global xp
       playerpos = Ycord[yp] + Xcord[xp]
       if stagelevel == 1:
              if playerpos in end1:
                     fogvariables[5].hideturtle()
                     fogvariables[6].hideturtle()
                     stagelevel += 1
                     playerpos = "T13"
                     yp = 19
                     xp = 12
                     knight.setx(63)
                     knight.sety(-235)
#Stage 1 object locations Stage 1 object locations Stage 1 object locations Stage 1 object locations 
table = ['E17', 'E16', 'E15', 'F16', 'F15', 'F17']
hallstatue = ['P4', 'P3', 'Q3', 'Q4']
bed = ['J8', 'J9']
chest1 = ['J10']
Ritualcircle = ['N15']
statuenearritual = ['I16', 'I15', 'I14', 'J15', 'J16', 'J14', 'K16', 'K15', 'K14']
encountertiles = ['F13', 'H7']
door1 = ['O11', 'N11']
door2 = ['D3', 'D4']
door3 = ['R15', 'R16']
door4 = ['M15', 'M16']
door5 = ['J15', 'I15']
table2 = ['R6', 'R7']
room1 = ['N11', 'N10']
chest = ['J10']
chest1 = ['M19', 'M18', 'N18']
bigchest = ['C7', 'C6', 'C8']
chest3 = ['E12']
chest4 = ['J10']
chest5 = ['B19']
def interaction(objecttointeract):
       return objecttointeract
def interactiveobjects():
       global playerposfordisplay
       global interaction
       if stagelevel == 1:
              if playerposfordisplay in table or playerposfordisplay in hallstatue or playerposfordisplay in bed or playerposfordisplay in chest or playerposfordisplay in Ritualcircle or playerposfordisplay in statuenearritual or playerposfordisplay in door1 or playerposfordisplay in door2:
                     return True
                     interaction = True
       if stagelevel == 2:
              if playerposfordisplay in door3 or playerposfordisplay in door5 or playerposfordisplay in door4 or playerposfordisplay in table2 or playerposfordisplay in room1 or playerposfordisplay in chest1 or playerposfordisplay in bigchest or playerposfordisplay in chest3 or playerposfordisplay in chest4 or playerposfordisplay in chest5:
                     return True
                     interaction = True
appless = 1
def gargoylestatue():
       global appless
       global inventory
       if appless == 1:
              time.sleep(1.5)
              writeup("Wait... I found something!", 0.02)
              time.sleep(1.5)
              print("")
              print("Picked up Key!")
              inventory.append("Key")
              appless = 0
def responseinteraction():
       global interaction
       if stagelevel == 1:
              if interactiveobjects() == True:
                     os.system('cls')
                     os.system("mode con cols=75 lines=25")
                     print("You: ")
                     if playerposfordisplay in table:
                            writeup("""My companions and I had a feast here... I wonder
where they are right now...""", 0.03)
                            print("")
                     if playerposfordisplay in hallstatue:
                            writeup("""The statue of a great warrior, he fought off the black skulls
himself back in the days. Now that he's dead, the black skulls came back. Maybe i'll
have my own statue!""", 0.03)
                            print("")
                     if playerposfordisplay in bed:
                            writeup("""Now is not the time for sleeping!""", 0.03)
                            print("")
                     if playerposfordisplay in Ritualcircle:
                            writeup("""I've never seen a ritual here... what was this for?""", 0.03)
                            print("")
                     if playerposfordisplay in chest:
                            writeup("""There is some loot in here!""", 0.03)
                            print("")
                            time.sleep(2)
                            print("Picked up Key!")
                            print("Picked up Iron Helm!")
                            print("Picked up Potion!")
                            inventory.append("Potion_of_health")
                            inventory.append("Key")
                            inventory.append("IronHelm")
                            chest.remove('J10')
                     if playerposfordisplay in statuenearritual:
                            writeup("""Seems like a statue of a gargoyle, wonder where they
are today...""", 0.03)
                            gargoylestatue()
                     if playerposfordisplay in chest1:
                            writeup("""There is some loot in here!""", 0.03)
                            print("")
                            time.sleep(1)
                            print("Picked up Key!")
                            print("Picked up Iron Helm!")
                            print("Picked up Potion!")
                            inventory.append("Potion_of_health")
                            inventory.append("Key")
                            inventory.append("IronHelm")
                            chest1.remove('J10')
                     if playerpos in door1:
                            writeup("This door is locked!", 0.03)
                            print("")
                            if "Key" in inventory:
                                   writeup("""Use key? ['f']
Leave ['e']""", 0.04)
                                   print("")
                                   choicess = input()
                                   if choicess == "f":
                                          walls.remove('O12')
                                          walls.remove('N12')
                                          door1.remove('011')
                                          door1.remove('N11')
                                          os.system('cls')
                                          os.system("mode con cols=75 lines=25")
                                          writeup("Door unlocked!", 0.04)
                                          inventory.remove("Key")
                                   else:
                                          freemode()
                     if playerpos in door2:
                            writeup("This door is locked!", 0.03)
                            print("")
                            if 'O12' not in walls:                                   
                                   if "Key" in inventory:
                                          writeup("""Use key? ['f']
Leave ['e']""", 0.04)
                                          print("")
                                          choicess= input()
                                          if choicess == "f":
                                                 walls.remove('C3')
                                                 walls.remove('C4')
                                                 door2.remove('D3')
                                                 door2.remove('D4')
                                                 os.system('cls')
                                                 os.system("mode con cols=75 lines=25")
                                                 writeup("Door unlocked!", 0.04)
                                                 inventory.remove("Key")
                                          else:
                                                 freemode()

                     print("")
                     print("Continue ['e']")
                     continuefrominteraction = input(": ")
                     freemode()
       if stagelevel == 2:
              if interactiveobjects() == True:
                      if playerpos in door3:
                            writeup("This door is locked!", 0.03)
                            print("")
                            if 'O12' not in walls:                                   
                                   if "Key" in inventory:
                                          writeup("""Use key? ['f']
Leave ['e']""", 0.04)
                                          print("")
                                          choicess= input()
                                          if choicess == "f":
                                                 walls2.remove('R16')
                                                 walls2.remove('O16')
                                                 door3.remove('R15')
                                                 door3.remove('R16')
                                                 os.system('cls')
                                                 os.system("mode con cols=75 lines=25")
                                                 writeup("Door unlocked!", 0.04)
                                                 print("")
                                                 writeup("""You found a silver key!""", 0.02)
                                          else:
                                                 freemode()
                      if playerpos in door4:
                            writeup("This door is locked!", 0.03)
                            print("")
                            if 'R16' not in walls2:                                   
                                   if "Key" in inventory:
                                          writeup("""Use key? ['f']
Leave ['e']""", 0.04)
                                          print("")
                                          choicess= input()
                                          if choicess == "f":
                                                 walls2.remove('M16')
                                                 door4.remove('M15')
                                                 door4.remove('M16')
                                                 os.system('cls')
                                                 os.system("mode con cols=75 lines=25")
                                                 os.system("mode con cols=75 lines=25")
                                                 writeup("Door unlocked!", 0.04)
                                                 print("")
                                                 writeup("""You see that this room contains
some loot, you also spot a special key!""", 0.02)
                                                 print("")
                                                 time.sleep(1)
                                                 print("Picked up Golden key!")
                                                 print("")
                                                 freemode()
                                          else:
                                                 freemode()
                            writeup("You need a silver key!", 0.03)
                            print("")
                      if playerpos in door5:
                             if 'M16' not in walls2:
                                   writeup("This door is locked!", 0.03)
                                   print("")                                 
                                   if "Key" in inventory:
                                          writeup("""Use key? ['f']
 Leave ['e']""", 0.04)
                                          print("")
                                          choicess= input()
                                          if choicess == "f":
                                                 walls2.remove('I15')
                                                 door5.remove('J15')
                                                 door5.remove('I15')
                                                 os.system('cls')
                                                 os.system("mode con cols=75 lines=25")
                                                 writeup("Door unlocked!", 0.04)
                                                 print("")
                                                 inventory.remove("Key")
                                                 print("continue ['e']")
                                                 aefrterwdes = input()
                                                 freemode()
                                          else:
                                                 freemode()
                             writeup("This door is locked! Requires a golden key!", 0.03)
                             print("")
                      if playerpos in table2:
                            writeup("""There is some loot in here!""", 0.03)
                            print("")
                            time.sleep(1)
                            print("Picked up IronBow!")
                            print("Picked up Potion!")
                            print("Picked up Potion!")
                            inventory.append("Potion_of_health")
                            inventory.append("Potion_of_health")
                            inventory.append("IronBow")
                            table2.remove('R6')
                            table2.remove('R7')
                      if playerpos in room1:
                            writeup("""There is a key and some loot
in thie room! maybe this key will
unlock the door by the entrance!""", 0.03)
                            print("")
                            time.sleep(1)
                            print("Picked up Key")
                            print("Picked up Potion!")
                            print("Picked up Potion!")
                            inventory.append("Potion_of_health")
                            inventory.append("Potion_of_health")
                            inventory.append("Key")
                            room1.remove("N11")
                            room1.remove("N10")
                      if playerpos in chest1:
                            writeup("""There is some loot in here!""", 0.03)
                            print("")
                            time.sleep(1)
                            print("Picked up DragonHelm!")
                            print("Picked up Potion!")
                            print("Picked up Potion!")
                            inventory.append("Potion_of_health")
                            inventory.append("Potion_of_health")
                            inventory.append("DragonHelm")
                            chest1.remove('M19')
                            chest1.remove('M18')
                            chest1.remove('N18')
                      if playerpos in bigchest:
                            writeup("""There is some loot in here!""", 0.03)
                            print("")
                            time.sleep(1)
                            print("Picked up Warwand!")
                            print("Picked up Firescroll!")
                            print("Picked up Potion!")
                            print("Picked up Potion!")
                            inventory.append("Potion_of_health")
                            inventory.append("Potion_of_health")
                            inventory.append("Firescroll")
                            inventory.append("Warwand")
                            bigchest.remove('C6')
                            bigchest.remove('C7')
                            bigchest.remove('C8')
                      if playerpos in chest3:
                            writeup("""There is some loot in here!""", 0.03)
                            print("")
                            time.sleep(1)
                            print("Picked up Firebow!")
                            print("Picked up Potion!")
                            inventory.append("Potion_of_health")
                            inventory.append("Firebow")
                            chest3.remove('E12')
                      if playerpos in chest4:
                            writeup("""There is some loot in here!""", 0.03)
                            print("")
                            time.sleep(1)
                            print("Picked up DragonSword!")
                            print("Picked up Potion!")
                            inventory.append("Potion_of_health")
                            inventory.append("DragonSword")
                            chest4.remove('J10')
                      if playerpos in chest5:
                            writeup("""There is some loot in here!""", 0.03)
                            print("")
                            time.sleep(1)
                            print("Picked up EnchantedWand!")
                            print("Picked up Potion!")
                            inventory.append("Potion_of_health")
                            inventory.append("EnchantedWand")
                            chest5.remove("B19")
                      print("")
                      print("Continue ['e']")
                      continuefrominteraction = input(": ")
                      freemode()
encountertiles2 = ['G13', 'H13', 'F9']
randomencounters = 0
def encounterresponse():
       global randomencounters
       global encountertiles
       global encountertiles2
       global stagelevel
       if stagelevel == 1:
              if playerpos in encountertiles:
                     os.system('cls')
                     os.system("mode con cols=75 lines=25")
                     if playerpos == 'F13':
                            writeup("""There were many happy townspeople here, now
it just feels empty...""", 0.03)
                            time.sleep(1)
                            writeup(""" wait... I hear noises....""", 0.04)
                            encountertiles.remove('F13')
                            fight("Blackskull knight", 50, 25, 0.1, "Face my wrath!", "idk", inventory, "blackknight.gif")
                     if playerpos == 'H7':
                            writeup("Oh my goodness! Blackskulls are everywhere!", 0.03)
                            time.sleep(0.05)
                            print("")
                            print("(Beyond this point you will encounter random enemies at random times)")
                            encountertiles.remove('H7')
                            randomencounters += 1
              print("Continue ['e']")
              continuefrominteraction = input()
              fight("BlackSkull Warrior", 80, 30, 0.2, "I will devour your corpse!", "dafuq", inventory, "blackwarrior.gif")
              freemode()
       if stagelevel == 2:
              if playerpos in encountertiles2:
                     os.system('cls')
                     os.system("mode con cols=75 lines=25")
                     if playerpos == 'G13' or playerpos == 'H13':
                            writeup("""There is the boss, sitting on that chair...
(When you feel ready, you can fight the boss by sitting
in the chair, or you could loot around and prepare""", 0.02)
                            encountertiles2.remove('G13')
                            encountertiles2.remove('H13')
                            print("Continue ['e']")
                            continuefrominteraction = input()
                     if playerpos == 'F9':
                            writeup("""Im gonna sit here and....
(The leader of the blackskulls gets up)
Blackskull leader: "I will annihlate you!""", 0.04)
                            print("")
                            writeup("""(The Blackskull Leader
is known for resurrecting itself after death)...""", 0.03)
                            print("")
                            print("Continue ['e']")
                            stuffff = input()
                            fight("Blackskull Leader", 500, 55, 0.1, "You will become mush!", "idk", inventory, "blackleader.gif")
#Idk this is just my troll way of ending a game that complete its purpose
#The main focus of this project was to create a working combat system, a
#Working inventoy/equipment/blackorb during movement system and a movement system on a given grid.

#Encounters Encounters Encounters Encounters Encounters Encounters Encounters 
def encountercheck():
       global encountertiles
       global encountertiles2
       if stagelevel == 1:
              if playerpos in encountertiles:
                     encounterresponse()
       elif stagelevel == 2:
              if playerpos in encountertiles2:
                     encounterresponse()

def randomencounter():
       global randomencounters
       if randomencounters == 1:
              if stagelevel == 1:
                     chancetile = random.randint(1,10)
                     mobtype = random.randint(1,5)
                     if chancetile < 2:
                            if mobtype == 1:
                                   fight("Black Knight", 50, 35, 0.1, "Get over here!!!", "meh", inventory, "blackknight.gif")
                            if mobtype == 2:
                                   fight("Black Skull Tank", 125, 25, 0.1, "Grrrr", "vdgdr", inventory, "blacktank.gif")
                            if mobtype == 3:
                                   fight("Black Skull Archer", 35, 60, 0.1, "Time for some more target practice!", "lol", inventory, "blackarcher.gif")
                            if mobtype == 4:
                                   fight("Black Skull Assassin", 30, 80, 0.1, "I will silence you", "hmph", inventory, "blackassassin.gif")
                            if mobtype == 5:
                                   fight("Black Knight", 50, 35, 0.1, "Get over here!!!", "meh", inventory, "blackknight.gif")
              if stagelevel == 2:
                     chancetile = random.randint(1,10)
                     mobtype = random.randint(1,5)
                     if chancetile < 2:
                            if mobtype == 1:
                                   fight("Black Warrior", 100, 55, 0.1, "Good think i sharpened my axe!!!", "meh", inventory, "blackwarrior.gif")
                            if mobtype == 2:
                                   fight("Black Skull Beserker", 150, 45, 0.1, "I lust blood", "vdgdr", inventory, "blackbeserker.gif")
                            if mobtype == 3:
                                   fight("Black Skull Sniper", 50, 90, 0.1, "Sigh another guy's head to splatter!", "lol", inventory, "blacksniper.gif")
                            if mobtype == 4:
                                   fight("Black Skull Suicider", 35, 110, 0.1, "Hahahahahaha", "hmph", inventory, "blacksuicider.gif")
                            if mobtype == 5:
                                   fight("Black Warrior", 100, 55, 0.1, "Good think i sharpened my axe!!!", "meh", inventory, "blackwarrior.gif")

#Input for movement
previousyp = 0 #For stage 2 smallwall check
previousxp = 0
def interactiondetails():
       os.system('cls')
       os.system("mode con cols=75 lines=25")
       global playerposfordisplay
       inventorydisplay()
       print("======================")
       print("[Move Up] ['w']")
       print("[Move Down] ['s']")
       print("[Move Right] ['d']")
       print("[Move Left] ['a']")
       print("======================")
       print("[Equipment] ['i']")
       print("[Inventory] ['o']")
       if interactiveobjects() == True:
              print("[Interact] ['e']")
       print("======================")
       print("Position = " + str(playerpos))
       print("Hp = " + str(Playerhealth))
       print("Base Atk = " + str(Playerdamage))
       print("Base Def = " + str(Playerdefense))
       print("BlackOrbs = " + str(Blackorbs) + "/30 ['b']")
       print("======================")
       
                       
def freemode():
       interactiondetails()
       global previousyp
       global previousxp
       global yp
       global xp
       encounter = "false"
       move1 = input()
       while encounter == "false":
              if move1 == "w":
                     previousyp = yp
                     yp += -1
                     check()
                     if valid == True:
                            up()
                     else:
                            yp += 1
                            print("cannot go that way")
                     fogchange()
              elif move1 == "s":
                     previousyp = yp
                     yp += 1
                     check()
                     if valid == True:
                            down()
                     else:
                            yp += -1
                            print("cannot go that way")
                     fogchange()
              elif move1 == "a":
                     previousxp = xp
                     xp += -1
                     check()
                     if valid == True:
                            left()
                     else:
                            xp += 1
                            print("cannot go that way")
                     fogchange()
              elif move1 == "d":
                     previousxp = xp
                     xp += 1
                     check()
                     if valid == True:
                            right()
                     else:
                            xp += -1
                            print("cannot go that way")
                     fogchange()
              elif move1 == "e":
                     responseinteraction()
              elif move1 == "i":
                     equipmentnavigation()
              elif move1 == "o":
                     inventorynavigation()
              elif move1 == "b":
                     blackorbnavi()
              stagecheck()
              randomencounter()
              previousxp = xp
              previousyp = yp
              encountercheck()
              interactiondetails()
              move1 = input()

#Item drops Item drops Item drops Item drops Item drops Item drops Item drops Item drops Item drops Item drops Item drops Item drops Item drops Item drops Item drops

def drops():
       print("")
       global Blackorbs
       blackorbnum = random.randint(1,10)
       ifitemwilldrop = random.randint(1, 10)
       itemdrop = random.randint(1,3)
       ifgooditemwilldrop = random.randint(1, 10)
       gooditem = random.randint(1,10)
       Blackorbs += blackorbnum
       writeup("You found " + str(blackorbnum) + " black orbs!", 0.02)
       if ifitemwilldrop >= 5:
              print("")
              if itemdrop == 1:
                     inventory.append("Potion_of_health")
                     writeup("You found Potion!", 0.02)
              elif itemdrop == 2:
                     inventory.append("Firescroll")
                     writeup("You found a firescroll!", 0.02)
              elif itemdrop == 3:
                     inventory.append("Essence_of_attack")
                     writeup("You found an essence of attack!", 0.02)
       if ifgooditemwilldrop < 2:
              print("")
              if gooditem < 2:
                     inventory.append("DragonChestplate")
                     writeup("You found a dragon-scaled chestplate! Wow!", 0.02)
              else:
                     inventory.append("IronChestplate")
                     writeup("You found an iron chestplate!", 0.02)
       


#Fight sequence and enemies Fight sequence and enemies Fight sequence and enemies Fight sequence and enemies Fight sequence and enemies Fight sequence and enemies Fight sequence and enemies Fight sequence and enemies
"""The combat system is not talked about in the actualy code and it must be adapted and
learned by the players. HOwever, just for the sake of explaining the fight stuff, essentially
you can basic attack, power attack, perform an ultimate, run, block or use items. The power
attack has charges where 1 is used up when it is used, and can only be restored by performing
basic attacks and blocks. Ultimates can be charged with power attacks, basic attacks and blocks, and at 4 charges,
you can use the ultimate attack and unleash a quadruple damage range attack. Everything
else should be self explanatory"""

def healthcheck(mobhealth, mobname):
       if Playerhealth < 1:
              os.system('cls')
              os.system("mode con cols=75 lines=25")
              writeup("""O no! You have died!""", 0.04)
              time.sleep(0.1)
              print("")
              writeup("Restart? ['e']")
              lollmao = input()
              startingscreen(screen)
       elif mobhealth < 1:
              os.system('cls')
              os.system("mode con cols=75 lines=25")
              writeup("You have slain " + str(mobname) + "!", 0.04)
              drops()
              mobimage.hideturtle()
              print("")
              print("continue? ['e']")
              noice = input()
              inventoryremovecheck()
              os.system('cls')
              os.system("mode con cols=75 lines=25")
              freemode()
              

def fightsequencedamagetaken(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory, block, successdodge, dodgechance, run, runsuccess, runchance, dodge):
       global Playerhealth
       os.system('cls')
       os.system("mode con cols=75 lines=25")
       round(mobdamage, 0)
       damagetaken = random.randint(round((mobdamage / 2)), (mobdamage))
       fulldamage = damagetaken - (damagetaken * Playerdefense)
       if dodge == 1:
              if successdodge == 1:
                     writeup("You successfully dodged " + str(mobname) + "''s attack!", 0.02)
                     print("")
                     writeup("You dodged from " + str(fulldamage) + " points of damage!", 0.02)
                     print("")
                     print("continue ['e']")
                     cool = input()
                     dodge = 0
                     fightinterface(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory, powerattack, ultimate)
              else:
                     writeup("Dodge failed!", 0.04)
                     print("continue ['e']")
                     cool = input()
       if run == 1:
              if runsuccess == 1:
                     writeup("Run sucess! You ran away from the fight!", 0.02)
                     print("")
                     print("Continue ['e']")
                     cool = input()
                     inventoryremovecheck()
                     freemode()
              else:
                     writeup("Run failed!", 0.02)
                     print("")
                     print("")
                     print("continue ['e']")
                     cool = input()
       if block == 1:
              blockamount = random.randint(1, 5)
              blockamount = blockamount / 10
              fulldamage = fulldamage * blockamount
              writeup("You negated %" + str((100 - (blockamount * 100))) + " of damage", 0.03)
              print("")
       Playerhealth = Playerhealth - fulldamage
       writeup("You have taken " + str(fulldamage) + " points of damage!", 0.02)
       print("")
       writeup(str(name) + ": " + str(Playerhealth) + "hp", 0.02)
       print("")
       writeup("You armor blocked " + str(damagetaken * Playerdefense) + " points of damage!", 0.02)
       print("")
       print("Continue ['e']")
       cool = input()
       healthcheck(mobhealth, mobname)
       fightinterface(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory)
       
                     
def fightsequence(action, mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory):
       global Playerhealth
       global powerattack
       global ultimate
       block = 0
       dodge = 0
       dodgechance = 0
       successdodge = 0
       run = 0
       runsuccess = 0
       runchance = 0
       print("=============================")
       round(Playerdamage)
       if (len(action)) > 1:
              print("Please input a valid action")
              print("Continue ['e']")
              continuefrominteraction = input()
              fightinterface(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory)
       elif action in alphabet:
              print("Please input a valid action")
              print("Continue ['e']")
              continuefrominteraction = input()
              fightinterface(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory)
       elif int(action) == 1:
              damagedone = random.randint(round(Playerdamage / 2), Playerdamage)
              mobhealth = mobhealth - damagedone
              writeup("You performed a basic attack!", 0.02)
              print("")
              time.sleep(1)
              writeup("You have dealt " + str(damagedone) + " damage points to " + str(mobname), 0.02)
              print("")
              writeup(str(mobname) + " health: " + str(mobhealth), 0.02)
              print("")
              if powerattack < 2:
                     powerattack += 1
              if ultimate < 4:
                     ultimate += 1
              print("Continue ['e']")
              continuefrominteraction = input()   
              healthcheck(mobhealth, mobname)
              fightsequencedamagetaken(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory, block, successdodge, dodgechance, run, runsuccess, runchance, dodge)

       elif int(action) == 2:
              if powerattack > 0:
                     damagedone = random.randint((round((Playerdamage * 1.5) / 2)), (round(Playerdamage * 1.5)))
                     mobhealth = mobhealth - damagedone
                     writeup("You performed a power attack! (Damage multiplier 1.5)", 0.02)
                     print("")
                     time.sleep(1)
                     writeup("You have dealt " + str(damagedone) + " damage points to " + str(mobname), 0.02)
                     print("")
                     writeup(str(mobname) + " health: " + str(mobhealth), 0.04)
                     print("")
                     if ultimate < 4:
                            ultimate += 1
                     powerattack = powerattack - 1
                     print("Continue ['e']")
                     continuefrominteraction = input()   
                     healthcheck(mobhealth, mobname)
                     fightsequencedamagetaken(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory, block, successdodge, dodgechance, run, runsuccess, runchance, dodge)
              else:
                     writeup("Not enought charges!", 0.04)
                     print("")
                     print("Continue ['e']")
                     continuefrominteraction = input()
                     fightinterface(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory)
       elif int(action) == 3:
              if ultimate == 4:
                     damagedone = random.randint((round((Playerdamage * 4) / 2)), (Playerdamage * 4))
                     mobhealth = mobhealth - damagedone
                     ultimate = 0
                     writeup("You performed an ultimate attack! [Quadruple damage range]", 0.02)
                     print("")
                     writeup("You have dealt " + str(damagedone) + " damage points to " + str(mobname), 0.02)
                     print("")
                     writeup(str(mobname) + " health: " + str(mobhealth), 0.04)
                     print("")
                     print("Continue ['e']")
                     continuefrominteraction = input()   
                     healthcheck(mobhealth, mobname)
                     fightsequencedamagetaken(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory, block, successdodge, dodgechance, run, runsuccess, runchance, dodge)
              else:
                     writeup("Ultimate not ready!", 0.02)
                     print("")
                     print("Continue ['e']")
                     continuefrominteraction = input()
                     fightoptions(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory)
       elif int(action) == 4:
              block = 1
              if powerattack < 2:
                     powerattack += 1
              if ultimate < 4:
                     ultimate += 1
              fightsequencedamagetaken(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory, block, successdodge, dodgechance, run, runsuccess, runchance, dodge)
       elif int(action) == 5:
              dodgechance = random.randint(0, 100)
              dodge = 1
              if dodgechance < 30:
                     successdodge = 1
              fightsequencedamagetaken(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory, block, successdodge, dodgechance, run, runsuccess, runchance, dodge)
       elif int(action) == 6:
              run = 1
              runchance = random.randint(0, 100)
              if runchance < 30:
                     runsuccess = 1
              fightsequencedamagetaken(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory, block, successdodge, dodgechance, run, runsuccess, runchance, dodge)
       elif int(action) == 7:
              if "Potion_of_health" in inventory:
                     print("You healed 30 health points!")
                     Playerhealth += 30
                     inventory.remove("Potion_of_health")
                     print("")
                     print("Continue ['e']")
                     continuefrominteraction = input()
                     fightinterface(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory)
       elif int(action) == 8:
              if "Firescroll" in inventory:
                     mobhealth = mobhealth - 65
                     print("You summoned a firescroll!")
                     print("You dealt 65 damage!")
                     print("")
                     print("Continue ['e']")
                     inventory.remove("Firescroll")
                     continuefrominteraction = input()
                     healthcheck(mobhealth, mobname)
                     fightsequencedamagetaken(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory, block, successdodge, dodgechance, run, runsuccess, runchance, dodge)
       print("Please input a valid action")
       print("Continue ['e']")
       continuefrominteraction = input()
       fightinterface(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory)
              
def fightoptions(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory):
       global powerattack
       global ultimate
       print("[1] - Basic Attack")
       print("[2] - Power Attack [" + str(powerattack) + "/2 charges]")
       print("[3] - Ultimate [" + str(ultimate) + "/4] Power")
       print("[4] - Block")
       print("[5] - Dodge [30% Chance]")
       print("[6] - Run [30 % Chance]")
       if "Potion_of_health" in inventory:
              print("[7] Use Potion")
       if "Firescroll" in inventory:
              print("[8] Use Firescroll")
       fightsequence(input(), mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory)
def fightinterface(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory):
       global ultimate
       os.system('cls')
       os.system("mode con cols=75 lines=25")
       print("===========================")
       print(str(mobname) + ": " + str(mobquote))
       print("===========================")
       print(str(name) + ":")
       print("Health = " + str(Playerhealth))
       print("Damage = " + str(Playerdamage / 2) + "-" + str(Playerdamage))
       print("Defense = " + str(Playerdefense))
       print("===========================")
       print(str(mobname) + ":")
       print("Health = " + str(mobhealth))
       print("Damage = " + str(mobdamage / 2) + "-" + str(mobdamage))
       print("Defense = " + str(mobdefense))
       print("===========================")
       fightoptions(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory)

mobimage = turtle.Turtle()
mobimage.hideturtle()
def fight(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory, imagelol):
       global name
       global Playerhealth
       global Playerdamage
       global Playerdefense
       screen.addshape(imagelol)
       mobimage.shape(imagelol)
       mobimage.showturtle()
       inventorycheck()
       os.system("cls")
       writeup("You have encountered " + str(mobname), 0.04)
       print("")
       print("Continue ['e']")
       continuefrominteraction = input()
       fightinterface(mobname, mobhealth, mobdamage, mobdefense, mobquote, mobpassive, inventory)
       
       



       
       

#Game sequence
def Stage1introduction():
       os.system('cls')
       os.system("mode con cols=75 lines=25")
       writeup("...", 1)
       time.sleep(2)
       os.system('cls')
       os.system("mode con cols=75 lines=25")
       writeup("Unknown: "+ str(name) + ", wake up!", 0.04)
       time.sleep(1)
       os.system('cls')
       os.system("mode con cols=75 lines=25")
       writeup("""You regain consciousness and see a dwarf with a
large beard while feeling acute pain in your head""", 0.02)
       screen.addshape("Dwarf.gif")
       temp1 = turtle.Turtle()
       temp1.shape("Dwarf.gif")
       time.sleep(2)
       print("")
       writeup(str(name) + ": Ow... what happened?", 0.04)
       print("")
       print("Continue ['e']")
       idk = input(": ")
       writeup("""Dwarf Guy: The Black Skulls is invading this town! They are causing chaos
in the streets and you were knocked out by one of them, presumed dead!""", 0.02)
       print("")
       print("Continue ['e']")
       idk = input(": ")
       os.system('cls')
       os.system("mode con cols=75 lines=25")
       writeup(str(name) + ": well, seems like I gotta kill them and destroy the Black Skulls!", 0.04)
       time.sleep(2)
       print("")
       writeup("""Dwarff Guy: Here is some basic gear that should get you started... dont forget
to loot any area that looks like it could have
some loot. Good luck!""", 0.04)
       time.sleep(2)
       print("")
       temp1.hideturtle()
       
              
startingscreen(screen)
introduction()
classtype(screen)
Stage1introduction()
freemode()
turtle.done()




       


       




