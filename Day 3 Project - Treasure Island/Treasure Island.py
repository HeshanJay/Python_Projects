print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

q1 = input('''You're at a cross road. Where do you want to go? 
Type "left" or "right" ''')
if q1 == "left" or q1 == "Left":
    q2 = input('''You have come to a lake. There is an island in the middle of the lake. 
    Type "wait" to wait for a boat. Type "swim" to swim across the lake ''')
    if q2 == "wait" or "Wait":
        q3 = input('''You have arrived on the island, standing before multiple doors, 
        each distinguished by a different color. To succeed and complete the challenge, 
        you must choose and open the correct door.
        Type "red" to select the door in red.
        Type "blue" to select the door in blue.
        Type "yellow" to select the door in yellow. ''')
        if q3 == "yellow" or "Yellow":
            print("Congratulations!. You have found the treasure!!!")
        elif q3 == "red" or "Red":
            print("You have burned by fire. Game Over!")
        elif q3 == "blue" or "Blue":
            print("you have eaten by beasts. Game Over!")
        else:
            print("Game Over!")
    else:
        print("You have attacked by trout. Game Over!")

else:
    print("You have fallen to a hole. Game Over!")