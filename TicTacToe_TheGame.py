import sys
import time

#Create the board
board = ["_","_","_","_","_","_"," "," "," "]


# Displays text with a typwriter effect
# This func is just for "enhanced" UI; leave out if not wanted 
def typewriter(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  
    
    
#Display Board
def display_game(board):
    print("\n+++++ TIC TAC TOE +++++\n")

    print("\t " + board[0] + "|" + board[1] + "|" + board[2])
    print("\t " + board[3] + "|" + board[4] + "|" + board[5])
    print("\t " + board[6] + "|" + board[7] + "|" + board[8])
   
    print("\n-----------------------")    


# Users choose their character
def player_char():
    char = "?"
    
    while char not in ["x", "o"]:
        time.sleep(0.2)
        typewriter("Choose your character: 'o' | 'x'?")
        char = input()
        
        if char not in ["x", "o"]:
            typewriter("Wrong character. Choose the ones that are presented")
        elif char == "x":
            typewriter(f"Player 1 will use 'x' \nPlayer 2 will use 'o'" )
            time.sleep(0.2)
            return ("x","o")
        else:
            typewriter(f"Player 1 will use 'o' \nPlayer 2 will use 'x'")
            time.sleep(0.2)
            return("o","x")


#User picks location on board to make a move
def pick_location():
    run = "True"
    x = [1,2,3,4,5,6,7,8,9]
    in_range = False
    
    while run.isdigit() == False or in_range == False:
        typewriter(f"Make your move and choose a position:\n ")
        run = input()
        if run.isdigit() == False:
            typewriter("You didn't include a digit from the list. \n\nTry again. ")
            
        if run.isdigit() == True:
            if int(run) in x:
                in_range = True
                x = x.remove(int(run))
            else:
                print(f"This position is not available anymore. \n\nChoose among these options:\n\n {x}")
    return int(run) -1


# Check if symbol is in grid before putting in place
def check_grid(board, position):
    
    while True:
        if board[position] == "x" or board[position] == "o":
            typewriter("This position is already chosen.")
        
            typewriter("Make another choice.")
            time.sleep(0.1)
        return False
    else:
        return True
    
    
# Place marker on board
def place_marker(position, marker, board):
    
    board[position] = marker
    
    return display_game(board)


# Check if a player won
def check_win(board, player):
    wins = [[0,1,2], [3,4,5], [6,7,8],[0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]  # Define winning patterns

    for triplet in wins: #Checks if there is a winner
        if all(board[i] == player for i in triplet):
            typewriter("It's a win!")
            typewriter(f"Congrats {player}")
            
            return False
        
    if " " not in board and "_" not in board: #Checks if game is a draw
        typewriter("It's a draw!")
        time.sleep(0.25)
        typewriter("No one wins...")
        return False
    
    return True


# Replay Game function
def restart_game(board):
    restart = "mt"
    
    while restart not in ["y", "n"]:
        
        restart = input("Do you want to play again? Y or N\n")
    
        if restart.casefold() not in ["y", "n"]:
            print("Wrong input! Answer properly!!!")
            
            

    if restart.casefold() == "y": #Game continues
        print("Time for a new game!")
        
        return True
    else:                          #End of the game
        typewriter("Game has ended!")
        time.sleep(0.5)
        typewriter("See you next time...")
        return False
            
    
"""                        TIC TAC TOE GAME                                """
    
"""
This script combines all above functions and forms the final version of
the game
"""
def tictactoe():
   
    board = ["_","_","_","_","_","_"," "," "," "]
    runner = True
    
    while runner: 
        #Board is displayed
        display_game(board) 
        
        #Player chooses character
        playa = player_char()
        
        
        game_on = True
        while game_on:
            
            #Player 1 makes move
            position = pick_location()
            checking = check_grid(board, position)

            if  checking == False:
                place_marker(position, playa[0],board)
                
                
                game_on = check_win(board, playa[0])
                if game_on == False:
                    break
        
            #Player 2 makes move
            position = pick_location()
            checking = check_grid(board, position)
    
            if  checking == False:
                place_marker(position, playa[1],board)
            
                game_on = check_win(board, playa[1])         
                if game_on == False:
                    break
            
        
        # Ask if replay game
        runner = restart_game(board)
        
        #Clear board after game has ended
        board = ["_","_","_","_","_","_"," "," "," "]
           