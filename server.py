# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from random import randrange
import random
import socket
import pickle
import configparser

game_board = []
player_board = []
options_text = []
rules_text = []
hits = 0
sunk = 0

Ships = {'Carrier': 4, 'Battleship': 3, 'Destroyer': 2} #size of each ship


def initialise_board(): #create a 4x4 board
    letters = ["A", "B", "C", "D", "E"]
    for x in range(len(letters)):
        game_board.append([])
        for y in range(0, 5):
            game_board[x].append(str(letters[x]) + str(y))
           
    for x in range(len(letters)):
        player_board.append([])
        for y in range(0, 5):
            player_board[x].append('O')

    choose_ships(game_board) #call function to choose ships
def choose_ships(game_board):
        Ships = {'Carrier': 4, 'Battleship': 3, 'Destroyer': 2} #size of each ship
        Ships_List = [['Carrier', 1],['Battleship', 1],['Destroyer', 1]] #number of ships to place
   
        lst = ['A', 'B', 'C', 'D', 'E']
        lst2 = [1,2,3,4]

        for x in Ships_List: #place ships
            r = 0

            while x[1] > 0: #check there's ships available
           
                str1 = random.choice(lst)
                str2 = random.choice(lst2)
                final = str1 + str(str2)
           
                r += 1
                type = x[0]
                ship_size = Ships[x[0]]
                position = final.format(x[0]) #choose position (i.e, A1)
                check = place_ship(game_board, ship_size, position, type)
                if check is True:
                    x[1] -= 1
               

   
        
def place_ship(game_board, ship_size, position, ship_type):
    row = position[0]
    row = ord(row) - 65
    if len(position) > 2:
        col = (position[1] + position[2])
    else:
        col = position[1]
    row = int(row)
    col = int(col)



    orientation = randrange(2) #horizontal or vertical
   
    if orientation == 1:
        direction = randrange(2) #up or down
       
        if direction == 1:
            result = check_availability(game_board, ship_size, col, row, 'up')
            if result is True:
                for i in range(0, ship_size):
                    game_board[int(row - i)][int(col) - 1] = str(ship_type)

            
        else:
            #print(str(ship_size) + " " + str(col) + " " + str(row))
            result = check_availability(game_board, ship_size, col, row, 'down')
            if result is True:
                for i in range(0, ship_size):
                    game_board[int(row + i)][int(col) - 1] = str(ship_type)

            


    else:
        direction = randrange(2)
       
       
        if direction == 1:
            result = check_availability(game_board, ship_size, col, row, 'right')
            if result is True:
                for i in range(0, ship_size):
                    game_board[int(row)][int(col) + i - 1] = str(ship_type)
            

        else:
            result = check_availability(game_board, ship_size, col, row, 'left')
            if result is True:
                for i in range(0, ship_size):
                    game_board[int(row)][int(col) - i - 1] = str(ship_type)
            

    return result



def check_availability(game_board, ship_size, col, row, direction): #check that ship can be placed
    check_ships = ["Carrier", "Battleship", "Destroyer"]
    if direction == 'up':
        if row - int(ship_size) >= 0: #check ship within boundaries
            for i in range(0, ship_size):
                if game_board[int(row - i)][int(col) - 1] not in check_ships: #check for collision
                    pass
                else:
                    return False
            return True
        else:
            return False
    elif direction == 'down':
        space = row + int(ship_size)
        if space <= 4: #check ship within boundaries
            for i in range(0, ship_size):
                rawr = game_board[int(row + i)][int(col) - 1]
                if rawr not in check_ships: #check for collision
                    pass
                else:
                    return False
            return True
        else:
            return False
    elif direction == 'right':
        if col + int(ship_size) <= 5: #check ship within boundaries
            for i in range(0, ship_size):
                if game_board[int(row)][int(col) + i - 1] not in check_ships: #check for collision
                    pass
                else:
                    return False
            return True
        else:
            return False
    elif direction == 'left':
        if col - int(ship_size) >= 0: #check ship within boundaries
            for i in range(0, ship_size + 1):
                if game_board[int(row)][int(col - 1) - i] not in check_ships: #check for collision
                    pass
                else:
                    return False
            return True
        else:
            return False


