import random 
choices2 = ['rock','paper','scissors']

input1 = None
print('welcome to rock,paper,scissors! type r for rock, p for paper and s for scissors')
translater = {'r':'rock','p':'paper','s':'scissors'}
beater = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}

while True:
  choice = random.choice(choices2)
  input1 = input('what\'s your choice? \n')

  if input1=='quit':
    break
  if input1 not in translater:  # Check if user input is valid
      print('Invalid input. Please enter "r" for rock, "p" for paper, or "s" for scissors')
      continue

  inputTranslated = translater[input1]

  if inputTranslated==choice:
    print('great minds thing alike, we both chose the same option! no one won unfortunately :(( ')
  elif inputTranslated==beater[choice]:
    print('wow you got lucky beating me like that, good job tho!')
  elif choice == beater[inputTranslated]:
    print('that was too easy! pick better next time...')

print('it was fun playing with you, play again!')