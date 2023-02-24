#############################################################
# https://www.geocaching.com/geocache/GC82WV5               #
# Each of the nine letters A, B, C, D, E, F, G, H, J        #
# represents a digit from 1 to 9. Every digit is used once; #
# each letter represents a different digit.                 #
# H x H = E                                                 #
# A + F = G                                                 #
# F x H x J = A                                             #
# G + H = B                                                 #
# F + H = J                                                 #
# D - C = J                                                 #
# The geocache is at N49 16.X W123 04.Y, where              #
# X = HEJ + EFC and                                         #
# Y = GAB - JJD                                             #
#############################################################


def solve(letters):
    """
    Uses a backtracking algorithm to find the solution to geocache GC82WV5.

    Parameters:
    letters (dict): Keys (strings A-J) and all possibile values (lists of ints 0-9).

    Returns:
    solution (dict): Keys (strings A-J) with one int value each which satisy contraints.
    """
    pass

def check_constraints(**letters):
    """Returns True if contraints are satisfied, False otherwise."""
    pass

def print_answer(letters):
    """Given a dict of (letter, digit) pairs, prints the solution."""
    pass


if __name__ == '__main__':
    letters = {
        'A': list(range(10)),
        'B': list(range(10)),
        'C': list(range(10)),
        'D': list(range(10)),
        'E': list(range(10)),
        'F': list(range(10)),
        'G': list(range(10)),
        'H': list(range(10)),
        'J': list(range(10))
    }
    solution = solve(letters)
    print_answer(solution)