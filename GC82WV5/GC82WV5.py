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
import itertools


def solve():
    """
    Reduces the solution space to find a solution to geocache GC82WV5. In theory, there
    are 10^9 different combinations of the digits 1-9. However, one constrain of the
    problem is that all digits have to be unique. Therefore, by only considering
    permutations of the digits 1-9 we can reduce the solution space drastically:
    9! / 10^9 = 0.00036, i.e. 0.036% of all possible combinations.

    Returns:
    solution (dict): (letter, digit) mappgins which satisfy constraints.

    Raises:
    ValueError: No solution could be found.
    """
    for digits in itertools.permutations(range(1, 10)):
        if check_constraints(to_letters(digits)):
            return to_letters(digits)
    raise ValueError('No solution could be found.')

def to_letters(digits):
    """Returns a dict of letter-to-digit mappings."""
    return dict(zip(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J'], digits))

def check_constraints(letters):
    """Returns True if contraints are satisfied, False otherwise."""
    if letters['H'] * letters['H'] != letters['E']:
        return False
    if letters['A'] + letters['F'] != letters['G']:
        return False
    if letters['F'] * letters['H'] * letters['J'] != letters['A']:
        return False
    if letters['G'] + letters['H'] != letters['B']:
        return False
    if letters['F'] + letters['H'] != letters['J']:
        return False
    if letters['D'] - letters['C'] != letters['J']:
        return False
    if len(set(letters.values())) != len(letters):  # all digits need to be unique
        return False
    return True

def print_answer(letters):
    """Given a dict of (letter, digit) pairs, prints the solution."""
    X = int(str(letters['H']) + str(letters['E']) + str(letters['J']))
    X += int(str(letters['E']) + str(letters['F']) + str(letters['C']))
    Y = int(str(letters['G']) + str(letters['A']) + str(letters['B']))
    Y -= int(str(letters['J']) + str(letters['J']) + str(letters['D']))
    print('The geocache is at N49 16.{X} W123 04.{Y}'.format(X=X, Y=Y))


if __name__ == '__main__':
    solution = solve()
    print_answer(solution)
