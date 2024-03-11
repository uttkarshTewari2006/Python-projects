
import random
import numpy as np
class TicTacToe:

  def __init__(self):
    self.defaultBoard2 = ['a','b','c','d','e','f','g','h','i']
    self.defaultBoard = np.array([['a','b','c'],['d','e','f'],['g','h','i']])

    self.clearBoard()
    self.players = {'player 1':'X','player 2':'O'}


  def displayBoard(self):

    self.newArr=np.array([['-']*3]*3)
    for i in range(3):
      for j in range(3):
        if self.board[i][j]=='X' or self.board[i][j]=='O':
          self.newArr[i][j] = self.board[i][j]

    for i in self.newArr:
      print(' '.join(i), '\n')
    '''for i in range(3):
      print('  '.join(self.newArr[i]))
      print('  '.join(self.defaultBoard[i]), '\n')'''

  def clearBoard(self):
    self.board = self.defaultBoard.copy()
    self.choices = ['a','b','c','d','e','f','g','h','i']


  def CheckPosition(self, board= True):
    if board == True:
      board = self.board
    if type(board) == str:
      print(board)
    for i in range(len(board)):
      #horizontal
      if all([x == board[i][0] for x in board[i]]):
        if board[i][0]=='X':
          return 'player 1'
        if board[i][0]=='O':
          return 'player 2'
      #vertical
      if all([x == board.T[i][0] for x in board.T[i]]):
        if board.T[i][0]=='X':
          return 'player 1'
        if board.T[i][0]=='O':
          return 'player 2'

    #diagonal

    self.dig1 = [board[i][i] for i in range(len(board))]
    self.dig2 = [board[i][2-i] for i in range(len(board))]

    if all([x==board[0][0] for x in self.dig1]):
      if board.T[0][0]=='X':
          return 'player 1'
      if board.T[0][0]=='O':
        return 'player 2'

    if all([x==board[0][2] for x in self.dig2]):
      if board[0][2]=='X':
          return 'player 1'
      if board[0][2]=='O':
        return 'player 2'

    #finally, checks for draw
    draw = True
    for i in board:
      for j in i:
        if j in self.defaultBoard2:
          draw = False
          break
    if draw:
      return 'draw'
  #replaces the number equavilent of the letter Lth index with val
  def Replace(self,L,val, board=True, mutator=True):
    boole=False
    if board== True:
      board = self.board
      boole = True


    self.num = ord(L.upper()) - 64

    if not mutator:
      board = board.copy()

    if self.num<=3:
      board[0][self.num-1] = val
    elif self.num<=6:
      board[1][self.num-4] = val
    else:
      board[2][self.num-7] = val

    if not boole:
      return board

  def checkWinner(self,comp=False):
        results = self.CheckPosition()
        if results == 'draw':
          print('Here\'s the final board:')
          self.displayBoard()
          print('\n The game is a draw!!')


          while True:
            inp2 = input("if you want to play again, type 'restart', if you want to quit, type 'quit'")
            a = self.stringIf(inp2)
            if a=='continue' or inp2=='':
              return 'continue'
            elif a=='break':
              return 'break'

        if results!=None:
          if comp:
            print('{} won!!'.format(results if results=='player 1' else 'computer'))
            print("Here's the final board:")
            self.displayBoard()
          else:
            print('Here\'s the final board:')
            self.displayBoard()
            print('\n congrats, {} won!!'.format(results))


          while True:
            inp2 = input("if you want to play again, type 'restart', if you want to quit, type 'quit'")
            a = self.stringIf(inp2)
            if a=='continue' or inp2=='':
              return 'continue'
            elif a=='break':
              return 'break'

  def pvc(self, type1):
    if type1 == 'random':
      print('welcome to pvc-random, the compute makes random moves so you better win!')
    if type1 == 'unbeatable':
      print('welcome to unbeatable mode, get ready to get absolutely destroyed! (hint: it\'s possible to draw if played perfectly!)')\

    n = 0

    while True:
      n+=1
      self.displayBoard()
      print("Here's your choices: {}".format(self.choices))
      userInput = input('make a move, type quit to quit, type restart to restart: ')

      if userInput=='quit':
        print('Thanks for playing!')
        break
      elif userInput=='restart':
        print('Clearing board...')
        n=0
        self.clearBoard()
        continue
      elif userInput=='':
        n+=1
        print('please type a valid square to play. Here\'s your choices: {}'.format(self.choices))
        continue

      if userInput.lower() in self.choices:
        self.choices.remove(userInput.lower())
        self.Replace(userInput.lower(),'X')
      else:
        print('invalid input! available squares are {}'.format(self.choices))

      if n>=3:
        a = self.checkWinner(comp=True)
        if a=='continue':
          n=0
          continue

        if a=='break':

          break

      if type1== 'random' or (n==1 and 'e' not in self.choices):
        compInput = random.choice(self.choices)
      elif type1 == 'unbeatable':
        if n==1 and 'e' in self.choices:
          compInput = 'e'
        else:
          compInput = self.get_move()

      self.choices.remove(compInput)
      self.Replace(compInput,'O')
      print('the computer picks {}!'.format(compInput))

      if n>=3:
        a = self.checkWinner(comp=True)
        if a=='continue':
          continue
          n=0
        if a=='break':
          n=0
          break

  def pvc_random(self):

    self.pvc('random')

  def pvc_unbeatable(self):
    self.pvc('unbeatable')

  def get_move(self):
    return self.minimax(self.board,self.choices,recursion = False)


  def minimax(self, board, choices, player=True, letter=None, recursion = True, alpha=float('-inf'), beta=float('inf')):
    playerMap = {True: 'O', False: 'X'}

    # Check terminal states

    if self.CheckPosition(board) == 'player 1':
        return -1 * (len(choices) + 1)
    elif self.CheckPosition(board) == 'player 2':
        return len(choices) + 1
    elif self.CheckPosition(board) == 'draw':
        return 0

    if player == True:
      best = float('-inf')

    else:
      best = float('inf')

    #without filtering thingy

    for i in choices: #iterating through all possible moves
        newBoard = board.copy()  # Create a copy of the board for each move
        newChoices = choices.copy()  # Create a copy of choices for each move

        newChoices.remove(i)
        self.Replace(i, playerMap[player], newBoard)

        # Recursively calculate utility values for opponent's moves
        utilVal = self.minimax(newBoard, newChoices, not player, letter=i)

        if player:  # Maximizing player

          if utilVal>best:
            best = utilVal
            bestMove = i
          '''alpha = max(alpha, result)
            if beta <= alpha:
                break  # Beta cutoff'''
        else:  # Minimizing player
          if utilVal<best:
            best = utilVal
            bestMove = i

    if recursion:
      return best
    else:
      return bestMove
    '''beta = min(beta, result)
            if beta <= alpha:
                break  # Alpha cutoff'''


  def stringIf(self,inp):
    if inp.lower()=='quit':
        print('thanks for playing this game mode! \n')
        return 'break'

    elif inp.lower() =='restart':
        self.clearBoard()
        self.n=0
        return 'continue'

    if inp.lower() in self.choices:
      self.choices.remove(inp.lower())

    else:
      print('Invalid input, the following squares are available: {}'.format(self.choices))
      self.n-=1
      return 'continue'






  def pvp(self):
    #self.choicesCopy = self.choices.copy()
    self.n=0
    self.players = ['player 1','player 2']
    self.tokens = ['X','O']
    while True:
      self.n+=1
      self.f = (self.n+1)%2 #when this is 0 it's player's two's turn otherwise it's player 1's turn
      print("Here's the board:")
      self.displayBoard()
      print("Here's your choices: {}".format(self.choices))
      inp1 = input("{}'s turn, type one of the letters (a-i) to place your {} on the square. Other commands: 'restart', 'quit' (neither case sensitive): ".format(self.players[self.f],self.tokens[self.f]))
      self.a1 = self.stringIf(inp1)
      if self.a1=='break':
          self.clearBoard()
          print(self.choices)
          break

      if self.a1=='continue':
          continue
      self.Replace(inp1.lower(),self.tokens[self.f])

      if self.n>=3:
        self.a = self.checkWinner()
        if self.a=='break':
          self.clearBoard()
          break
        if self.a=='continue':
          continue



  def play(self):
    print('Welcome to ticTacToe!')
    while True:
      gameMode = input(" to play pvp, type '1' \n to play against computer (easy), type '2' \n to play against computer (hard), type '3' \n To quit, type 'quit':\n ")
      if gameMode == '1':
        self.pvp()
      elif gameMode == '2':
        self.pvc_random()
      elif gameMode == '3':
        self.pvc_unbeatable()
      elif gameMode.lower() == 'quit':
        print('play again!')
        break
      else:
        print("invalid input")

newGame = TicTacToe()


newGame.play()