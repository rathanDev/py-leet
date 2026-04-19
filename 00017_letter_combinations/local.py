import pytest
from solution_v3 import Solution

@pytest.mark.parametrize(
    "digits, expected",
    [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("2", ["a", "b", "c"]),
        ("", []),
        ("7", ["p", "q", "r", "s"]),
        ("9", ["w", "x", "y", "z"]),
        ("27", ["ap", "aq", "ar", "as", "bp", "bq", "br", "bs", "cp", "cq", "cr", "cs"]),
    ],
)
def test_find_letter_combinations(digits, expected):
    solution = Solution()
    result = solution.find_letter_combinations(digits)
    assert sorted(result) == sorted(expected)