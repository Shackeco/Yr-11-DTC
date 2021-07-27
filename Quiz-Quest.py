import random
import keyboard
print("Welcome to the league of legends quiz")
while True:
    enter_choice = input('Enter Y to play or N to exit\n')
    if enter_choice == 'y':
        print("Have Fun!")
        break
    if enter_choice == 'n':
        print('Goodbye!')
        exit()


def all_questions(question, correct_ans, ans):
    while True:
        print(question)
        random.shuffle(ans)
        print(ans)
        response = input("What's your answer \n")   
        if response == correct_ans:
            print('Congrats, You got it right')
            return True
        else:
            print('You failed, Try the next question')
            return False
            
q1 = all_questions('Who is the Iron Revenant?', 'Mordekaiser', ['Mordekaiser', 'Garen', 'Kayn', 'Fiora'])
q2 = all_questions('What race is Rakan & Xayah?', 'Vastayan', ['Vastayan', 'Trolls', 'Titans', 'Vastayashai"Rei'])
q3 = all_questions('Which one of these characters was transmuted?','Warwick',['Singed','Le Blanc','Gragas','Warwick'])
q4 = all_questions('What is kassadins ultimate?','A quick teleport',['He launches himself','A quick teleport','Devours the target','Suppresses an enemy'])
q5 = all_questions('Which nation is the strongest?','Demacia',['Freljord','Ionia','Noxus','Demacia'])
q6 = all_questions('Which one of these champions is strongest is the lore?','Ornn',['Ornn','Aurelion Sol','Karma','Bard'])
q7 = all_questions('Which one of these champions are sisters?','Kayle & Morgana',['Sejuani & Leona','Akali & Katarina','Kayle & Morgana','Illaoi & Tristana'])
q8 = all_questions('Which of these champions have a root ability?','Lux',['Galio','Teemo','Warwick','Lux'])
q9 = all_questions('Which of these champions are classed as a jungler?','Gragas',['Teemo','Darius','Gragas','Zed'])
q10 = all_questions('Which of these champions were a couple','Illaoi & Gangplank',['Warwick & Volibear','Lucian & Poppy','Illaoi & Gangplank','Mordekaiser & Taric'])
q11 = all_questions('','',['','','',''])
q12 = all_questions('','',['','','',''])
q13 = all_questions('','',['','','',''])
q14 = all_questions('','',['','','',''])
q15 = all_questions('','',['','','',''])