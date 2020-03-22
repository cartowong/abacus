import random

from Core import Problem, Skill
from typing import List, Tuple

# ============================================================
# Private constants.
# ============================================================

__digits_no49 = (0, 1, 2, 3, 5, 6, 7, 8)
__digits_no05 = (1, 2, 3, 4, 6, 7, 8, 9)


# ============================================================
# Private utility functions.
# ============================================================

def __randbool(p: float) -> bool:
    """
    Bernoulli random variable.

    :param p: the probability of True
    :return: a sample of Bernoulli random variable
    """
    return random.random() < p


def __randpath(a: int, forward: bool) -> Tuple[int]:
    """
    Given an integer a in {0, 1, ..., 9}, find a random path of integers from a to 9 (forward) or
    0 (backward) so that in each step exactly one (lower or upper) bead is added (if forward) or
    is subtracted (if backward).

    :param a: the given integer a
    :param forward: Is forward?
    :return: a sample of random path
    """
    path: List[int] = [a]
    if forward:
        while path[len(path) - 1] != 9:
            x = path[len(path) - 1]
            x1 = x % 5
            x2 = 1 if x >= 5 else 0
            two_ways = x1 < 4 and x2 == 0
            if x1 == 4 or (two_ways and __randbool(0.2)):
                path.append(x + 5)
            else:
                path.append(x1 + 1 + 5 * x2)

        return tuple(path)
    else:
        while path[len(path) - 1] != 0:
            x = path[len(path) - 1]
            x1 = x % 5
            x2 = 1 if x >= 5 else 0
            two_ways = x1 > 0 and x2 == 1
            if x1 == 0 or (two_ways and __randbool(0.2)):
                path.append(x - 5)
            else:
                path.append(x1 - 1 + 5 * x2)

        return tuple(path)


def __pick_simple_addend(x: int, allow_upper_bead: bool) -> int:
    """
    Given an integer x, randomly choose a simple, non-zero addend y between -9 and 9. By simple,
    we mean the addition or subtraction only involves moving lower beads, and perhaps also moving
    one upper bead in the same rod in the opposite direction. For example, a simple "+7" involves
    moving two lower beads up and one upper bead down.

    :param x: the given integer
    :param allow_upper_bead: allow upper bead movement (in the opposite direction)?
    :return:
    """
    r1 = x % 5
    r2 = x % 10

    # With probability 1/9, we return 5 or -5.
    if allow_upper_bead and __randbool(1 / 9):
        return 5 if r2 < 4.5 else -5

    # Pick a simple addend that does not involve upper bead movement.
    ys = [y for y in range(-r1, 5 - r1) if y != 0]
    y = random.choice(ys)

    if allow_upper_bead and y * (r2 - 4.5) < 0 and __randbool(1 / 2):
        y = y + 5 if r2 < 4.5 else y - 5
    return y


def __pick_no_carry_borrow_addend(x: int) -> int:
    """
    Given an integer x, randomly choose a non-zero addend y between -9 and 9 such that the addition
    x + y does not involve carry or borrow. In other words, the integers x and x + y have the same
    quotient mod 10.

    :param x: the given integer
    :return:
    """
    r = x % 10
    a = random.choice([u for u in range(0, 10) if u != r])
    return a - r


def __extend_simple(a: int, b: int) -> Problem:
    """
    Given a pair of integers (a, b), randomly generate a problem of the form x + a + b or a + b + x by
    prepending or appending a simple addition or subtraction.

    :param a: the first integer
    :param b: the second integer
    :return: Problem
    """
    prepend = __randbool(1 / 2)
    if prepend:
        u = __pick_simple_addend(a, True)
        return Problem(a + u, -u, b)
    else:
        v = __pick_simple_addend(a + b, True)
        return Problem(a, b, v)


def __extend_no_carry_borrow(a: int, b: int) -> Problem:
    """
    Given a pair of integers (a, b), randomly generate a problem of the form x + a + b or a + b + x by
    prepending or appending an addition or subtraction which does not involve carry or borrow.

    :param a: the first integer
    :param b: the second integer
    :return: Problem
    """
    prepend = __randbool(1 / 2)
    if prepend:
        u = __pick_no_carry_borrow_addend(a)
        return Problem(a + u, -u, b)
    else:
        v = __pick_no_carry_borrow_addend(a + b)
        return Problem(a, b, v)


