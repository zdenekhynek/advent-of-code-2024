import os

test_input = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

def get_columns(input_txt):
  lines = input_txt.strip().splitlines()
  digits = [tuple(map(int, line.split())) for line in lines]
  return zip(*digits)

# Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.


def match_pairs(list1, list2):
    sort_list1, sort_list2 = [sorted(l) for l in [list1, list2]]
    return [[sort_list1[i], sort_list2[i]] for i in range(len(sort_list1))]


# Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.


def get_pair_distance(l):
    return abs(l[1] - l[0])


def get_day_1_part_1_answer(input_txt):
    columns = get_columns(input_txt)
    pairs = match_pairs(*columns)
    distances = [ get_pair_distance(pair) for pair in pairs]
    return sum(distances)
    
def get_numbers_multiplier(list1, list2):
    return [list2.count(l1) for l1 in list1]
    
def get_day_1_part_2_answer(input_txt):
    columns = get_columns(input_txt)
    list1, list2 = columns
    multipliers = get_numbers_multiplier(list1, list2)
    multipled = [v * multipliers[i] for i, v in enumerate(list1)]
    return sum(multipled)

if __name__ == "__main__":
    # PART 1
    working_dir = os.path.dirname(os.path.abspath(__file__))
    input_text = open(f"{working_dir}/day_1_input.txt").read()
    print(f"Part 1: {get_day_1_part_1_answer(input_text)}")

    # PART 2 = 
    print(f"Part 2: {get_day_1_part_2_answer(input_text)} ")
