import gameboard
import player

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
gameboards = [
    gameboard.GameBoard()
]
board = gameboards[0]
# Create a new Player called played starting at position 3,2
players = [
    player.Player( 3, 2)
]
played = players[0]

while True:
    board.printBoard(played.rowPosition, played.columnPosition)
    selection = input("Make a move: ")
    # TODO
    # Move the player through the board
    # Check if the player has won, if so print a message and break the loop!
