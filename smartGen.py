import math 
from random import randint
from quandles import isQuandle, generateOpTable

def print_table(t):
    print("---------")
    for l in t:
        for e in l:
            print(e," ",end="", sep="")
        print()
    print("---------")

def fill_slot(opTable):
    to_fill = randint(0, len(opTable) - 1)
    for i in range(len(opTable)):
        for j in range(len(opTable)):
            if opTable[i][j] == -1:
                opTable[i][j] = to_fill
                return opTable

def fill_on_axioms(t):
    for i in range(len(t)):
        for j in range(len(t)):
            print_table(t)
            if t[i][j] != j:
                t[t[i][j]][j] = i 
    return t



def is_valid_operation(ot):
    return isQuandle(ot)

def try_fill_slot(ot, x, y, value):
    original = ot[x][y]
    ot[x][y] = value
    if not is_valid_operation(ot):
        ot[x][y] = original
        return False
    return True

def fill_on_axioms(ot):
    n = len(ot)
    for i in range(n):
        for j in range(n):
            if ot[i][j] == -1:  # Find an unfilled slot.
                # Attempt to fill this slot with a valid value.
                for possible_value in range(n):
                    if try_fill_slot(ot, i, j, possible_value):
                        break  # Stop if successfully filled with a valid value.
                else:
                    print("No valid filling found for position", i, j)
                    return ot
    return ot


"""
0 2 -
2 1 2
1 0 1

"""

def main():
    n = int(input())
    opTable = [[-1 for i in range(n)] for i in range(n)]
    for i in range(n):
        opTable[i][i]  = i 
    print(opTable)
    fill_slot(opTable)
    print(opTable)
    fill_on_axioms(opTable)
    print(opTable)

    

if __name__ == "__main__":
    main()