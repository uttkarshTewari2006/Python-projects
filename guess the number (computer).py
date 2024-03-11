import random
num=None
while num!='0':
  num = input('welcome to random number game (computer), think of a number between 1 and 10 and when you are ready, type 0! ')


num1 = None
n = 0
input1=None
HigherBound = 10
LowerBound = 0
choices = list(range(10))
outputs = ['I guess that your number is {}!','Hmm, lemme try again, is it {}?', 'You buggin I definetely got it before, what about {}', 'how tf?!?!?! what about {}', 'my luck really awful out here, this one is definetely it: {}','Statistically I should have gotten it a long time ago, it\'s probably {}','this is getting out of hand, here: {}', 'enjoy your luck while it lasts I am winning all the next games, the number is {}', 'dang the universe is really out to get me, two options left I am going with {}','IUEHOIERUHGIUHRG WHAT ARE EVEN THE CHANCES OF THIS HAPPENING!!!!!']
while input1!='yes':

  num1 = random.choice(choices)
  print(outputs[n].format(num1+1))
  input1 = input('reply yes if i guessed correctly, higher if your number is higher than what I guessed, lower if your number is lower than what I guessed \n')
  if input1=='higher':
    LowerBound = max(LowerBound,num1+1)
  elif input1=='lower':
    HigherBound = min(HigherBound,num1)
  choices = list(range(LowerBound,HigherBound))
  n+=1

if n<=3:
  print('I am the goat bro get wrecked')
elif n<=5 and n>3:
  print('Good game bro this one was a draw')
elif n<=7 and n>5:
  print('sheesh you got me with this one but i will get you next time')
else:
  print('WTFAOSUHFOSUH I GOT REALLY UNLUCKY THIS IS NOT FAIR!!!!')


