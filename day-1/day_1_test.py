from day_1 import (
    get_columns,
    match_pairs,
    get_pair_distance,
    get_day_1_part_1_answer,
    test_input,
    get_numbers_multiplier,
    get_day_1_part_2_answer,
)


def test_get_columns():
    columns = list(get_columns(test_input))
    assert len(columns) == 2
    assert len(columns[0]) == 6
    assert columns[0][0] == 3


def test_match_pairs():
    columns = get_columns(test_input)
    result = match_pairs(*columns)
    assert len(result) == 6
    assert result[0] == [1, 3]


def test_get_pair_distance():
    assert get_pair_distance([1, 3]) == 2
    assert get_pair_distance([3, 1]) == 2


def test_get_day_1_part_1_answer():
    assert get_day_1_part_1_answer(test_input) == 11


def test_get_numbers_multipler():
    columns = get_columns(test_input)
    result = get_numbers_multiplier(*columns)
    assert result == [3, 1, 0, 0, 3, 3]


def test_get_day_1_part_2_answer():
    assert get_day_1_part_2_answer(test_input) == 31
