# import random
# c=['parota','chicken rice','biriyani','noodles','tea']
# a=random.choice(c)
# G=['_' for i in a]
# attempts=4

# while attempts > 0 and '_'in G:
#     print('Word: ',''.join(G))
#     g=input('Guess a letter:')
#     if g in a:
#         for i in range(len(a)):
#             if a[i]==g:
#                 G[i]= g
#     else:
#         attempts-=1
#         print(f'Incorrrect!{attempts} attempats left ')
# if '_' not in G:
#     print('Congrats! you found the word',a)
# else:
#     print('Game over! the word was:',a)


# q= {
#     "To whom do you vote in 2026?":"TVK",
#     "Which is good energy drink?":"campa",
#     "Good slogan for campa":"campa kudi nenachatha mudi"
# }
# print(len(q))
# s=0
# for b ,answer in q.items():
#     a=input(b+'').strip()
#     if a==answer:
#         print('Correct!')
#         s +=1
#     else:
#         print(f'Wrong the correct answer is {answer}. ')

# print(f"Final Score: {s}/{len(q)}")

import random

def scramble_word(word):
   return "".join(random.sample(word, len(word)))

words = ["python", "developer", "programming", "challenge"]
word = random.choice(words)
scrambled = scramble_word(word)

print("Scrambled word:", scrambled)

attempts = 3
while attempts > 0:
   guess = input("Guess the word: ").lower()
   if guess == word:
       print("Correct! ????")
       break
   else:
       attempts -= 1
       print(f"Wrong! {attempts} attempts left.")

if attempts == 0:
   print(f"Game over! The correct word was {word}.")

print('Welcome to AskPython Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: What is your Favourite programming language?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: Do you follow any author on AskPython? ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: What is the name of your favourite website for learning Python?')
    if answer.lower()=='askpython':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')