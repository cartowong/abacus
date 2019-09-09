import random


class Skill:
    """
    This is a class for a skill. A skill comes with a description and a sample method which
    randomly picks a problem of the current skill. For example, the skill "+2 = -3 + 5" may
    have a sample problem (14, 2, -1) which represents 14 + 2 - 1.
    """

    def __init__(self, description, do_sample):
        """
        Constructor.

        :param description: str a description of the skill
        :param do_sample: callable the sampling function
        """
        self.description = description
        self.__do_sample = do_sample

    def sample(self):
        """
        Randomly picks a sample problem of the current skill.

        :return: Tuple(int) a triple of integers (a, b, c) representing the problem a + b + c.
        """
        return self.__do_sample()


class Step:
    """
    This is a class for a step. A step is a tuple of skills.
    """

    def __init__(self, *skills):
        """
        Constructor.

        :param skills: Tuple(Skill) a tuple of Skill objects
        """
        self.__skills = skills
        self.__description = ''

    def with_description(self, description):
        """
        Set the description of this step and return this instance.
        :return: Step
        """
        self.__description = description
        return self

    def description(self):
        """
        Getter of a description of this step.

        :return: string
        """
        s = ', '.join([s.description for s in self.__skills])
        return self.__description if isinstance(self.__description, str) and len(self.__description) > 0 else s

    def sample(self):
        """
        Randomly samples a problem using the underlying skills.

        :return: Tuple(int) a triple of integers (a, b, c) representing the problem a + b + c.
        """
        return random.choice(self.__skills).sample()


class Problem:
    """
    This is a class for problem. A problem is a triple of integers (a, b, c) which represents a + b + c.
    """

    def __init__(self, a, b, c):
        """
        Constructor.

        :param numbers: int a
        :param numbers: int b
        :param numbers: int c
        """
        self.__a = a
        self.__b = b
        self.__c = c

    def a(self):
        """
        Getter for a.
        :return: int
        """
        return self.__a

    def b(self):
        """
        Getter for b.
        :return: int
        """
        return self.__b

    def c(self):
        """
        Getter for c.
        :return: int
        """
        return self.__c
