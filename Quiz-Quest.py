import random
score = 0
# Prints a welcome message
print("Welcome to the league of legends quiz")
# Asks the user if they want to play
while True:
    enter_choice = input('Enter Yes to play or No to exit\n')
    enter_choice = enter_choice.capitalize()
    if enter_choice == 'Yes':
        print("Have Fun!")
        break
    if enter_choice == 'No':
        print('Goodbye!')
        exit()
# Contains the questions, correct answer and the other answers
def Questions_and_Answers(question, correct_ans, ans):
# Prints those questions and answers then ask the user for a response, 
# if it's right it congratulates them and adds to score, if wrong it says that they are wrong
    global score
    while True:
        print(question)
        random.shuffle(ans)
        print(ans)
        response = input("Enter an answer from the options \n")
        response = response.capitalize()
        if response == correct_ans:
            print('Congrats, You got it right')
            score += 1
            print(f'Your current score is {score} out of 15')
            return True
        if response not in ans:
            print("Your answer needs to be one of the options")
        else:
            print(f'You failed, your current score is {score} out of 15.\nTry the next question')
            return False

# The questions and answers       
q1 = Questions_and_Answers('Who is the Iron Revenant?', 'Mordekaiser', ['Mordekaiser', 'Garen', 'Kayn', 'Fiora'])
q2 = Questions_and_Answers('What race is Rakan & Xayah?', 'Vastayan', ['Vastayan', 'Trolls', 'Titans', "Vastayashai'Rei"])
q3 = Questions_and_Answers('Which one of these characters was transmuted?','Warwick',['Singed','LeBlanc','Gragas','Warwick'])
q4 = Questions_and_Answers('What is kassadins ultimate?','A quick teleport',['He launches himself','A quick teleport','Devours the target','Suppresses an enemy'])
q5 = Questions_and_Answers('Which nation is the strongest?','Demacia',['Freljord','Ionia','Noxus','Demacia'])
q6 = Questions_and_Answers('Which one of these champions is strongest in the lore?','Ornn',['Ornn','Aurelion Sol','Karma','Bard'])
q7 = Questions_and_Answers('Which one of these champions has a sister?','Morgana',['Leona','Katarina','Morgana','Tristana'])
q8 = Questions_and_Answers('Which of these champions have a root ability?','Lux',['Galio','Teemo','Warwick','Lux'])
q9 = Questions_and_Answers('Which of these champions are classed as a jungler?','Gragas',['Teemo','Renekton','Gragas','Zed'])
q10 = Questions_and_Answers('Which of these champions is a pirate?','Gangplank',['Volibear','Poppy','Gangplank','Taric'])
q11 = Questions_and_Answers('The ruined king is named Viego','True',['True','False'])
q12 = Questions_and_Answers("Kayle's ultimate is called Devine Punishment",'False',['False','True'])
q13 = Questions_and_Answers('Which one of these characters is most hated?','Teemo',['Teemo','Fizz','Morgana','Lux'])
q14 = Questions_and_Answers('How many champions summon a creature as their ultimate?','3',['2','3','5','7'])
q15 = Questions_and_Answers("When was League of Legends made?",'October 27 2009',['October 27 2009','April 20 1969','September 11 2001','Donald Trumps birthday'])

# prints the score they got and congratulates them 
print(f"Thank you for playing, your final score was {score}, have a great day")
