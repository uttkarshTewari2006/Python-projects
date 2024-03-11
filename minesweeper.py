
import numpy as np
import random
class mineSweeper(object):

  def __init__(self):
    self.boardSize = 0
    self.numBombs = 0
    self.board = None
    self.displayBoard = None

  def new_board(self,boardSize=10, numBombs=10):
    self.boardSize = boardSize
    self.numBombs = numBombs
    self.board = np.zeros((boardSize, boardSize), dtype=int)
    self.displayBoard = np.full((boardSize, boardSize), '-', dtype=str)
    #placing mines
    self.mines = []

    n=0
    while True:
      if n>=self.numBombs:
        break
      row = int(random.random()*boardSize)
      column = int(random.random()*boardSize)
      if (row,column) in self.mines:
          continue
      else:
        self.mines.append((row,column))
        n+=1

      self.board[row][column] = -1


      #adding a number to every square around the mine if it isn't another mine and is a valid index
      if row<boardSize and column+1<boardSize and self.board[row][column+1]!=-1:
        self.board[row][column+1] += 1 #square up
      if row+1<boardSize and column<boardSize and self.board[row+1][column]!=-1:
        self.board[row+1][column] += 1 #square to the right
      if row<boardSize and column-1<boardSize and self.board[row][column -1]!=-1 and column-1>=0:
        self.board[row][column -1] += 1 #square down
      if row-1<boardSize and column<boardSize and self.board[row-1 ][column]!=-1 and row-1>=0:
        self.board[row-1 ][column] += 1 #square to the left
      if row+1<boardSize and column+1<boardSize and self.board[row+1][column+1]!=-1:
        self.board[row+1][column+1] += 1 #upper right diagonal
      if row+1<boardSize and column-1<boardSize and self.board[row+1][column-1]!=-1 and column-1>=0:
        self.board[row+1][column-1] += 1 #lower right diagonal
      if row-1<boardSize and column+1<boardSize and self.board[row-1][column+1]!=-1 and row-1>=0:
        self.board[row-1][column+1] += 1 #upper left diagonal
      if row-1<boardSize and column-1<boardSize and self.board[row-1][column-1]!=-1 and row-1>=0 and column-1>=0:
        self.board[row-1][column-1] += 1 #lower left diagonal

    #setting the display board as a bunch of dashes representing squares players can play


  def display_board(self):
    for i in range(0,len(self.board)+1):
      if i==0:
        for L in range(self.boardSize+1):
          print(L, end='  ')
        print('\n')
      else:
        for j in range(0,len(self.board)+1):
          if j==0:
            print(i, end="  ")
          else:
            if self.displayBoard[i-1][j-1]==-1:
              print('*', end="  ")
            else:
              if j<10:
                print(self.displayBoard[i-1][j-1], end="  ")
              else:
                print(self.displayBoard[i-1][j-1], end="   ")
        print('\n')

  def reveal(self, row, column, boardSize, first=True):
    #first reveals the chosen square
    if first:
      self.takenList = [(row,column)]
    else:
      self.takenList.append((row,column))

    opposites = {1:3,3:1,0:2,2:0,7:4,4:7,6:5,5:6}
    self.displayBoard[row][column] = self.board[row][column]
    if self.board[row][column] !=0:
      return None
    else:
      #if no mines surrounding the square, reveals all squares recursively until squares with mines
      if row<boardSize and column+1<boardSize and self.board[row][column+1]!=-1 and (row,column+1) not in self.takenList:
        #print('1, row: {}, column: {}'.format(row,column))

        self.reveal(row,column+1, boardSize, False)


      if row+1<boardSize and column<boardSize and self.board[row+1][column]!=-1:
        #print('2, row: {}, column: {}'.format(row,column))

        self.reveal(row+1,column, boardSize, False)


      if row<boardSize and column-1<boardSize and column-1>=0 and self.board[row][column -1]!=-1 and (row,column+1) not in self.takenList:
        #print('3, row: {}, column: {}'.format(row,column))

        self.reveal(row, column-1, boardSize, False)


      if row-1<boardSize and column<boardSize and row-1>=0 and self.board[row-1 ][column]!=-1 and (row-1,column) not in self.takenList:
        #print('4, row: {}, column: {}'.format(row,column))

        self.reveal(row-1,column, boardSize, False)


      if row+1<boardSize and column+1<boardSize and self.board[row+1][column+1]!=-1 and (row+1,column+1) not in self.takenList:
        #print('5, row: {}, column: {}'.format(row,column))

        self.reveal(row+1,column+1, boardSize, False)


      if row+1<boardSize and column-1<boardSize and column-1>=0 and self.board[row+1][column-1]!=-1 and (row+1,column-1) not in self.takenList:
        #print('6, row: {}, column: {}'.format(row,column))

        self.reveal(row+1,column-1, boardSize, False)


      if row-1<boardSize and column+1<boardSize and row-1>=0 and self.board[row-1][column+1]!=-1 and (row-1,column+1) not in self.takenList:
        #print('7, row: {}, column: {}'.format(row,column))

        self.reveal(row-1,column+1, boardSize, False)


      if row-1<boardSize and column-1<boardSize and column-1>=0 and row-1>=0 and self.board[row-1][column-1]!=-1 and (row-1,column-1) not in self.takenList:
        #print('8, row: {}, column: {}'.format(row,column))

        self.reveal(row-1,column-1, boardSize, False)



  def isWon(self):
    if np.count_nonzero(self.displayBoard == '-') == self.numBombs:
      return True
    return False

  def check_board(self, row, column, boardSize):
    #checks if the square is a mine, is directly next to a mine or if the player won the game, If neither conditions are met, calls reveal method




    val = self.board[row][column]

    if val  == -1:
      return 'mine'
    else:
      print('squares yet to check: ', np.count_nonzero(self.displayBoard == '-') , 'bombs: ', self.numBombs)
      self.reveal(row,column, boardSize)

  def set_up(self):
    veryEasy = (5,3)
    easy = (10,5)
    medium = (10,15)
    hard = (10,20)
    veryHard = (15,25)

    while True:
      print("Welcome to minesweeper! Chose your difficulty: \n")
      difficulty = input("type '1' for very easy, '2' for easy, '3' for medium, '4' for hard, '5' for very hard and '6' for custom: ")

      if difficulty == '1':
        self.new_board(5,3)
        print('You chose very easy, you better win!')
        break

      elif difficulty == '2':
        self.new_board(*easy)
        print('you chose easy, a good mode for beginers. Good luck!')
        break

      elif difficulty == '3':
        self.new_board(*medium)
        print('you chose medium, a good balance between a good time and a good challenge!')
        break

      elif difficulty == '4':
        self.new_board(*hard)
        print('you chose hard, get ready for a challenge!')
        break

      elif difficulty == '5':
        self.new_board(*veryHard)
        print("you chose very hard. The odds aren't in your favor but I believe in you")
        break

      elif difficulty == '6':
        while True:
          boardSize = input('type your board size: ')
          if type(boardSize) != int and boardSize>25:
            print('please select a valid number as your board size, the max amount is 25')
            continue
          break

        while True:
          numMines = input('type your minefield size: ')
          if type(numMines) != int and numMines>30:
            print('please select a valid number as your board size, the max amount is 25')
            continue
          if numMines>= boardSize**2:
            print("That's more mines than squares! please select a lower number of mines.")
            continue
          break

        self.new_board(boardSize, numMines)

      else:
        print('type a valid number from 1-6 representing your difficulty.')
        continue

  def play(self):
    responses = ['Wow, you got lucky on that one...', 'You live another day!!', "You didn't step on a mine this time but how long will you last?", "No casualties today!", 'you are safe']
    responses2 = {'mine':'You stepped on a mine and lost!' , True: 'congratulations, you won minesweeper! '}
    self.set_up()
    takenSquares = []
    #print(self.board)

    while True:
      val = False
      print("here's the board:")
      self.display_board()

      inp = input('chose your square represented by two indices (0-9) seperated by a comma')
      try:
        cordinate = inp.split(',')
        cordinate = [int(i) for i in cordinate]
        assert len(cordinate)==2
        print(cordinate)
      except:
        print('please type two numbers seperated by comma, try again')
        continue


      if cordinate[0] in range(self.boardSize+1) and cordinate[1] in range(self.boardSize+1) and cordinate not in takenSquares:
        result = self.check_board(cordinate[1]-1,cordinate[0]-1,self.boardSize)
        status = self.isWon()

        if result =='mine' or status:
          self.displayBoard = self.board
          print("Here's the final board (mines are noted by 'X's)")
          self.display_board()
          print('\n')
          if status:
            print('congratulations, you won minesweeper!')
          else:
            print('you stepped on a mine and lost!')


          while True:
            inp2 = input("to play a different mode type 'quit' to exit the game, type 'exit'")
            if inp2.lower()=='quit':
              self.__init__()
              self.play()
              break
            elif inp2.lower()=='exit':
              val = True
              break
          if val==True:
            break



        else:
          print(np.random.choice(responses))
          takenSquares.append(cordinate)
          continue

      elif cordinate in takenSquares:
        print('Square already picked, do better!')
      else:
        print('invalid input, cordinates out of range!')


newGame2 = mineSweeper()
newGame2.play()