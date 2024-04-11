from itertools import product

def calculate_mod_sum(values, equation, mod_k):
    return sum(val * eq for val, eq in zip(values, equation)) % mod_k

def find_valid_colorings(matrix, mod_k):
    num_vars = len(matrix[0]) 
    valid_colorings = []

    # Generates all possible combinations of colors
    for coloring in product(range(mod_k), repeat=num_vars):  
        if all(calculate_mod_sum(coloring, equation, mod_k) == 0 for equation in matrix):
            valid_colorings.append(coloring)
    
    return valid_colorings


matrix = [[2, -1, 0, 0, 0, -1],
        [-1, 0, 0, 0, -1, 2],
        [0, 2, -1, 0, 0, -1],
        [0, -1, 2, -1, 0, 0],
        [0, 0, -1, 2, -1, 0]]
mod_k = 6

matrix = [[2, -1, -1],
        [-1, -1, 2],
        [-1, 2, -1]]
mod_k = 3

valid_colorings = find_valid_colorings(matrix, mod_k)
print(f"There are {len(valid_colorings)} valid colorings.")
print(valid_colorings)
