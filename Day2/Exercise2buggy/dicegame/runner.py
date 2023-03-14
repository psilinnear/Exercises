from .die import Die

class GameRunner:

    def __init__(self):
        self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(cls):
        # Counts consecutive wins
        consecutive_wins = 0
        
        runner = cls()
        
        while True:
            runner.dice = Die.create_dice(1)

            print("Round {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())

            guess = input("What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, well done!")
                runner.wins += 1
                consecutive_wins += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                runner.loses += 1
                consecutive_wins = 0
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            
            runner.round += 1

            if consecutive_wins == 6:
                print("You won. Congratulations!")
                break

            prompt = input("Would you like to play again?[Y/n]: ")
            if prompt.lower() == 'n':
                break
# Took away the exception thing, it didn't do anything.
# Changed the answer function to actually add all the die
# Changed c to wins, because it should break after 6 wins
# Changed so that it actually counted the wins, losses and rounds instead of resetting all the time
