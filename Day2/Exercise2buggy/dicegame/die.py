import random


class Die:
    """
    This is always correct. Seriously, look away.
    """

    def __init__(self):
        self.roll()

    def roll(self):
        self.value = int(random.random() * 6 + 1)

    def show(self):
        if self.value == 1:
            return("---------\n|       |\n|   *   |\n|       |\n---------")
        elif self.value == 2:
            return("---------\n|*      |\n|       |\n|      *|\n---------")
        elif self.value == 3:
            return("---------\n|*      |\n|   *   |\n|      *|\n---------")
        elif self.value == 4:
            return("---------\n|*     *|\n|       |\n|*     *|\n---------")
        elif self.value == 5:
            return("---------\n|*     *|\n|   *   |\n|*     *|\n---------")
        else:
            return("---------\n|*     *|\n|*     *|\n|*     *|\n---------")

    @classmethod
    def create_dice(cls, n):
        return [cls() for _ in range(n)]
    
# Took away the roll(dice) function since it didn't do anything
# Didn't change Die, since it was always correct
# Added a line to break the code when I didn't want to play any more
# Generally made it a bite nicer