def check_hit(pos):

    check_ships = ["Carrier", "Battleship", "Destroyer"]
    victory = False
    choice = 0
   
    global sunk
    global Ships

    
   
    lst = ['A', 'B', 'C', 'D', 'E']
    lst2 = ['1', '2', '3', '4', '5']

    row = pos[0]
    row = ord(row) - 65
    if len(pos) > 2:
        col = (pos[1] + pos[2])
    else:
        col = pos[1]
        row = int(row)
        col = int(col) - 1
        target = game_board[row][col]
        ship_hit = target
        
        # if hit, target = name of ship, else will be position on board
        target = str(ship_hit)
    if target in check_ships:
        player_board[row][col] = 'X'
        Ships[target] = Ships[target] - 1
        if target == "Carrier":
            # if all carrier positions hit
            if Ships['Carrier'] == 0:
                sunk += 1
                if sunk == 3:
                    return "Victory"
                else:
                    return 'Sunk Carrier'
            else:
                return "Hit Carrier"
        if target =="Battleship":
            # if all battleship positions hit
            if Ships['Battleship'] == 0:
                sunk += 1
                if sunk == 3:
                    return "Victory"
                else:
                    return 'Sunk Battleship'
            else:
                return "Hit BattleShip"
        if target =="Destroyer":
            # if all destroyer positions hit
            if Ships['Destroyer'] == 0:
                sunk += 1
                if sunk == 3:
                    return "Victory"
                else:
                    return 'Sunk Destroyer'
            else:
                return "Hit Destroyer"
    else:
        player_board[row][col] = "-"
        return "Miss"

    
  
   
def reset():
   
    global game_board
    global player_board
   
    # clear board and reinitialise it with new random ships
    game_board.clear()
    player_board.clear()
    game_board = []
    player_board = []
    initialise_board()

   
def close():
    print("Close")
       
# getting host and port from cinfig file
configparser = configparser.ConfigParser()  
configFilePath = 'ServerConfig.ini'
configparser.read(configFilePath)
   
host = configparser.get('Server', 'host')
port = configparser.get('Server', 'port')

new_host = host[1:-1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((new_host, int(port)))

print("Server Started at port " + port)

initialise_board()

options_text.append("")
options_text.append("Options")
options_text.append("1: Pick a target")
options_text.append("2: Show Info")
options_text.append("3: Show Ship Map")
options_text.append("4: Reset Map")
options_text.append("5: Quit")

rules_text.append(r"Option 1 brings up the player board, which will start empty.")
rules_text.append(r"A square marked 'O' indicated a square that has not been ")
rules_text.append(r"targeted yet. A square marked 'X' marks a hit, and a square")
rules_text.append(r"marked '-' marks a square that has been targeted but does")
rules_text.append(r"not contain a ship. The player is prompted to enter a valid") 
rules_text.append(r"target (between A1 and E5 case sensitive) and is then asked")
rules_text.append(r"for their next option.")
rules_text.append("")
rules_text.append(r"Option 2 opens up a text file containing information about")
rules_text.append(r"the game (this file) for their next option.")
rules_text.append("") 
rules_text.append(r"Option 3 Shows the player the map of where the ships are.")                 
rules_text.append("")
rules_text.append(r"Option 4 resets the map with new ship positions and resets ")
rules_text.append(r"the player map")
rules_text.append("")
rules_text.append(r"Option 5 closes the server.")

while True:

    # get user choice from client
    data, addr = s.recvfrom(1024)
    choice = int(data.decode('utf-8'))
    
    if choice == 1:
        
        #sent to client player board
        sent_player_board = pickle.dumps(player_board)
        s.sendto(sent_player_board, addr)

        # wait for client to send target
        data, addr = s.recvfrom(1024)
        target = data.decode('utf-8')

        # get result of target
        returned = check_hit(str(target))
        
        if returned == "Victory":
            sent_str = "You Win!!!"
            s.sendto(sent_str.encode('utf-8'), addr)
            s.close()
            break
        
        s.sendto(returned.encode('utf-8'), addr)

    elif choice == 2:
        ## do nothing
        sent_rules_text = pickle.dumps(rules_text)
        s.sendto(sent_rules_text, addr)
    elif choice == 3:
        sent_game_board = pickle.dumps(game_board)
        s.sendto(sent_game_board, addr)
    elif choice == 4:
        reset()
        sent_str = "Board reset"
        s.sendto(sent_str.encode('utf-8'), addr)
    else:
        sent_str = "Closing Server"
        s.sendto(sent_str.encode('utf-8'), addr)
        s.close()
        break


