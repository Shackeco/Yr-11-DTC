#yuuuuuuuuuuuuuy
import keyboard
import random
# the actual question 
# Answer
# Wrong answers 


def all_questions(question, correct_ans, ans):
    while True:
        print(question)
        random.shuffle(ans)
        print(ans)
        response = input("Whats your answer")   
        try:
            response = int(response)
            if response == ans:
                print('Congrats, You got it right')
            else:
                print('You failed gg no re')
        except ValueError:
            print("Your answer needs to be between 1 and 4 and a whole number")

all_questions('what is the day today', 'friday', ['sat', 'sun', 'mon', 'friday'])



# print("Welcome to the league of legends quiz. \nPress Y to play, or press N to leave")
# while True:
#     try:
#         if keyboard.is_pressed('y'):
#             print("I Hope you enjoy the quiz ;)")
#             break
        
#         if keyboard.is_pressed('n'):
#             print("Ok, goodbye my lover")
#             exit()
#     except:
#         break
# quest1 = None 
# while quest1 != 1:
#     quest1 = input("Question 1, Who is the Iron Revenant\n\
#                 1 - Mordekaiser\
#                 2 - Tahm Kench \
#                 3 - Garen\
#                 4 - Kayn\n")
#     try:
#         quest1 = int(quest1)
#         if quest1 == 1:
#             print("Congrats, you got it right")
#             break
#         if quest1 < 1:
#             print("That was incorrect, please restart the quiz")
#             exit()
#         if quest1 > 1:
#             print("That was incorrect, please restart the quiz")
#             exit()
#     except:
#         ValueError()
#         print("Your answer needs to be between 1 and 4 and a whole number")

# while True:
#     quest2 = input("Question 2, Who's ultimate drags every enemy in, then fires a beam of lunar energy on them\n\
#                 1 - Yorick\
#                 2 - Kayle\
#                 3 - Diana\
#                 4 - Kled\n")
#     try:
#         quest2 = int(quest2)
#         if quest2 == 3:
#             print("Congrats, that was correct")
#             break
#         if quest2 < 3:
#             print("That was incorrect, please restart the quiz")
#             exit()
#         if quest2 > 3:
#             print("That was incorrect, please restart the quiz")
#             exit()
#     except:
#         ValueError()
#         print("Your guess needs to be a whole number between 1 and 4")
