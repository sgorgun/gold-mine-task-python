import pytest as pytest

from task.solution import get_gold_count


def fixed_test(mines: list[list[int]], answer) -> None:
    assert answer == get_gold_count(mines), \
        'Wrong answer'


@pytest.mark.timeout(5)
def test_1():
    fixed_test([[10]], 10)


@pytest.mark.timeout(5)
def test_2():
    fixed_test([[7, 2], [4, 1]], 9)


@pytest.mark.timeout(5)
def test_3():
    fixed_test([[3, 2, 1], [4, 1, 5], [1, 6, 2]], 12)


@pytest.mark.timeout(5)
def test_4():
    fixed_test([[3, 2, 1, 6], [4, 1, 1, 8], [1, 6, 2, 4]], 16)


@pytest.mark.timeout(5)
def test_5():
    fixed_test([[4, 1, 6, 7], [4, 1, 5, 3], [6, 6, 1, 2], [7, 1, 1, 1]], 18)
