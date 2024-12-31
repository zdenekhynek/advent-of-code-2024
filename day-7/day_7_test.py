from day_7 import (
    test_input,
    get_rows,
    get_all_variations,
    apply_eq,
    is_equation,
    get_truth_sum,
)


def test_get_columns():
    rows = list(get_rows(test_input))
    print(rows)
    assert len(rows) == 9
    assert rows[0]["test"] == 190


def test_get_all_variations():
    out = get_all_variations((10, 19))
    assert len(out) == 2

    out = get_all_variations((10, 19, 20))
    assert len(out) == 4

    out = get_all_variations((10, 19, 20, 20))
    assert len(out) == 8


def test_apply_eq():
    assert apply_eq((10, 19), "+") == 29
    assert apply_eq((10, 19), "*") == 190
    assert apply_eq((10, 19), "|") == 1019


def test_is_equation():
    input = {"test": 190, "digits": (10, 19)}
    assert is_equation(input) == True


def test_get_truth_sum():
    assert get_truth_sum(test_input) == 3749
    assert get_truth_sum(test_input, "+*|") == 11387
