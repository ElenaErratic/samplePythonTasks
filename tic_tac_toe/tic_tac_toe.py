def print_board(board):
    print("---------")
    print('|', board[0], board[1], board[2], '|')
    print('|', board[3], board[4], board[5], '|')
    print('|', board[6], board[7], board[8], '|')
    print("---------")

def evaluate(board): 
  while True:
    global O_wins
    global X_wins
    global draw
    draw = False
    if '_' not in board:
      blank = 0
    else:
      blank = 1
    if ((board[0] == 'X' and board[1] == 'X' and board[2] == 'X')
      or (board[3] == 'X' and board[4] == 'X' and board[5] == 'X')
      or (board[6] == 'X' and board[7] == 'X' and board[8] == 'X')
      or (board[0] == 'X' and board[3] == 'X' and board[6] == 'X')
      or (board[1] == 'X' and board[4] == 'X' and board[7] == 'X')
      or (board[2] == 'X' and board[5] == 'X' and board[8] == 'X')
      or (board[0] == 'X' and board[4] == 'X' and board[8] == 'X')
      or (board[2] == 'X' and board[4] == 'X' and board[6] == 'X')):
      X_wins = True
    else:
      X_wins = False
    
    if ((board[0] == 'O' and board[1] == 'O' and board[2] == 'O')
      or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O')
      or (board[6] == 'O' and board[7] == 'O' and board[8] == 'O')
      or (board[0] == 'O' and board[3] == 'O' and board[6] == 'O')
      or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O')
      or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O')
      or (board[0] == 'O' and board[4] == 'O' and board[8] == 'O')
      or (board[2] == 'O' and board[4] == 'O' and board[6] == 'O')):
      O_wins = True
    else:
      O_wins = False
    
    if X_wins == False and O_wins == False and blank == 0:
      draw = True
      print("Draw")
      return draw
    if X_wins == True:
      print("X wins")
    if O_wins == True:
      print("O wins")
    break


def overwrite(i):
  global move
  
  if board[i] == "_":
    if move % 2 == 0:
      board[i] = "X"
    else:
      board[i] = "O"
    print_board(board)
    move += 1
  else:
    print("This cell is occupied! Choose another one!")

  return board[i]


def write_to_cell(x, y):
  if x == 1 and y == 1:
    cell = board[0]
    overwrite(0)
  elif x == 2 and y == 1:  
    cell = board[3]
    overwrite(3)
  elif x == 3 and y == 1:  
    cell = board[6]
    overwrite(6)
  elif x == 1 and y == 2:  
    cell = board[1]
    overwrite(1)
  elif x == 2 and y == 2:  
    cell = board[4]
    overwrite(4)
  elif x == 3 and y == 2:  
    cell = board[7]
    overwrite(7)
  elif x == 1 and y == 3:  
    cell = board[2]
    overwrite(2)
  elif x == 2 and y == 3:  
    cell = board[5]
    overwrite(5)
  elif x == 3 and y == 3:  
    cell = board[8]
    overwrite(8)
  
  return board  


# game starts

initial_board = list('_' * 9)
board = initial_board
print_board(board)

move = 0
while True:
  coordinates = input('Enter the coordinates: ').split()
  try:
    x = int(coordinates[0])
    y = int(coordinates[1])
  except ValueError:
    print("You should enter numbers!")

  if not type(x) is int and not type(y) is int:
    pass
  elif x not in range(1, 4) or y not in range(1, 4):
    print("Coordinates should be from 1 to 3!")
  else:
    write_to_cell(x, y)
    evaluate(board)
    if X_wins or O_wins or draw:
      break
