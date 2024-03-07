import itertools
from quandles import isQuandle

def apply_permutation(table, perm):
    # Apply the permutation to the rows
    permuted = [table[i] for i in perm]
    # Apply the permutation to the columns
    permuted = [[row[j] for j in perm] for row in permuted]
    # for l in permuted:
    #     for e in permuted:
    #         permuted[i][j] = 
    index_mapping = {original: new for original, new in enumerate(perm)}
    # Apply the mapping to each element in the table
    permuted_with_elements = [[index_mapping[element] for element in row] for row in permuted]
    return permuted_with_elements
    return permuted

def tables_are_isomorphic(t1, t2):
    n = len(t1)
    for perm in itertools.permutations(range(n)):
        # print("Perm:", perm)
        permuted_t1 = apply_permutation(t1, perm)
        # print("Permuted table:", permuted_t1)
        if permuted_t1 == t2:
            return True
    return False

def remove_isomorphic_tables(tables):
    unique_tables = []  # To hold tables after removing isomorphic ones
    n = len(tables)

    # To track if a table has been found to be isomorphic and removed
    is_removed = [False] * n

    # brute to check
    for t1 in tables:
        for t2 in tables:
            
            if tables_are_isomorphic(t1, t2):
                print("Isomorphism found:", t1, t2)

    for i in range(n):
        if not is_removed[i]:
            for j in range(i + 1, n):
                if tables_are_isomorphic(tables[i], tables[j]):
                    is_removed[j] = True
                    print("Found isomorphic")
            # Assume the current table is unique until found otherwise
            # unique_tables.append(tables[i])
            # for j in range(i+1, n):
            #     if not is_removed[j] and tables_are_isomorphic(tables[i], tables[j]):
            #         # Mark the table as removed if it's isomorphic to any already considered table
            #         is_removed[j] = True
    for i in range(n):
        if not is_removed[i]:
            unique_tables.append(tables[i])

    return unique_tables


def generate_tables(n):
    # Create an iterable for the range of values each cell can take
    cell_values = range(n)
    # Generate the Cartesian product for an n x n table
    # This will generate all possible configurations as flat tuples
    for config in itertools.product(cell_values, repeat=n*n):
        # Reshape the flat tuple into an n x n table
        table = [list(config[i*n:(i+1)*n]) for i in range(n)]

        yield table

def valid_tables(n):
    all_tables = generate_tables(n)
    valid_tables = []
    for table in all_tables:
        if isQuandle(table):
            valid_tables.append(table)
    return valid_tables

def main():
    tables = valid_tables(3)
    unique = remove_isomorphic_tables(tables)
    print("ALL:", tables)
    for t in tables:
        print(t)
    print(len(tables))
    print(len(unique))
    for t in unique:
        print(t)
    # t1 = [[0,0,1], [1,1,0], [2,2,2]]
    # t2 = [[0,0,0], [2,1,1], [1,2,2]]
    # print(tables_are_isomorphic(t1, t2))

if __name__ == "__main__":
    main()
