play_board = [
  [' ' ,' ' ,' '],
  [' ' ,' ' ,' '],
  [' ' ,' ' ,' ']
]

X_CHOICE = 'X'
O_CHOICE = 'O'

#prints the board
#you don't need to modify this function
def print_board():
  for i in range(3):
    for j in range(3):
      print("[" + play_board[i][j] +"]", end="")#print elements without new line
    print()#print empty line after each row
  print('--------------')

def play_at_position( row , col, player ):
  if play_board[row][col] == ' ':
    play_board[row][col] = player.upper()
    print_board()
  else:
    print("Position is not empty")

def get_at_position(row, col):
  return play_board[row][col]

def get_winner():
  #check win first row
  if get_at_position(0,0) != ' ' and get_at_position(0,0) == get_at_position(0,1) == get_at_position(0,2):
    if get_at_position(0,0) == X_CHOICE:
      return X_CHOICE
    elif get_at_position(0,0) == O_CHOICE:
      return O_CHOICE
  #check win second row
  if get_at_position(1,0) != ' ' and get_at_position(1,0) == get_at_position(1,1) == get_at_position(1,2):
    if get_at_position(1,0) == X_CHOICE:
        return X_CHOICE
    elif get_at_position(1,0) == O_CHOICE:
        return O_CHOICE
  else:
    return None;
  


def is_board_full():
  for i in range(3):
    for j in range(3):
      if play_board[i][j] == ' ':
        return False
  return True


def clear_board():
  for i in range(3):
    for j in range(3):
      play_board[i][j]= ' '