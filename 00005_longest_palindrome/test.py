import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("s1, exp", [
    ("abcba", "abcba"),
    ("abcbx", "bcb"),
    ("babad", "bab"),
    ("cbbd", "bb"),
])
def test_find_longest_palindrome(solution, s1, exp):
    assert solution.find_longest(s1) == exp