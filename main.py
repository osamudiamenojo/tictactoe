from play_board import play_at_position,  get_winner,is_board_full,clear_board

X_CHOICE = 'X'
O_CHOICE = 'O'

game_list = []

while True:
  clear_board()
  print()
  print("1. New Game")
  print("2. Previous Games")
  print("3. Exit")

  choice = int(input("\nEnter a choice: "))

  if choice == 2:
    print()
    print("--------------------------")
    for game in game_list:
      print(game)
    print("--------------------------")
    print()
   
    continue
  elif choice == 3:
    break
  

  player1_name = input("Player 1's name: ")
  player2_name = input("Player 2's name: ")
  
  
  player1_choice = input(f"{player1_name}, Choose 'X' or 'O': ")
  player1_choice = player1_choice.upper()
  
  #set player 2 choice based on player one's choice
  if player1_choice == X_CHOICE:
    player2_choice = O_CHOICE
  else:
    player1_choice = O_CHOICE
    player2_choice = X_CHOICE
  
  
  print("----------------------")
  print("Welcome to Tic Tac Toe")
  print(f"\n{player1_name} plays as '{player1_choice}'and {player2_name} play as '{player2_choice}'. Lets play!\n")
  
  
  
  while True:  
    #Player 1 turn
    player1_play_position   = input(player1_name + ", enter a position to play at (i.e., 1,1) ")
    player1_pos_row = int(player1_play_position.split(",")[0])
    player1_pos_col = int(player1_play_position.split(",")[1])
    
    play_at_position (player1_pos_row , player1_pos_col , player1_choice)
  
    winner = get_winner()
    #print("Winner", winner)
    if winner == player1_choice:
      print(f"{player1_name} wins!")
      game_list.append(f"{player1_name} X {player2_name} - {player1_name} won!")
      break
      
    #Player 2 turn
    player2_play_position   = input(player2_name + ", enter a position to play at (i.e., 1,1) ")
    player2_pos_row = int(player2_play_position.split(",")[0])
    player2_pos_col = int(player2_play_position.split(",")[1])
    
    play_at_position (player2_pos_row , player2_pos_col , player2_choice)
    
    winner = get_winner()
    #print("Winner", winner)
    if winner == player2_choice:
      print(f"{player2_name} wins!")
      game_list.append(f"{player1_name} X  {player2_name} - {player2_name} won!")
      break
  
    if is_board_full():
      print("Draw!")
      game_list.append(f"{player1_name} VS.  {player2_name}. Draw!")

      break

