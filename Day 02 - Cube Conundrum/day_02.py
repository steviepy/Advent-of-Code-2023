from typing import List


def get_max_n_game_cubes(game_cubes: str) -> bool:
    n_colors_found = {"red": 0, "green": 0, "blue": 0}
    subsets_of_cubes = game_cubes.split(";")
    for subset_of_cubes in subsets_of_cubes:
        for handful_of_cubes in subset_of_cubes.split(","):
            number = int(handful_of_cubes.strip().split(" ")[0])
            color = handful_of_cubes.strip().split(" ")[1]
            if number > n_colors_found[color]:
                n_colors_found[color] = number
    if all(
        [
            n_colors_found["red"] <= 12,
            n_colors_found["green"] <= 13,
            n_colors_found["blue"] <= 14,
        ]
    ):
        return True
    return False


def analyze_game(game_data: str) -> int:
    game_id = int(game_data.strip().split(":")[0].split(" ")[1])
    game_cubes = game_data.split(":")[1]
    if get_max_n_game_cubes(game_cubes):
        return game_id
    return 0


def analyze_games(games: List[str]) -> int:
    sum_of_ids = 0
    for game in games:
        id = analyze_game(game)
        sum_of_ids += id
    return sum_of_ids


def main():
    with open("puzzle_input_02.txt", "r", encoding="utf-8") as puzzle_input:
        games = puzzle_input.readlines()
    sum_of_ids = analyze_games(games)
    print(f"Sum of game IDs: {sum_of_ids}")


if __name__ == "__main__":
    main()
