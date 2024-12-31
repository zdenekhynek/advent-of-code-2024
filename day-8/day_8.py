import os

test_input = """
..........
..........
..........
....a.....
..........
.....a....
..........
..........
..........
..........
"""

test_input2 = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

test_input3 = """
T.........
...T......
.T........
..........
..........
..........
..........
..........
..........
..........
"""


def get_grid(input: str) -> list:
    return [line for line in input.splitlines() if line != ""]


def is_coords_in_grid(grid, row, col):
    return row > -1 and row < len(grid) and col > -1 and col < len(grid[row])


def get_antennas(grid, empty_space="."):
    antennas = []
    for row_idx, _ in enumerate(grid):
        for cell_idx, cell in enumerate(grid[row_idx]):
            if cell != empty_space:
                antennas.append((cell_idx, row_idx))
    return antennas


def place_antidotes(grid, antennas, any_distance=False):
    antidotes = []
    for a1 in antennas:
        for a2 in antennas:
            # do not compare the same antennas
            if a1 == a2:
                continue

            # are we comparing the same letters
            if grid[a1[1]][a1[0]] != grid[a2[1]][a2[0]]:
                continue

            dx = a2[0] - a1[0]
            dy = a2[1] - a1[1]

            if not any_distance:
                # part 1
                candidate1 = (a1[0] - dx, a1[1] - dy)
                candidate2 = (a2[0] + dx, a2[1] + dy)

                if is_coords_in_grid(grid, candidate1[0], candidate1[1]):
                    antidotes.append(candidate1)
                if is_coords_in_grid(grid, candidate2[0], candidate2[1]):
                    antidotes.append(candidate2)
            else:
                # part 2

                # for each antenna go in the direction away from the antenna
                # and place an antidote
                c1 = (a1[0], a1[1])
                new_antidotes = []

                while c1 is not None:
                    if is_coords_in_grid(grid, c1[0], c1[1]):
                        new_antidotes.append(c1)
                        c1 = (c1[0] - dx, c1[1] - dy)
                    else:
                        c1 = None

                antidotes += new_antidotes
                pass
    return antidotes


def get_unique_antidotes(input_txt, any_distance=False):
    grid = get_grid(input_txt)

    antennas = get_antennas(grid)
    antidotes = place_antidotes(grid, antennas, any_distance)

    unique_antidotes = list(set(antidotes))
    return unique_antidotes


if __name__ == "__main__":
    # PART 1
    working_dir = os.path.dirname(os.path.abspath(__file__))
    input_text = open(f"{working_dir}/day_8_input.txt").read()
    unique_antidotes = get_unique_antidotes(input_text)
    print(f"Part 1: {len(unique_antidotes)}")

    unique_antidotes_any_distance = get_unique_antidotes(input_text, True)
    print(f"Part 2: {len(unique_antidotes_any_distance)}")
