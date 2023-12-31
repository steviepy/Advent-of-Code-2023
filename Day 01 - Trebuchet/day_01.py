from typing import List


def find_digits(string: str) -> List[int]:
    digits = []
    for character in string:
        if character.isdigit():
            digits.append(int(character))
    return digits


def sum_of_calibration_values(lines: List[str]) -> int:
    total = 0
    for line in lines:
        line_digits = find_digits(line.strip())
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
