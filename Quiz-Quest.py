import keyboard
import random

def all_questions(question, correct_ans, ans):
    while True:
        print(question)
        random.shuffle(ans)
        print(ans)
        response = input("Whats your answer \n")   
        try:
            response = str(response)
            if response == correct_ans:
                print('Congrats, You got it right')
                return True
            else:
                print('You failed gg no re')
                return False
        except:
            if response == int or float:
                print('Your answer needs to be one of the options')
                return False
            
q1 = all_questions('Who is the Iron Revenant', 'Mordekaiser', ['Mordekaiser', 'Garen', 'Kayn', 'Fiora'])
q2 = all_questions('What race is Rakan & Xayah', 'Vastayan', ['Vastayan', 'Trolls', 'Titans', 'Vastayashai"Rei'])