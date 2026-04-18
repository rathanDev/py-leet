import pytest
from solution import Solution

@pytest.fixture()
def solution():
    return Solution()

def test_find_max1(solution):
    h: list[int] = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    max_vol: int = solution.find_max_vol(h)
    assert max_vol == 49