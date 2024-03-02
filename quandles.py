"""
Brute forcing all possible quandles.
"""
import math 
from random import randint

def isQuandle(opTable):
    def axiom1(ot):
        for i in range(len(ot)):
            if ot[i][i] != i:
                return False 
        return True 
    
    def axiom2(ot):
        for i in range(len(ot)):
            for j in range(len(ot)):
                xpy = ot[i][j]
                if ot[xpy][j] != i:
                    return False 
        return True
    
    def axiom3(ot):
        for x in range(len(ot)):
            for y in range(len(ot)):
                for z in range(len(ot)):
                    left = ot[ot[x][y]][z]
                    right = ot[ot[x][z]][ot[y][z]]
                    if left != right:
                        return False 
        return True

    return (axiom1(opTable) and axiom2(opTable) and axiom3(opTable))

def generateOpTable(n):
    opTable = [[randint(0, n - 1) for i in range(n)] for i in range(n)]
    for i in range(n):
        opTable[i][i] = i
    # print("Randomly Generated operation table:")
    # print(opTable)
    return opTable

def main():
    # working wih operation tables 
    n = int(input("Select N (elements in X): "))
    opTable = [[0 for i in range(n)] for i in range(n)]
    table = [[0,2,0,2], [3,1,3,1], [2,0,2,0], [1,3,1,3]]
    # print("Is Quandle?:", isQuandle(table))
    # print(opTable)
    iterations = 0
    randTable = generateOpTable(n)
    while not isQuandle(randTable):
        randTable = generateOpTable(n)
        if isQuandle(randTable):
            print("Randomly generated quandle:", randTable)
            print("Is randomly generated a quandle:", isQuandle(randTable))
        iterations += 1
    print("After", iterations, "iterations.")


if __name__ == "__main__":
    main()