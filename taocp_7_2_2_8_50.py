# taocp_7_2_2_8_50.py / June 2020 / Nathan Brixius @natebrix
#
# A partial solution to exercise 50 from TAOCP 7.2.2.8, exercise 50.
# This problem is found in "Pre-Fascicle 9b": fasc9b.ps
#
# Exercise 50 asks us to solve the skeleton multiplication puzzle:
#
#          N  N  N
#    x  N  N  N  N
#    -------------
#       N  N  N  7
#    N  N  N  N
# N  N  N  N
# N  N  N  
# ----------------
# 7  7  7  7  7  7
#
# where N != 7.
#
# More details can be found at nathanbrixius.wordpress.com.


from constraint import *

def make_puzzle():
    """ Create a CSP representing part of the skeleton puzzle. """
    problem = Problem()
    problem.addVariable("n_1", list(range(100, 999+1)))
    problem.addVariable("n_2", list(range(1000, 9999+1)))

    not_seven = [0, 1, 2, 3, 4, 5, 6, 8, 9] # no sevens allowed!
    
    # n_1 = d_13 d_12 d_11
    problem.addVariable("d_13", not_seven)
    problem.addVariable("d_12", not_seven)
    problem.addVariable("d_11", not_seven)

    # n_2 = d_24 d_23 d_22 d_21
    problem.addVariable("d_24", not_seven)
    problem.addVariable("d_23", not_seven)
    problem.addVariable("d_22", not_seven)
    problem.addVariable("d_21", not_seven)

    # last line of puzzle
    problem.addConstraint(lambda n_1, n_2: n_1 * n_2 == 777777, ['n_1', 'n_2'])

    # Establish that n_0 and n_1 are the sum of their digits.
    problem.addConstraint(lambda d_11, d_12, d_13, n_1: 
                          100 * d_13 + 10 * d_12 + d_11 == n_0, 
                          ['d_11', 'd_12', 'd_13', 'n_1'])
    problem.addConstraint(lambda d_21, d_22, d_23, d_24, n_2: 
                          1000 * d_24 + 100 * d_23 + 10 * d_22 + d_21 == n_2, 
                          ['d_21', 'd_22', 'd_23', 'd_24', 'n_2'])

    problem.addConstraint(lambda d_11, d_21: (d_11 * d_21) % 10 == 7, ['d_11', 'd_21'])

    # It is possible (but tedious) to write down the remaining partial
    # products.  Since I have omitted them, we are solving a less
    # restrictive version of the original problem.
    #

    # This is the 'N' in the first product row, next to the 7.
    #problem.addConstraint(lambda d_11, d_12, d_21, d_22: 
    #                      ((d_21 * d_12) + (d_11 * d_21) // 10) % 10 != 7, 
    #                      ['d_11', 'd_12', 'd_21', 'd_22'])

    return problem


def solve_puzzle(problem):
    """ Solve the CSP model. """
    print('Solving puzzle.')
    return problem.getSolutions()

def go():
    p = make_puzzle()
    s = solve_puzzle(p)
    # s is a list of solutions. Each solution is a dict of variable values.
    for t in s:
        print(f"{t['n_0']} x {t['n_1']} = {t['n_0'] * t['n_1']}")
