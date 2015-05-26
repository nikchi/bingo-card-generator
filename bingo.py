import random
import os
path = os.getcwd() + "\\" #Gets the directory.  Reads content files and saves output here.
db = [[0,0,0,0,0],[0,0,0,0,0],[0,0,"FREE SPACE",0,0],[0,0,0,0,0],[0,0,0,0,0]] #The default, empty board.  0 is not a number used in bingo.  Signifies that a space hasn't been filled yet

###Functions for operation

def printboard(board): #prints the bingo board.  used for debugging
    for i in range(0,5):
        strout = ""
        for j in range(0,5):
            if j < 4:
                strout += (str(board[i][j]) + ",")
            else:
                strout += (str(board[i][j]) + "\n")
        print(strout)

def getrand(input): #faster than typing random.randrange every time it's needed
    return random.randrange(0,input)

def loadfile(rarity): #opens and parses a file corresponding to a rarity level
    e = open(path + rarity + '.txt')
    content = e.read().splitlines()
    return content

def getitem(buffer): #randomly chooses an item of a particular rarity, and then removes it from that list so it can't be picked again
    size = len(buffer)
    num = getrand(size)
    out = buffer.pop(num)
    return out

def fillbuffer(): #gets items from different rarity lists and puts them into a list for fillboard
    buffer = []
    for i in range (0,9):
        buffer.append(getitem(common))
    for i in range (0,9):
        buffer.append(getitem(uncommon))
    for i in range (0,4):
        buffer.append(getitem(rare))
    for i in range (0,1):
        buffer.append(getitem(ultrarare))
    for i in range (0,1):
        buffer.append(getitem(legendary))
    return buffer

def fillboard(board, buffer): #fills in each empty slot on the board with a random item from the buffer
    for i in range(0,5):
        for j in range(0,5):
            if board[i][j] == 0:
                board[i][j] = getitem(buffer)
    return 0

def writeboard(board): #saves the board as out.csv in the working directory
    try:
        os.remove(path + 'out.csv')
    except OSError:
        pass
    
    f = open(path + 'out.csv', 'w+')
    seq = []

    for i in range(0,5):
        strout = ""
        for j in range(0,5):
            if j < 4:
                strout += (str(board[i][j]) + ",")
            else:
                strout += (str(board[i][j]) + "\n")
        seq.append(strout)
    
    f.writelines(seq)
    return

def genboard(): #creates, fills, and writes a board
    newboard = db
    fillboard(newboard, fillbuffer())
    writeboard(newboard)
    
    return

###filenames
common = loadfile('sample_common')
uncommon = loadfile('sample_uncommon')
rare = loadfile('sample_rare')
ultrarare = loadfile('sample_ultrarare')
legendary = loadfile('sample_legendary')

###execution
genboard()
