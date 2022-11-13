from task.gold_mine import get_gold_count


def test_get_gold_count():
    assert get_gold_count([[10]]) == 10
    assert get_gold_count([[7, 2], [4, 1]]) == 9
    assert get_gold_count([[3, 2, 1], [4, 1, 5], [1, 6, 2]]) == 12
    assert get_gold_count([[3, 2, 1, 6], [4, 1, 1, 8], [1, 6, 2, 4]]) == 16
    assert get_gold_count([[4, 1, 6, 7], [4, 1, 5, 3], [6, 6, 1, 2], [7, 1, 1, 1]]) == 18
