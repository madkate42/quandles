import itertools

"""
Input: Q(L), |X| and op_table_X 
Output: Valid colorings / number of valid colorings
"""

def give_valid_colorings(X, tX, Q, size_q):
    valid_colorings = []
    valid_inmod_colorings = []
    # need to generate k-permutation .. n = X, k = size_q 
    for f in itertools.product(range(X), repeat=size_q):
        # perm has size_q elements, ranged 0 to X - 1
        # element 0 -> f[0]
        # 1 -> f[1]
        # print(f[0], f[1])
        valid = True
        valid_inMod = True 
        for q in Q:
            if not (f[q[2]] == tX[f[q[0]]][f[q[1]]]):
                valid = False 
            if not ((f[q[2]] % size_q) == (tX[f[q[0]] % size_q][f[q[1]] % size_q] % size_q)):
                valid_inMod = False     
        if valid:
            valid_colorings.append(f) # append map 
        if valid_inMod:
            valid_inmod_colorings.append(f)

    print("There are", len(valid_colorings), "valid colorings.")
    # print(valid_colorings)
    print("However, there are valid in modulus:", len(valid_inmod_colorings))
    # print(valid_inmod_colorings)
    return valid_colorings

def generate_dihedral(X):
    tX = [[0 for x in range(X)] for x in range(X)]
    for i in range(X):
        for j in range(X):
            tX[i][j] = (2 * j - i) % X
    return tX

tX = [[0, 2, 1],
    [2, 1, 0],
    [1, 0, 2]] # dihedral 

X = 3

# # Trefoil:
# Q = [(2, 0, 1), # 2 |> 0 = 1
#      (1, 2, 0), # 1 |> 2 = 0
#      (0, 1, 2)] # 

# size_q = 3

# STAR
Q = [(2, 1, 0),
     (3, 2, 1),
     (4, 3, 2),
     (0, 4, 3),
     (1, 0, 4)]
size_q = 5

for i in range(20):
    print(i)
    n = 15
    give_valid_colorings(i, generate_dihedral(i), Q, size_q)





    