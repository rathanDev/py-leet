import pytest
from solution import Solution

@pytest.fixture()
def solution():
    return Solution()

def test_1(solution):
    nums: list[int] = [-1, 0, 1, 2, -1, -4]
    res = solution.find_3_sum(nums)
    print(f"Nums: {nums} Res: {res}")
    assert sorted(res) == sorted([[-1, -1, 2], [-1, 0, 1]])

def test_no_triplets(solution):
    nums: list[int] = [1, 2, 3, 4, 5]
    res = solution.find_3_sum(nums)
    print(f"Nums: {nums} Res: {res}")
    assert res == []

def test_all_zeros(solution):
    nums: list[int] = [0, 0, 0, 0]
    res = solution.find_3_sum(nums)
    print(f"Nums: {nums} Res: {res}")
    assert res == [[0, 0, 0]]

def test_large_numbers(solution):
    nums: list[int] = [-1000000, 500000, 500000, 0]
    res = solution.find_3_sum(nums)
    print(f"Nums: {nums} Res: {res}")
    assert res == [[-1000000, 500000, 500000]]

def test_empty_list(solution):
    nums: list[int] = []
    res = solution.find_3_sum(nums)
    print(f"Nums: {nums} Res: {res}")
    assert res == []

def test_single_element(solution):
    nums: list[int] = [1]
    res = solution.find_3_sum(nums)
    print(f"Nums: {nums} Res: {res}")
    assert res == []

def test_two_elements(solution):
    nums: list[int] = [1, -1]
    res = solution.find_3_sum(nums)
    print(f"Nums: {nums} Res: {res}")
    assert res == []