# compute quandle polynomial 

def quandle_polynomial(op_table):
    n = len(op_table)
    
    def c(x):
        return sum(1 for y in range(n) if op_table[y][x] == y)
    
    def r(x):
        return sum(1 for y in range(n) if op_table[x][y] == x)
    
    quandle_poly_terms = []
    
    for x in range(n):
        rx = r(x)
        cx = c(x)
        quandle_poly_terms.append(f"s^{rx} * t^{cx}")
    print("Quandle poly terms:", quandle_poly_terms)
    quandle_polynomial = " + ".join(quandle_poly_terms)
    return quandle_polynomial

op_table = [
    [0, 0, 0], 
    [2, 1, 1], 
    [1, 2, 2]
]

mq1 = [[0, 0, 0],
       [1, 1, 1],
       [2, 2, 2]]

print(quandle_polynomial(mq1))