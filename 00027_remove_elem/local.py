import pytest
from solution import Solution

@pytest.fixture()
def solution():
    return Solution()

def test_with_other(solution):
    nums: list[int] = [3, 2, 2, 3]
    val: int = 3
    res: int = solution.remove_elem(nums, val)
    assert res == 2

def test_with1(solution):
    nums: list[int] = [0,1,2,2,3,0,4,2]
    val: int = 2
    res: int = solution.remove_elem(nums, val)
    assert res == 5