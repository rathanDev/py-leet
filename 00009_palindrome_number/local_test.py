import pytest 
from solution import Solution

@pytest.fixture()
def solution():
    return Solution()

def test_negative(solution):
    assert solution.is_palindrome(-123) == False

def test_non_pal(solution):
    assert solution.is_palindrome(123) == False    

def test_pal(solution):
    assert solution.is_palindrome(1223221) == True