# ============================================================
# Private problem generators.
# ============================================================

def __generate_simple_addition_or_subtraction(is_addition: bool, is_one_digit: bool) -> Problem:
    """
    Randomly generate a 1-digit simple problem using only addition or only subtraction.
    :param is_addition: use addition?
    :param is_one_digit: if yes, all numbers are one-digit numbers.
    :return:
    """
    start = 0 if is_addition else 9
    path = __randpath(start, is_addition)
    indices = random.sample(range(0, len(path)), k=3)
    indices.sort()
    a = path[indices[0]]
    b = path[indices[1]] - a
    c = path[indices[2]] - path[indices[1]]

    if not is_one_digit:
        s = 10 * random.randint(0, 9)
        a = a + s
    return Problem(a, b, c)


def __generate_simple_addition_subtraction(max_value, allow_upper_bead) -> Problem:
    """
    Randomly generate a simple addition/subtraction problem.

    :param max_value: int the maximum number generated (e.g. 9 or 99)
    :param allow_upper_bead: bool Is upper bead movement allowed?
    :return: Problem
    """
    a = random.randint(0, max_value)
    b = __pick_simple_addend(a, allow_upper_bead)
    c = __pick_simple_addend(a + b, allow_upper_bead)
    return Problem(a, b, c)


# Generate problem for a skill of the form +a = -b + 5 or
# -a = +b - 5, where a + b = 5.

def __generate_plus1_eq_minus4_plus5() -> Problem:
    """
    Generate a problem for the skill +1 = -4 + 5.
    :return: Problem
    """
    a = 10 * random.randint(0, 9) + 4
    return __extend_simple(a, 1)


def __generate_minus1_eq_plus4_minus5() -> Problem:
    """
    Generate a problem for the skill -1 = +4 - 5.
    :return: Problem
    """
    a = 10 * random.randint(0, 9) + 5
    return __extend_simple(a, -1)


def __generate_plus2_eq_minus3_plus5() -> Problem:
    """
    Generate a problem for the skill +2 = -3 + 5.
    :return: Problem
    """
    a = 10 * random.randint(0, 9) + random.choice([3, 4])
    return __extend_simple(a, 2)


def __generate_minus2_eq_plus3_minus5() -> Problem:
    """
    Generate a problem for the skill -2 = +3 - 5.
    :return: Problem
    """
    a = 10 * random.randint(0, 9) + random.choice([5, 6])
    return __extend_simple(a, -2)


def __generate_plus3_eq_minus2_plus5() -> Problem:
    """
    Generate a problem for the skill +3 = -2 + 5.
    :return: Problem
    """
    a = 10 * random.randint(0, 9) + random.choice([2, 3, 4])
    return __extend_simple(a, 3)


def __generate_minus3_eq_plus2_minus5() -> Problem:
    """
    Generate a problem for the skill -3 = +2 - 5.
    :return: Problem
    """
    a = 10 * random.randint(0, 9) + random.choice([5, 6, 7])
    return __extend_simple(a, -3)


def __generate_plus4_eq_minus1_plus5() -> Problem:
    """
    Generate a problem for the skill +4 = -1 + 5.
    :return: Problem
    """
    a = 10 * random.randint(0, 9) + random.choice([1, 2, 3, 4])
    return __extend_simple(a, 4)


def __generate_minus4_eq_plus1_minus5() -> Problem:
    """
    Generate a problem for the skill -4 = +1 - 5.
    :return: Problem
    """
    a = 10 * random.randint(0, 9) + random.choice([5, 6, 7, 8])
    return __extend_simple(a, -4)


# ============================================================

def __generate_no_carry_borrow() -> Problem:
    """
    Generate a problem which does not involve carry or brrow.
    :return: Problem
    """
    a = 10 * random.randint(0, 9)
    x = random.randint(0, 9)
    y = __pick_no_carry_borrow_addend(x)
    z = __pick_no_carry_borrow_addend(x + y)
    return Problem(a + x, y, z)


# ============================================================


