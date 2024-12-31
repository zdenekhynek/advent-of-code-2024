from day_8 import (
    test_input,
    test_input2,
    test_input3,
    get_grid,
    get_unique_antidotes,
    get_antennas,
)


def test_get_grid():
    grid = get_grid(test_input)
    assert len(grid) == 10
    assert grid[1][3] == "."


def test_get_unique_antidotes():
    assert len(get_unique_antidotes(test_input)) == 2
    assert len(get_unique_antidotes(test_input2)) == 14
    assert len(get_unique_antidotes(test_input3, True)) == 9
    assert len(get_unique_antidotes(test_input2, True)) == 34


def test_get_antennas():
    grid = get_grid(test_input2)
    antennas = get_antennas(grid)
    assert len(antennas) == 7
    assert antennas[0] == (8, 1)
