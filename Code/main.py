import time
import farm
import juwel
import chicken
import Club


def cooldown():
    print("Script startet in 5 sekunden")
    time.sleep(1)
    print("Script startet in 4 sekunden")
    time.sleep(1)
    print("Script startet in 3 sekunden")
    time.sleep(1)
    print("Script startet in 2 sekunden")
    time.sleep(1)
    print("Script startet in 1 sekunde")




print(r"""
 _____                                       _____ 
( ___ )                                     ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |       ___ ___  _______  _______       |   | 
 |   |      |   Y   ||   _   ||   _   |      |   | 
 |   |      |.  1   ||   |   ||   |   |      |   | 
 |   |      |.  _   | \___   | \___   |      |   | 
 |   |      |:  |   ||:  1   ||:  1   |      |   | 
 |   |      |::.|:. ||::.. . ||::.. . |      |   | 
 |   |      `--- ---'`-------'`-------'      |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                     (_____)
""")
print("1=Notruf Hamburg Kassenraub(Farm)")
print("2=Notruf Hamburg Kassenraub(Juwel)")
print("3=AFK(Chicken_Wing")
print("4=Nortuf Hamburg Club")
print("Mehre Bots werden noch kommen")
print ("Wähle eine Zahl")
choice = input()
if choice == "1":
 cooldown()
 farm.farm_function()

if choice == "2":
 cooldown()
 juwel.juwel_function()

if choice == "3":
 cooldown()
 chicken.chicken_wing()

if choice == "4":
 cooldown()
 Club.Club_function()
 
    