def __generate_plus1_eq_minus9_plus10() -> Problem:
    """
    Generate a problem for the skill +1 = -9 + 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no49) + 9
    return __extend_no_carry_borrow(a, 1)


def __generate_minus1_eq_plus9_minus10() -> Problem:
    """
    Generate a problem for the skill -1 = +9 - 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no05)
    return __extend_no_carry_borrow(a, -1)


def __generate_plus2_eq_minus8_plus10() -> Problem:
    """
    Generate a problem for the skill +2 = -8 + 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no49) + random.choice([8, 9])
    return __extend_no_carry_borrow(a, 2)


def __generate_minus2_eq_plus8_minus10() -> Problem:
    """
    Generate a problem for the skill -2 = +8 - 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no05) + random.choice([0, 1])
    return __extend_no_carry_borrow(a, -2)


def __generate_plus3_eq_minus7_plus10() -> Problem:
    """
    Generate a problem for the skill +3 = -7 + 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no49) + random.choice([7, 8, 9])
    return __extend_no_carry_borrow(a, 3)


def __generate_minus3_eq_plus7_minus10() -> Problem:
    """
    Generate a problem for the skill -3 = +7 - 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no05) + random.choice([0, 1, 2])
    return __extend_no_carry_borrow(a, -3)


def __generate_plus4_eq_minus6_plus10() -> Problem:
    """
    Generate a problem for the skill +4 = -6 + 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no49) + random.choice([6, 7, 8, 9])
    return __extend_no_carry_borrow(a, 4)


def __generate_minus4_eq_plus6_minus10() -> Problem:
    """
    Generate a problem for the skill -4 = +6 - 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no05) + random.choice([0, 1, 2, 3])
    return __extend_no_carry_borrow(a, -4)


def __generate_plus5_eq_minus5_plus10() -> Problem:
    """
    Generate a problem for the skill +5 = -5 + 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no49) + random.choice([5, 6, 7, 8, 9])
    return __extend_no_carry_borrow(a, 5)


def __generate_minus5_eq_plus5_minus10() -> Problem:
    """
    Generate a problem for the skill -5 = +5 - 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no05) + random.choice([0, 1, 2, 3, 4])
    return __extend_no_carry_borrow(a, -5)


def __generate_plus6_eq_minus4_plus10() -> Problem:
    """
    Generate a problem for the skill +6 = -4 + 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no49) + random.choice([4, 9])
    return __extend_no_carry_borrow(a, 6)


def __generate_minus6_eq_plus4_minus10() -> Problem:
    """
    Generate a problem for the skill -6 = +4 - 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no05) + random.choice([0, 5])
    return __extend_no_carry_borrow(a, -6)


def __generate_plus7_eq_minus3_plus10() -> Problem:
    """
    Generate a problem for the skill +7 = -3 + 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no49) + random.choice([3, 4, 8, 9])
    return __extend_no_carry_borrow(a, 7)


def __generate_minus7_eq_plus3_minus10() -> Problem:
    """
    Generate a problem for the skill -7 = +3 - 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no05) + random.choice([0, 1, 5, 6])
    return __extend_no_carry_borrow(a, -7)


def __generate_plus8_eq_minus2_plus10() -> Problem:
    """
    Generate a problem for the skill +8 = -2 + 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no49) + random.choice([2, 3, 4, 7, 8, 9])
    return __extend_no_carry_borrow(a, 8)


def __generate_minus8_eq_plus2_minus10() -> Problem:
    """
    Generate a problem for the skill -8 = +2 - 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no05) + random.choice([0, 1, 2, 5, 6, 7])
    return __extend_no_carry_borrow(a, -8)


def __generate_plus9_eq_minus1_plus10() -> Problem:
    """
    Generate a problem for the skill +9 = -1 + 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no49) + random.choice([1, 2, 3, 4, 6, 7, 8, 9])
    return __extend_no_carry_borrow(a, 9)


def __generate_minus9_eq_plus1_minus10() -> Problem:
    """
    Generate a problem for the skill -9 = +1 - 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no05) + random.choice([0, 1, 2, 3, 5, 6, 7, 8])
    return __extend_no_carry_borrow(a, -9)


# ============================================================


