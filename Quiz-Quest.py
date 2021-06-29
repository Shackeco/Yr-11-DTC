#yuuuuuuuuuuuuu
import keyboard
print("Welcome to the league of legends quiz. \nPress Y to play, or press N to leave")
while True:
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

if quest1 == 1:
    print("Congrats, you got it right")
    else:
    print("Incorrect, you fail, please restart the quiz")
