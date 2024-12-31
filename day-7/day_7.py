import os
from itertools import product

test_input = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


def get_rows(input_txt):
    rows = [line.split(": ") for line in input_txt.strip().splitlines()]
    return [{"test": int(test), "digits": tuple(map(int, digits.split()))} for test, digits in rows]


def get_all_variations(digits, operators="+*"):
    # 2: ++, *+, *+, ** - 4
    # 3: +++, *++, +*+, ++*, **+, +**, *-*, *** - 8
    # 4: ++++, *+++, +*++, ++*+, +++*, **++, +**+, ++**, +***, ***+, ****
    variations = tuple(product(operators, repeat=len(digits) - 1))
    return variations


def apply_eq(digits, varition):
    sum = digits[0]

    for i in range(len(digits) - 1):
        d = digits[i + 1]
        v = varition[i]
        if v == "*":
            sum *= d
        elif v == "|":
            sum = int(f"{sum}{d}")
        else:
            sum += d
        
    return sum


def is_equation(row, operators="+*"):
    test, digits = row.values()
    all_combinations = get_all_variations(digits, operators)

    found_solution = False
    for combination in all_combinations:
        if apply_eq(digits, combination) == test:
            found_solution = True
            break

    return found_solution


def get_truth_sum(input_txt, operators="+*"):
    rows = get_rows(input_txt)
    true_tests = [row["test"] for row in rows if is_equation(row, operators)]
    return sum(true_tests)


if __name__ == "__main__":
    # PART 1
    working_dir = os.path.dirname(os.path.abspath(__file__))
    input_text = open(f"{working_dir}/day_7_input.txt").read()
    print(f"Part 1: {get_truth_sum(input_text)}")

    # PART 2 =
    part2_result = get_truth_sum(input_text, "+*|")
    print(f"Part 2: {part2_result}")