def __generate_plus6_eq_plus1_minus5_plus10() -> Problem:
    """
    Generate a problem for the skill +6 = +1 - 5 + 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no49) + random.choice([5, 6, 7, 8])
    return __extend_no_carry_borrow(a, 6)


def __generate_minus6_eq_minus1_plus5_minus10() -> Problem:
    """
    Generate a problem for the skill -6 = -1 + 5 - 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no05) + random.choice([1, 2, 3, 4])
    return __extend_no_carry_borrow(a, -6)

def __generate_plus7_eq_plus2_minus5_plus10() -> Problem:
    """
    Generate a problem for the skill +7 = +2 - 5 + 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no49) + random.choice([5, 6, 7])
    return __extend_no_carry_borrow(a, 7)


def __generate_minus7_eq_minus2_plus5_minus10() -> Problem:
    """
    Generate a problem for the skill -7 = -2 + 5 - 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no05) + random.choice([2, 3, 4])
    return __extend_no_carry_borrow(a, -7)


def __generate_plus8_eq_plus3_minus5_plus10() -> Problem:
    """
    Generate a problem for the skill +8 = +3 - 5 + 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no49) + random.choice([5, 6])
    return __extend_no_carry_borrow(a, 8)


def __generate_minus8_eq_minus3_plus5_minus10() -> Problem:
    """
    Generate a problem for the skill -8 = -3 + 5 - 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no05) + random.choice([3, 4])
    return __extend_no_carry_borrow(a, -8)


