#!/usr/bin/env python3

from itertools import permutations

MPCdesignations = [1, 136108, 136472]
permu_list = (list(permutations(MPCdesignations, 3)))


def solve(x, y, z):
    solutions = []
    equations = [[8*x + 8*y + 12*z, 2947748],[18*x + 2*y + 28*z, 2722916],[6*x + 11*y + 20*z, 2454788],
                 [14*x + 4*y + 16*z, 2245003],[13*x + 7*y + 22*z, 2900212],[9*x + 3*y + 30*z, 2654486],
                 [5*x + 12*y + 8*z, 2318212],[6*x + 14*y + 10*z, 2997803],[4*x + 10*y + 12*z, 2600652],
                 [8*x + 5*y + 5*z, 2249445]]

    for elem in equations:
        expression, value = elem
        if expression == value:
            solutions.append([value])
    if len(solutions) != 0:
        return solutions
    else:
        return False


for elem in permu_list:
    x, y, z = elem
    solution = solve(x, y, z)
    if solution:
        print("password:", 12*x + 8*y + 17*z)
        print("right sides of matching equations:", solution)
        print("x=%d, y=%d, z=%d" % (x, y, z))
