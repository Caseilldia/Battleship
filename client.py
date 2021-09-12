# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 12:31:52 2021

@author: Casey
"""

import socket
import pickle

lst = ['A', 'B', 'C', 'D', 'E']
lst2 = ['1', '2', '3', '4', '5']

# method to print out information about game
def display_info(info):
    
    for line in info:
        print(line)

# method to print out game board
def display_game_board(game_board):
    
    for row in game_board:
        for col in row:
            if len(col) == 9:
                print(col, end = "   ")
            elif len(col) == 10:
                print(col, end = "  ")
            elif len(col) == 2:
                print("", end = "     " + col + "     ")
            else:
                print(col, end = "     ")
        print()

# method to print out board for player
def display_player_board(player_board):
    
    rows = ['A', 'B', 'C', 'D', 'E']
    columns = ['1', '2', '3', '4', '5']
    
    print("  " + columns[0] + " "+ columns[1] + " "+ columns[2] + " "+ columns[3] + " " + columns[4])
    
    for row in range(0,5):
        print(rows[row], end = " ")
        for col in range(0,5):
            print(str(player_board[row][col]), end = " ")
        print()

# method to check if string can be represented as an int
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

# method to display and get user input for game choice
def display_choices():
    
    print("")
    print("Options")
    print("1: Pick a target")
    print("2: Show Info")
    print("3: Show Ship Map")
    print("4: Reset Map")
    print("5: Quit")
    
    choice = input("Choice: ")
    
    while True:
        if not RepresentsInt(choice) or int(choice) < 1 or int(choice) > 6:
            choice = input("enter a valid number between 1 and 5: ")
        if RepresentsInt(choice) and int(choice) > 0 and int(choice) < 6:
            return int(choice)
            
    

def Main():

    
    host = input("Enter the host ip of the server: ")
    port = int(input("Enter the port number of the host server: "))
    
    #server is tuple of host and port
    server = (host,port)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # connect to server    
    s.connect(server)
    
    while True:

        # et user choice
        choice = display_choices()
        str_choice = str(choice)

        s.sendto(str_choice.encode('utf-8'), server)

        # if playing game
        if choice == 1:
            player_board, addr = s.recvfrom(1024)
            decoded_player_board = pickle.loads(player_board)
            display_player_board(decoded_player_board)

            #asking for target
            while True:
                pos = input("Enter a valid Input: ")
                if pos[0] in lst and pos[1] in lst2 and len(pos) == 2:
                    break

            s.sendto(pos.encode('utf-8'), server)
            message, addr = s.recvfrom(1024)
            new_message = message.decode('utf-8', 'ignore')
            print(new_message)
            
            # if game is over
            if new_message == 'You Win!!!!':
                message, addr = s.recvfrom(1024)
                quit_message = message.decode('utf-8')
                print(str(quit_message))
                
                #close client connection
                s.close()
                
        # if showing info
        elif choice == 2:
            info, addr = s.recvfrom(1024)
            decoded_info = pickle.loads(info)
            display_info(decoded_info)
        
        # if showing ships map
        elif choice == 3:
            game_board, addr = s.recvfrom(1024)
            decoded_game_board = pickle.loads(game_board)
            display_game_board(decoded_game_board)
        
        # if reset boards
        elif choice == 4:
            message, addr = s.recvfrom(1024)
            reset_message = message.decode('utf-8')
            print(str(reset_message))
            
        # if quit
        elif choice == 5:
            message, addr = s.recvfrom(1024)
            quit_message = message.decode('utf-8')
            print(str(quit_message))
            s.close()
            break
            
        else:
            print("Enter a valid choice (1-5)")



if __name__=='__main__':
    Main()
