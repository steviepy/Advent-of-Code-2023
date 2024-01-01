from typing import List, Set


def position_adjacent_to_symbol(
    current_row: int, current_column: int, symbol_locations: Set[tuple[int, int]]
):
    for row in range(current_row - 1, current_row + 2):
        for column in range(current_column - 1, current_column + 2):
            if (row, column) in symbol_locations:
                print(current_row, current_column, row, column, True)
                return True
            print(current_row, current_column, row, column, False)
    return False


def sum_of_part_numbers(puzzle_lines: List[str]) -> int:
    symbol_locations = set()
    part_numbers = []

    # Build list of symbol locations
    row = 0
    for puzzle_line in puzzle_lines:
        row += 1
        column = 0
        for char in puzzle_line:
            column += 1
            if all([char != ".", not char.isnumeric(), char.isprintable()]):
                symbol_locations.add((row, column))

    # Construct list of part numbers that are adjacent to a symbol
    row = 0
    for puzzle_line in puzzle_lines:
        part_number = ""
        adjacent_to_symbol = False
        row += 1
        column = 0
        for char in puzzle_line:
            column += 1
            if char.isdecimal():
                # Build part number
                part_number += str(char)
                if position_adjacent_to_symbol(row, column, symbol_locations):
                    adjacent_to_symbol = True
            else:
                # No decimal at current location
                if part_number != "":
                    # Append detected part number, if adjacent to symbol
                    if adjacent_to_symbol:
                        print(f"Desired part number: {part_number}")
                        part_numbers.append(int(part_number))
                    else:
                        print(f"Undesired part number: {part_number}")
                    part_number = ""
                adjacent_to_symbol = False
    print(part_numbers)
    return sum(part_numbers)


def main():
    with open("puzzle_input_03.txt", "r", encoding="utf-8") as puzzle_input:
        puzzle_lines = puzzle_input.readlines()
    sum_of_all_part_numbers = sum_of_part_numbers(puzzle_lines)
    print("Sum of all desired part numbers: ", sum_of_all_part_numbers)


if __name__ == "__main__":
    main()
