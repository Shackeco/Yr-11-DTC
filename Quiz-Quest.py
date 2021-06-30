#yuuuuuuuuuuuuu
import keyboard
print("Welcome to the league of legends quiz. \nPress Y to play, or press N to leave")
while not True:
    try:
        if keyboard.is_pressed('y'):
            print("I Hope you enjoy the quiz ;)")
            break
        
        if keyboard.is_pressed('n'):
            print("Ok, goodbye my lover")
            exit()
    except:
        break

quest1 = input("Question 1, Who is the Iron Revenant\n\
    1 - Mordekaiser\
    2 - Tahm Kench \
    3 - Garen\
    4 - Kayn\n")
while not True:
    try:
        if quest1 == 1:
            print("Congrats, you got it right")
            break
        if quest1 != 1:
            print("That was incorrect, please restart the quiz")
            exit()

quest2 = input("Question 2, Who's ultimate sucks every enemy in, then fires a beam of moon light on them\n\
    1 - Yorick\
    2 - Kayle\
    3 - Diana\
    4 - Kled\n")
while not True:
    try:
        if quest2 == 3:
            print("Congrats, that was correct")
            break
        if quest2 != 3:
            print("That was incorrect, please restart the quiz")
            exit()
