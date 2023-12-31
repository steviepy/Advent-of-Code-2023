from typing import List


def find_decimals(string: str) -> List[int]:
    decimals = []
    for character in string:
        if character.isdecimal():
            decimals.append(int(character))
    return decimals


def sum_of_calibration_values(lines: List[str]) -> int:
    total = 0
    for line in lines:
        line_digits = find_decimals(line.strip())
        calibration_value = int(f"{line_digits[0]}{line_digits[-1]}")
        total += calibration_value
    return total


def main():
    calibration_document = "puzzle_input.txt"
    with open(calibration_document, "r", encoding="utf-8") as wrapper:
        lines = wrapper.readlines()
    print(f"Sum of calibration values: {sum_of_calibration_values(lines)}")


if __name__ == "__main__":
    main()
