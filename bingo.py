import random
import os
path = os.getcwd() + "\\" #Gets the directory.  Reads content files and saves output here.
db = [[0,0,0,0,0],[0,0,0,0,0],[0,0,"FREE SPACE",0,0],[0,0,0,0,0],[0,0,0,0,0]] #The default, empty board.  0 is not a number used in bingo.  Signifies that a space hasn't been filled yet

###Functions for operation

def printboard(board): #prints the bingo board.  used for debugging
    for i in [0,1,2,3,4]:
        print(str(board[0][i]) + "," + str(board[1][i]) + "," + str(board[2][i]) +
              "," + str(board[3][i]) + "," + str(board[4][i]))

def getrand(input): #faster than typing random.randrange every time it's needed
    return random.randrange(0,input)

def loadfile(rarity): #opens and parses a file corresponding to a rarity level
    e = open(path + rarity + '.txt')
    content = e.read().splitlines()
    return content

def getslot(board, rarity): #ugly and will be replaced with something more elegant.  picks a spot on the card that hasn't been filled in yet
    firstnum = getrand(5)
    secondnum = getrand(5)
    if board[firstnum][secondnum] != 0:
        return getslot(board, rarity)
    else:
        board[firstnum][secondnum] = getitem(rarity)

def getitem(rarity): #randomly chooses an item of a particular rarity, and then removes it from that list so it can't be picked again
    size = len(rarity)
    num = getrand(size)
    out = rarity.pop(num)
    return out

def fillboard(board): 
    for i in range (0,9):
        getslot(board, common)
    for i in range (0,9):
        getslot(board, uncommon)
    for i in range (0,4):
        getslot(board, rare)
    for i in range (0,1):
        getslot(board, ultrarare)
    for i in range (0,1):
        getslot(board, legendary)
    return 0

def genboard():
    newboard = db
    fillboard(newboard)
    writeboard(newboard)
    return

def writeboard(board):
    try:
        os.remove(path + 'out.csv')
    except OSError:
        pass
    
    f = open(path + 'out.csv', 'w+')
    seq = []

    for i in range(0,5):
        strout = (str(board[0][i]) + "," + str(board[1][i]) + "," + str(board[2][i]) + "," + str(board[3][i]) + "," + str(board[4][i]) + '\n')
        seq.append(strout)
    
    f.writelines(seq)
    return

common = loadfile('sample_common')
uncommon = loadfile('sample_uncommon')
rare = loadfile('sample_rare')
ultrarare = loadfile('sample_ultrarare')
legendary = loadfile('sample_legendary')

genboard()
