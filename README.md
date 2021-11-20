# Battleship
Battleship game in Python using socket programming (client/server)

The game is similar to a regular game of battleship but instead is only singleplayer. The game works by using two machines and establishing a connection using TCP/IP protocols.
The game uses a config fike (serverconfig.ini) where the player enters the host and port of the server side of the application. The user then enters the host and port of the client side as user input.

When the game loads, a randm map of ships is geneated and the following options appear:

1: Pick a target
2: Show Info
3: Show Ship Map
4: Reset Map
5: Quit

Option 1 brings up the player board, which will start empty. 

A square marked 'O' indicated a square that has not been targeted yet. 
A square marked 'X' marks a hit
A square marked '-' marks a square that has been targeted but does not contain a ship. 

The player is prompted to enter a valid target (between A1 and E5 case sensitive) and is then asked for their next option.

Option 2 opens up a text file containing the following information

Option 3 Shows the player the map of where the ships are.

Option 4 resets the map with new ship positions and resets the player map.

Option 5 closes the server.

The player must close the server before closing the application in order to free the port.
