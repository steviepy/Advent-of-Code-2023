import re
from math import exp2
from typing import List


def calculate_card_points(matches: int) -> int:
    if matches <= 0:
        return 0
    return int(exp2(matches - 1))


def calculate_points(cards: List[str]) -> int:
    points = 0
    for card in cards:
        matches = 0
        winning_numbers = re.split(r"\s+", card.split(":")[1].split("|")[0].strip())
        numbers_you_have = re.split(r"\s+", card.split("|")[1].strip())
        for number in numbers_you_have:
            if number in winning_numbers:
                matches += 1
        card_points = calculate_card_points(matches)
        points += card_points
    return points


def main():
    with open("puzzle_input_04.txt", "r", encoding="utf-8") as puzzle_input:
        cards = puzzle_input.readlines()
    points = calculate_points(cards)
    print(f"Points of all cards: {points}")


if __name__ == "__main__":
    main()
