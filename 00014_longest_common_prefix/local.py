import pytest
from solution import Solution

@pytest.fixture()
def solution():
    return Solution()

def test_word1(solution):
    words: list[str] = ["flower", "flow", "flight"]
    assert solution.find_prefix(words) == "fl"