def __generate_plus9_eq_plus4_minus5_plus10() -> Problem:
    """
    Generate a problem for the skill +9 = +4 - 5 + 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no49) + random.choice([5])
    return __extend_no_carry_borrow(a, 9)


def __generate_minus9_eq_minus4_plus5_minus10() -> Problem:
    """
    Generate a problem for the skill -9 = -4 + 5 - 10.
    :return: Problem
    """
    a = 10 * random.choice(__digits_no05) + random.choice([4])
    return __extend_no_carry_borrow(a, -9)

# ============================================================

def __generate_from_4x_to_5x() -> Problem:
    """
    Generate a problem which involves an addition a + x = b,
    where 41 <= a <= 49, 1 <= x <= 9, and 50 <= b <= 59.
    :return:
    """
    a = random.choice(range(41, 50))
    b = random.choice(range(50, a+10))
    return __extend_no_carry_borrow(a, b - a)

# ============================================================
# Public skills to be accessed by the Steps module.
# ============================================================

one_digit_simple_addition = Skill(
    "One-digit simple addition",
    lambda: __generate_simple_addition_or_subtraction(True, True))
one_digit_simple_subtraction = Skill(
    "One-digit simple subtraction",
    lambda: __generate_simple_addition_or_subtraction(False, True))
one_digit_addition_or_subtraction_lower_bead_only = Skill(
    "One-digit simple addition or subtraction (lower bead only)",
    lambda: __generate_simple_addition_subtraction(9, False))
one_digit_addition_or_subtraction_allow_upper_bead = Skill(
    "One-digit simple addition or subtraction (allow upper bead)",
    lambda: __generate_simple_addition_subtraction(9, True))

simple_addition = Skill(
    "Simple addition",
    lambda: __generate_simple_addition_or_subtraction(True, False))
simple_subtraction = Skill(
    "Simple subtraction",
    lambda: __generate_simple_addition_or_subtraction(False, False))
simple_addition_or_subtraction_lower_bead_only = Skill(
    "Simple addition or subtraction (lower bead only)",
    lambda: __generate_simple_addition_subtraction(99, False))
simple_addition_or_subtraction_allow_upper_bead = Skill(
    "Simple addition or subtraction (allow upper bead)",
    lambda: __generate_simple_addition_subtraction(99, True))

plus1_eq_minus4_plus5 = Skill("+1 = -4 + 5", __generate_plus1_eq_minus4_plus5)
minus1_eq_plus4_minus5 = Skill("-1 = +4 - 5", __generate_minus1_eq_plus4_minus5)
plus2_eq_minus3_plus5 = Skill("+2 = -3 + 5", __generate_plus2_eq_minus3_plus5)
minus2_eq_plus3_minus5 = Skill("-2 = +3 - 5", __generate_minus2_eq_plus3_minus5)
plus3_eq_minus2_plus5 = Skill("+3 = -2 + 5", __generate_plus3_eq_minus2_plus5)
minus3_eq_plus2_minus5 = Skill("-3 = +2 - 5", __generate_minus3_eq_plus2_minus5)
plus4_eq_minus1_plus5 = Skill("+4 = -1 + 5", __generate_plus4_eq_minus1_plus5)
minus4_eq_plus1_minus5 = Skill("-4 = +1 - 5", __generate_minus4_eq_plus1_minus5)

no_carry_borrow = Skill("No carry or borrow", __generate_no_carry_borrow)

plus1_eq_minus9_plus10 = Skill("+1 = -9 + 10", __generate_plus1_eq_minus9_plus10)
minus1_eq_plus9_minus10 = Skill("-1 = +9 - 10", __generate_minus1_eq_plus9_minus10)
plus2_eq_minus8_plus10 = Skill("+2 = -8 + 10", __generate_plus2_eq_minus8_plus10)
minus2_eq_plus8_minus10 = Skill("-2 = +8 - 10", __generate_minus2_eq_plus8_minus10)
plus3_eq_minus7_plus10 = Skill("+3 = -7 + 10", __generate_plus3_eq_minus7_plus10)
minus3_eq_plus7_minus10 = Skill("-3 = +7 - 10", __generate_minus3_eq_plus7_minus10)
plus4_eq_minus6_plus10 = Skill("+4 = -6 + 10", __generate_plus4_eq_minus6_plus10)
minus4_eq_plus6_minus10 = Skill("-4 = +6 - 10", __generate_minus4_eq_plus6_minus10)

plus5_eq_minus5_plus10 = Skill("+5 = -5 + 10", __generate_plus5_eq_minus5_plus10)
minus5_eq_plus5_minus10 = Skill("-5 = +5 - 10", __generate_minus5_eq_plus5_minus10)
plus6_eq_minus4_plus10 = Skill("+6 = -4 + 10", __generate_plus6_eq_minus4_plus10)
minus6_eq_plus4_minus10 = Skill("-6 = +4 - 10", __generate_minus6_eq_plus4_minus10)
plus7_eq_minus3_plus10 = Skill("+7 = -3 + 10", __generate_plus7_eq_minus3_plus10)
minus7_eq_plus3_minus10 = Skill("-7 = +3 - 10", __generate_minus7_eq_plus3_minus10)
plus8_eq_minus2_plus10 = Skill("+8 = -2 + 10", __generate_plus8_eq_minus2_plus10)
minus8_eq_plus2_minus10 = Skill("-8 = +2 - 10", __generate_minus8_eq_plus2_minus10)
plus9_eq_minus1_plus10 = Skill("+9 = -1 + 10", __generate_plus9_eq_minus1_plus10)
minus9_eq_plus1_minus10 = Skill("-9 = +1 - 10", __generate_minus9_eq_plus1_minus10)

plus6_eq_plus1_minus5_plus10 = Skill("+6 = +1 - 5 + 10", __generate_plus6_eq_plus1_minus5_plus10)
minus6_eq_minus1_plus5_minus10 = Skill("-6 = -1 + 5 - 10", __generate_minus6_eq_minus1_plus5_minus10)
plus7_eq_plus2_minus5_plus10 = Skill("+7 = +2 - 5 + 10", __generate_plus7_eq_plus2_minus5_plus10)
minus7_eq_minus2_plus5_minus10 = Skill("-7 = -2 + 5 - 10", __generate_minus7_eq_minus2_plus5_minus10)
plus8_eq_plus3_minus5_plus10 = Skill("+8 = +3 - 5 + 10", __generate_plus8_eq_plus3_minus5_plus10)
minus8_eq_minus3_plus5_minus10 = Skill("-8 = -3 + 5 - 10", __generate_minus8_eq_minus3_plus5_minus10)
plus9_eq_plus4_minus5_plus10 = Skill("+9 = +4 - 5 + 10", __generate_plus9_eq_plus4_minus5_plus10)
minus9_eq_minus4_plus5_minus10 = Skill("-9 = -4 + 5 - 10", __generate_minus9_eq_minus4_plus5_minus10)

from_4x_to_5x = Skill("From 4x to 5x", __generate_from_4x_to_5x)
