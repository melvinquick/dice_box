from secrets import choice
from sys import exit


class DiceRoller:
    def __init__(self):
        pass

    def roll(self, num_sides=6, num_dice=1):
        die_counter = 0
        rolls = []

        while die_counter < num_dice:
            rolls.append(choice(range(1, num_sides + 1)))
            die_counter += 1

        sum_of_rolls = self.sum_of_rolled_dice(rolls)
        count_of_evens, count_of_odds = self.even_odd_count(rolls)
        sum_of_evens, sum_of_odds = self.even_odd_sums(rolls)

        return (
            rolls,
            sum_of_rolls,
            count_of_evens,
            count_of_odds,
            sum_of_evens,
            sum_of_odds,
        )

    def sum_of_rolled_dice(self, rolls):
        sum_of_rolls = 0

        for roll in rolls:
            sum_of_rolls += roll

        return sum_of_rolls

    def even_odd_count(self, rolls):
        count_of_evens = 0
        count_of_odds = 0

        for roll in rolls:
            if roll % 2 == 0:
                count_of_evens += 1
            else:
                count_of_odds += 1

        return count_of_evens, count_of_odds

    def even_odd_sums(self, rolls):
        sum_of_evens = 0
        sum_of_odds = 0

        for roll in rolls:
            if roll % 2 == 0:
                sum_of_evens += roll
            else:
                sum_of_odds += roll

        return sum_of_evens, sum_of_odds


def line_spacer():
    print("")


def main():
    try:
        num_sides = int(
            input("How many sides should your die have (e.g. 1, 2, ..., N): ")
        )
        num_dice = int(
            input("How many die would you like to roll (e.g. 1, 2, ..., N): ")
        )
    except Exception:
        line_spacer()
        print(
            "You entered an incorrect value. Please only enter non-zero, positive, integer values for the number of sides and the number of die!"
        )
        exit(1)

    roller = DiceRoller()
    rolls, sum_of_rolls, count_of_evens, count_of_odds, sum_of_evens, sum_of_odds = (
        roller.roll(num_sides=num_sides, num_dice=num_dice)
    )
    line_spacer()
    print(f"Rolls: {', '.join(map(str, rolls))}")
    print(f"Sum of Rolls: {sum_of_rolls}")
    print(f"Count of Evens Rolled: {count_of_evens}")
    print(f"Count of Odds Rolled: {count_of_odds}")
    print(f"Sum of Evens Rolled: {sum_of_evens}")
    print(f"Sum of Odds Rolled: {sum_of_odds}")


if __name__ == "__main__":
    main()
