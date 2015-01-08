import random
import sys
import os
path = 'C:/Users/Class2018/Desktop/bingo/'
db = [[0,0,0,0,0],[0,0,0,0,0],[0,0,"Dennis makes a spreadsheet (FREE SPACE)",0,0],[0,0,0,0,0],[0,0,0,0,0]]
wbv = [[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[1,1,1,1,1],[0,0,0,0,0]]
wbh = [[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[1,0,1,0,1],[0,0,1,0,0]]

"""
#test horizontal bingo
def vcheck(board):
    for i in [0,1,2,3,4]:
        bingo = 1
        for j in [0,1,2,3,4]:
            if board[i][j] == 0:
                bingo = 0
        if bingo == 1:
            print("BINGO!")
            break
        else:
            print("No bingo!")
    return bingo
            
def hcheck(board):
    for i in [0,1,2,3,4]:
        bingo = 1
        for j in [0,1,2,3,4]:
            if board[j][i] == 0:
                bingo = 0
        if bingo == 1:
            print("BINGO!")
            break
        else:
            print("No bingo!")
    return 1
            
def check(board):
    if vcheck(board) == 1:
        return 1
    else:
        return hcheck(board)
"""

def printboard(board):
    for i in [0,1,2,3,4]:
        print(str(board[0][i]) + "," + str(board[1][i]) + "," + str(board[2][i]) +
              "," + str(board[3][i]) + "," + str(board[4][i]))

def getrand(size):
    x = random.randrange(0,size)
    return x

def loadfile(rarity):
    e = open(path + rarity + '.txt')
    content = e.read().splitlines()
    return content

def getslot(board, rarity):
    firstnum = getrand(5)
    secondnum = getrand(5)
    if board[firstnum][secondnum] != 0:
        return getslot(board, rarity)
    else:
        board[firstnum][secondnum] = getitem(rarity)

def getitem(rarity):
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
    i = 0
    str0 = (str(board[0][i]) + "," + str(board[1][i]) + "," + str(board[2][i]) + "," + str(board[3][i]) + "," + str(board[4][i]) + '\n')
    i = 1
    str1 = (str(board[0][i]) + "," + str(board[1][i]) + "," + str(board[2][i]) + "," + str(board[3][i]) + "," + str(board[4][i]) + '\n')
    i = 2
    str2 = (str(board[0][i]) + "," + str(board[1][i]) + "," + str(board[2][i]) + "," + str(board[3][i]) + "," + str(board[4][i]) + '\n')
    i = 3
    str3 = (str(board[0][i]) + "," + str(board[1][i]) + "," + str(board[2][i]) + "," + str(board[3][i]) + "," + str(board[4][i]) + '\n')
    i = 4
    str4 = (str(board[0][i]) + "," + str(board[1][i]) + "," + str(board[2][i]) + "," + str(board[3][i]) + "," + str(board[4][i]) + '\n')

    seq = [str0,str1,str2,str3,str4]
    f.writelines(seq)
    return
    

common = loadfile('common')
uncommon = loadfile('uncommon')
rare = loadfile('rare')
ultrarare = loadfile('ultrarare')
legendary = loadfile('legendary')

genboard()
