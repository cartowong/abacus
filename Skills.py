import random

from Core import Problem, Skill


# ============================================================
# Private utility functions.
# ============================================================

def __pick_simple_addend(x, allow_upper_bead):
    """
    Given an integer x, randomly choose a simple, non-zero addend y between -9 and 9. By simple,
    we mean the addition or subtraction only involves moving lower beads, and perhaps also moving
    one upper bead in the same rod in the opposite direction. For example, a simple "+7" involves
    moving two lower beads up and one upper bead down.

    :param allow_upper_bead: bool allow upper bead movement (in the opposite direction)?
    :return: Problem
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


def __randbool(p):
    """
    Bernoulli random variable.

    :param p: float the probability of True
    :return: bool
    """
    return random.random() < p


def __randproblem(a, b):
    """
    Given a pair of integers (a, b), randomly generate a problem of the form x + a + b or a + b + x by
    prepending or appending a simple addition or subtraction.

    :param a: int the first integer
    :param b: int the second integer
    :return: Problem
    """
    prepend = __randbool(1 / 2)
    if prepend:
        u = __pick_simple_addend(a, True)
        return Problem(a + u, -u, b)
    else:
        v = __pick_simple_addend(a + b, True)
        return Problem(a, b, v)


# ============================================================
# Private problem generators.
# ============================================================

def __generate_simple_addition_subtraction(allow_upper_bead):
    """
    Randomly generate a simple addition/subtraction problem.

    :param allow_upper_bead: bool Is upper bead movement allowed?
    :return: Problem
    """
    a = random.randint(0, 99)
    b = __pick_simple_addend(a, allow_upper_bead)
    c = __pick_simple_addend(a + b, allow_upper_bead)
    return Problem(a, b, c)


# Generate problem for a skill of the form +a = -b + 5 or
# -a = +b - 5, where a + b = 5.

def __generate_plus1_eq_minus4_plus5():
    """
    Generate a problem for the skill +1 = -4 + 5.
    :return: Problem
    """
    a = 10 * random.randint(0, 9) + random.choices([4])[0]
    return __randproblem(a, 1)


def __generate_minus1_eq_plus4_minus5():
    """
    Generate a problem for the skill -1 = +4 - 5.
    :return: Problem
    """
    a = 10 * random.randint(0, 9) + random.choices([5])[0]
    return __randproblem(a, -1)


def __generate_plus2_eq_minus3_plus5():
    """
    Generate a problem for the skill +2 = -3 + 5.
    :return: Problem
    """
    a = 10 * random.randint(0, 9) + random.choices([3, 4])[0]
    return __randproblem(a, 2)


def __generate_minus2_eq_plus3_minus5():
    """
    Generate a problem for the skill -2 = +3 - 5.
    :return: Problem
    """
    a = 10 * random.randint(0, 9) + random.choices([5, 6])[0]
    return __randproblem(a, -2)


def __generate_plus3_eq_minus2_plus5():
    """
    Generate a problem for the skill +3 = -2 + 5.
    :return: Problem
    """
    a = 10 * random.randint(0, 9) + random.choices([2, 3, 4])[0]
    return __randproblem(a, 3)


def __generate_minus3_eq_plus2_minus5():
    """
    Generate a problem for the skill -3 = +2 - 5.
    :return: Problem
    """
    a = 10 * random.randint(0, 9) + random.choices([5, 6, 7])[0]
    return __randproblem(a, -3)


def __generate_plus4_eq_minus1_plus5():
    """
    Generate a problem for the skill +4 = -1 + 5.
    :return: Problem
    """
    a = 10 * random.randint(0, 9) + random.choices([1, 2, 3, 4])[0]
    return __randproblem(a, 4)


def __generate_minus4_eq_plus1_minus5():
    """
    Generate a problem for the skill -4 = +1 - 5.
    :return: Problem
    """
    a = 10 * random.randint(0, 9) + random.choices([5, 6, 7, 8])[0]
    return __randproblem(a, -4)


# ============================================================

def __generate_no_carry_borrow():
    """
    Generate a problem which does not involve carry or brrow.
    :return: Problem
    """
    a = 10 * random.randint(0, 9)
    x = random.randint(0, 9)
    y = random.choices([u for u in range(0, 9) if u != x])[0]
    z = random.choices([u for u in range(0, 9) if u != y])[0]
    return Problem(a + x, y - x, z - y)


# ============================================================
# Public skills to be accessed by the Steps module.
# ============================================================

simple_addition_or_subtraction = Skill("Simple addition or subtraction",
                                       lambda: __generate_simple_addition_subtraction(False))
simple_addition_or_subtraction_allow_upper_bead = Skill("Simple addition or subtraction (allow upper bead)",
                                                        lambda: __generate_simple_addition_subtraction(True))
plus1_eq_minus4_plus5 = Skill("+1 = -4 + 5", __generate_plus1_eq_minus4_plus5)
minus1_eq_plus4_minus5 = Skill("-1 = +4 - 5", __generate_minus1_eq_plus4_minus5)
plus2_eq_minus3_plus5 = Skill("+2 = -3 + 5", __generate_plus2_eq_minus3_plus5)
minus2_eq_plus3_minus5 = Skill("-2 = +3 - 5", __generate_minus2_eq_plus3_minus5)
plus3_eq_minus2_plus5 = Skill("+3 = -2 + 5", __generate_plus3_eq_minus2_plus5)
minus3_eq_plus2_minus5 = Skill("-3 = +2 - 5", __generate_minus3_eq_plus2_minus5)
plus4_eq_minus1_plus5 = Skill("+4 = -1 + 5", __generate_plus4_eq_minus1_plus5)
minus4_eq_plus1_minus5 = Skill("-4 = +1 - 5", __generate_minus4_eq_plus1_minus5)

no_carry_borrow = Skill("No carry or borrow", __generate_no_carry_borrow)


