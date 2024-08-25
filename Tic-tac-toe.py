"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jakub Macíček
email:  macicekjakub@gmail.com
discord: TheKmzm #9073
"""
from random import randint
from time import sleep
oddelovac = "=" * 50
full_tiles = []
tiles = {}

def rules():
    """Vypíše pravidla a vysvětlení jak hrát hru."""
    print(oddelovac,"""GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
First player is randomly selected.""", sep="\n")     
    for i in range(1,10):
        write(i,i)
    table()
    clean()

def write(symbol, position :int):
    """It writes the character in the appropriate place in the table and then prints it."""
    full_tiles.append(position)
    tiles["tile{}".format(position)] = symbol
    
def table():
    """Prit current plaing table."""
    line = " +---+---+---+"
    print(f"{line}\n",tiles["tile1"],tiles["tile2"],tiles["tile3"],"",sep=" | ")
    print(f"{line}\n",tiles["tile4"],tiles["tile5"],tiles["tile6"],"",sep=" | ")
    print(f"{line}\n",tiles["tile7"],tiles["tile8"],tiles["tile9"],f"\n{line}",sep=" | ")

def player1_turn(): 
    """Player one move."""
    global lastTurn
    lastTurn = 1
    char = "X"  #Player's character
    while True: #input loop
        print(oddelovac)
        position = input(f"Player('{char}') Please enter your move number: ")
        print(oddelovac)
        try:    #Input test for nonnumbers
            position = int(position)
        except ValueError:
            print("Type number btw. 1-9")
            continue
        if position in full_tiles:  #Input test for free tile
            print("This tile is occupy, type valid number.")
            continue
        if position in range(1,10): #Input test for legit number
            write(char,position)
            table()
            break
        print("Type valid number btw. 1-9!")

def player2_turn():
    """Player two move."""
    global lastTurn
    lastTurn = 0
    char = "O"  #Player's character
    while True: #input loop
        print(oddelovac)
        position = input(f"Player('{char}') Please enter your move number: ", )
        print(oddelovac)
        try:    #Input test for nonnumbers
            position = int(position)
        except ValueError:
            print("Type number btw. 1-9")
            continue
        if position in full_tiles:  #Input test for free tile
            print("This tile is occupy, type valid number.")
            continue
        if position in range(1,10): #Input test for legit number
            write(char,position)
            table()
            break
        print("Type valid number btw. 1-9!")

def random_1_player():
    """It randomly selects the first player."""
    if randint(1,2) == 1:   #randomizer
        player1_turn()
    else :
        player2_turn()
    
def chec4wWin():
    """It will check if there is a win or a draw, if so it will write it."""
    win = False
    win_comb = [["tile1","tile2","tile3"],["tile4","tile5","tile6"],["tile7","tile8","tile9"],
                ["tile1","tile4","tile7"],["tile2","tile5","tile8"],["tile3","tile6","tile9"],
                ["tile1","tile5","tile9"],["tile3","tile5","tile7"]]
    for t in win_comb:
        if ((tiles[t[1]] == tiles[t[2]] == tiles[t[0]]) and (tiles[t[1]] != " ") and win == False ):    #checks winning combinations
            char = tiles[t[1]]
            winner = f"'{char}' win the game."
            win = True 
            print(winner)      
    if (len(full_tiles) == 9) and (win == False):   #checks for a tie
        print("Tie")
        win = True 
    return(win)

def clean():
    """Clears the variables used during the game to its base state."""
    global full_tiles
    global tiles
    full_tiles = []
    tiles = {}
    for x in range(1, 10):
        tiles["tile{0}".format(x)] = " "
    return()

def again():
    """It'll make sure the player can play over and over again for as long as he wants."""
    x = 0
    while True:
        print(oddelovac)
        again = input("Do you want play again?\nJust type yes.\nIf you want shut this down type exit.\n")
        if again in ["yes", "y"]:   #again
            hra(True)
        elif again in ["exit", "Exit"]: #Exit
            break
        else:
            x += 1  #counter
        if x == 5:  #Exit if playr type nonsens
            print("Let me help you, i see you realy strugle to type EXIT.")
            sleep(3)
            break  
        
def hra(again=False):
    """Starts the game"""
    if again == False:  #only for new player
        print(oddelovac,"Welcome to Tic Tac Toe", sep="\n")
        rules()
    print(oddelovac)
    print("Let's start the game")
    random_1_player()
    win = False
    while not(win): #loop until win or tie
        if lastTurn == 1:
            player2_turn()
        else :
            player1_turn()
        win = chec4wWin()
    clean()
    
if __name__ == "__main__":
    hra()
    again()