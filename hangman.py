import random
word_list = [
    'apple', 'banana', 'orange', 'lemon', 'kiwi', 'grape', 'peach', 'strawberry', 'pineapple', 'watermelon',
    'avocado', 'blueberry', 'raspberry', 'blackberry', 'cranberry', 'pomegranate', 'grapefruit', 'tangerine',
    'cantaloupe', 'honeydew', 'cucumber', 'tomato', 'broccoli', 'cauliflower', 'asparagus', 'eggplant',
    'zucchini', 'mushroom', 'spinach', 'lettuce', 'carrot', 'potato', 'onion', 'garlic', 'ginger', 'radish',
    'turnip', 'celery', 'parsley', 'cilantro'
]

lettersNotUsed = []

n1 =0
print('welcome to hangman!')
word = random.choice(word_list)
stringList = ['-']*len(word)

while True:
  n1+=1
  print('Here\'s what we got:')
  print(''.join(stringList), 'letters you haven\'t used:', ' '.join(lettersNotUsed),'\n')

  letter = input('gimme a letter from a-z (caps is fine but u a psychopath for that), type quit to reveal the word (u a loser for that ngl): ')
  if letter=='quit':
    print('\n It\'s all good bro some people are just not meant to win in this world. The word was {}'.format(word))
    break
  letter = letter.lower()
  if letter in word:
    n2 = 0
    for i in range(len(word)):
      if letter==word[i]:
        n2+=1
        stringList[i] = letter
    print('Good job! {} appears {} amount of times in the word!'.format(letter,n2))
  else:
    print('{} not in word'.format(letter))
    lettersNotUsed.append(letter)
  if ''.join(stringList)==word:
    print('congratulations!, it took you {} amount of times to beat hang man!'.format(n1))
    break


