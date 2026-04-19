import pytest
from solution import Solution

@pytest.fixture()
def solution():
    return Solution()

def test_with_sad(solution):
    haystack: str = "sadbutsad"
    needle: str = "sad"
    res: int = solution.find_first(haystack, needle)
    assert res == 0

