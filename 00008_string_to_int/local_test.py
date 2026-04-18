import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_positive_number(solution):
    input: str = "123"
    res = solution.string_to_int(input)
    print(f"input:{input} res:{res}")
    assert res == 123

def test_neg_number(solution):
    input: str = "-123"
    res = solution.string_to_int(input)
    print(f"input:{input} res:{res}")
    assert res == -123

