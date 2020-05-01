import random
from typing import Callable


class Problem:
    """This is a class for problem. A problem is a triple of integers (a, b, c) which represents a + b + c.
    """

    def __init__(self, a: int, b: int, c: int):
        """Constructor.
        """
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self) -> int:
        return self.__a

    @property
    def b(self) -> int:
        return self.__b

    @property
    def c(self) -> int:
        return self.__c

    def __eq__(self, other) -> bool:
        if not isinstance(other, Problem):
            return NotImplemented

        return self.__a == other.__a and self.__b == other.__b and self.__c == other.__c

    def __hash__(self):
        return hash((self.__a, self.__b, self.__c))


class Skill:
    """This is a class for a skill. A skill comes with a description and a sample method which
    randomly picks a problem of the current skill. For example, the skill "+2 = -3 + 5" may
    have a sample problem (14, 2, -1) which represents 14 + 2 - 1.
    """

    def __init__(self, description: str, do_sample: Callable[[], Problem]):
        """Constructor.

        Arguments:
            description {str}
                a description of the skill
            do_sample {str}
                the sampling function
        """
        self.description = description
        self.__do_sample = do_sample

    def sample(self) -> Problem:
        """Randomly picks a sample problem of the current skill.

        Returns: {Problem}
            a problem of the form a + b + c.
        """
        return self.__do_sample()


class Step:
    """This is a class for a step. A step is a tuple of skills.
    """

    def __init__(self, *skills: Skill):
        """Constructor.

        Arguments:
            skills {tuple of Skill}
                a tuple of Skill objects
        """
        self.__skills = skills
        self.__description = ''

    def with_description(self, description: str):
        """Set the description of this step and return this instance.
        """
        self.__description = description
        return self

    def description(self) -> str:
        """Getter of a description of this step.
        """
        s = ', '.join([s.description for s in self.__skills])
        return self.__description if isinstance(self.__description, str) and len(self.__description) > 0 else s

    def sample(self) -> Problem:
        """Randomly samples a problem using the underlying skills.

        Returns: {Problem}
            a problem of the form a + b + c.
        """
        return random.choice(self.__skills).sample()


