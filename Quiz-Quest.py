import random
score = 0
# Prints a welcome message
print("Welcome to the league of legends quiz")
# Asks the user if they want to play
while True:
    enter_choice = input('Enter Y to play or N to exit\n')
    if enter_choice == 'y' or 'Y':
        print("Have Fun!")
        break
    if enter_choice == 'n' or 'N':
        print('Goodbye!')
        exit()
# Contains the questions, correct answer and the other answers
def Questions_and_Answers(question, correct_ans, ans):
# Prints those questions and answers then ask the user for a response, if its right it congratulates them, if wrong it says gg no re
    global score
    while True:
        print(question)
        random.shuffle(ans)
        print(ans)
        response = input("What's your answer \n")   
        if response == correct_ans:
            print('Congrats, You got it right')
            score += 1
            print(f'Your current score is {score} out of 15')
            return True
        if response != ans:
            print('Your answer needs to be one of the options')
        else:
            print(f'You failed, your current score is still {score} out of 15.\nTry the next question')
            return False


# The questions and answers       
q1 = Questions_and_Answers('Who is the Iron Revenant?', 'Mordekaiser', ['Mordekaiser', 'Garen', 'Kayn', 'Fiora'])
q2 = Questions_and_Answers('What race is Rakan & Xayah?', 'Vastayan', ['Vastayan', 'Trolls', 'Titans', 'Vastayashai"Rei'])
q3 = Questions_and_Answers('Which one of these characters was transmuted?','Warwick',['Singed','Le Blanc','Gragas','Warwick'])
q4 = Questions_and_Answers('What is kassadins ultimate?','A quick teleport',['He launches himself','A quick teleport','Devours the target','Suppresses an enemy'])
q5 = Questions_and_Answers('Which nation is the strongest?','Demacia',['Freljord','Ionia','Noxus','Demacia'])
q6 = Questions_and_Answers('Which one of these champions is strongest is the lore?','Ornn',['Ornn','Aurelion Sol','Karma','Bard'])
q7 = Questions_and_Answers('Which one of these champions are sisters?','Kayle & Morgana',['Sejuani & Leona','Akali & Katarina','Kayle & Morgana','Illaoi & Tristana'])
q8 = Questions_and_Answers('Which of these champions have a root ability?','Lux',['Galio','Teemo','Warwick','Lux'])
q9 = Questions_and_Answers('Which of these champions are classed as a jungler?','Gragas',['Teemo','Renekton','Gragas','Zed'])
q10 = Questions_and_Answers('Which of these champions were a couple','Illaoi & Gangplank',['Warwick & Volibear','Lucian & Poppy','Illaoi & Gangplank','Mordekaiser & Taric'])
q11 = Questions_and_Answers('The ruined king is named Viego','true',['true','false'])
q12 = Questions_and_Answers("Kayle's ultimate is called Devine Punishment",'false',['false','true'])
q13 = Questions_and_Answers('','',['','','',''])
q14 = Questions_and_Answers('','',['','','',''])
q15 = Questions_and_Answers('','',['','','',''])














#   while True:
 #       if score == 1 or 2 or 3:
  #          print(f"Congratulations, you got a whopping score of {score}, you are worse than a 3 year old child guessing.")
   #     if score == 4 or 5 or 6:
    #        print(f"Congratulations, you got a whopping score of {score}, you are worse than a 6 year old child with parkinsons trying to aim a squirt gun.")
     #   if score == 7 or 8 or 9:
      #      print(f"Congratulations, you got a whopping score of {score}, you are worse than a 9 year old child trying to bake a cake on their own.")
       # if score == 10 or 11 or 12:
        #    print(f"Congratulations, you got a whopping score of {score}, you are worse than a 12 year old trying to cheat on his math quiz.")
        #if score == 13 or 14 or 15:
         #   print(f"Congratulations, you got a whopping score of {score}, you have utterly too much time on your hands and should probably get help.")