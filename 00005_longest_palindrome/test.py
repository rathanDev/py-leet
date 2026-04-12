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
    ("a", "a")
])
def test_find_longest_palindrome(solution, s1, exp):
    assert solution.find_longest_palindrome(s1) == exp