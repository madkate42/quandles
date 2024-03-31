
def calculate_line(values, equation):
    linear_sum = 0
    for i in range(len(values)):
        linear_sum += values[i] * equation[i]
    return linear_sum

t = [[2, -1, -1],
     [-1, -1, 2],
     [-1, 2, -1]]

m = 3

n = 6

knot = [[2, -1, 0, 0, 0, -1],
        [-1, 0, 0, 0, -1, 2],
        [0, 2, -1, 0, 0, -1],
        [0, -1, 2, -1, 0, 0],
        [0, 0, -1, 2, -1, 0]]

colorings_big_knot = []

# so values could be 0 to n - 1 (mod n - 1)
# if 7 colors, then mod 7 so 0-6.
# each variable could be 0-6 (7 options), then 
#if equal to 0 that's good ...
# we have 6 variables...

for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                for e in range(n):
                    for f in range(n):
                        coloring = [a,b,c,d,e,f]
                        # now check if valid coloring... 
                        works = True
                        for equation in knot:
                            if calculate_line(coloring, equation) % n != 0:
                                works = False 
                        
                        if works:
                            colorings_big_knot.append(coloring)

# print(calculate_line([1,1,1,1,1,1], knot[0]))
print("For big knot, there are", len(colorings_big_knot), "valid colorings.")
print(colorings_big_knot)

colorings_small_knot = []

for a in range(3):
    for b in range(3):
        for c in range(3):
            coloring = [a,b,c]
            works = True 
            for equation in t:
                if calculate_line(coloring, equation) % 3 != 0:
                    works = False 
            
            if works:
                colorings_small_knot.append(coloring)

print("For trefoil, there are", len(colorings_small_knot), "colorings")
print(colorings_small_knot)

print(calculate_line([1,0,2], t[0]))
print(calculate_line([1,0,2], t[1]))
print(calculate_line([1,0,2], t[2]))