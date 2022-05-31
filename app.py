from gameboard import GameBoard as gameboard
from player import Player as player
from coins import Coins as coins

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")
print("Try to get to the end! Good Luck!")
print("-----------------------------")


# TODO
# Create a new GameBoard called board
board = gameboard()
# Create a new Player called played starting at position 3,2
played = player(3,2)
playerCoins = str(0)
availableCoin = [
    coins(1,2),
    coins(1,7),
    coins(5,3),
    coins(5,7)
]

print("Player Coins: " + playerCoins)

while True:
    board.printBoard(played.rowPosition, played.columnPosition)
    selection =input("Make a move: ")
    
    
    # TODO
    # Move the player through the board
    
    if(selection == 'w'):
        board.checkMove(testRow=played.rowPosition, testColumn=played.columnPosition)
        played.moveUp()
    elif(selection == 's'):
        played.moveDown()
    elif(selection == 'a'):
        played.moveLeft()
    elif(selection == 'd'):
        played.moveRight()
    

    # Check if the player has won, if so print a message and break the loop!
    board.checkWin(playerRow=played.rowPosition, playerColumn=played.columnPosition)    