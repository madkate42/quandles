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



def main():
    


if __name__ == "__main__":
    main()