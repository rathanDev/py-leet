import pytest
from solution_v2 import Solution

@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),  # Simple valid case
        ("()[]{}", True),  # Multiple valid pairs
        ("(]", False),  # Mismatched parentheses
        ("([)]", False),  # Incorrect nesting
        ("{[]}", True),  # Correctly nested
        ("(", False),  # Single opening bracket
        (")", False),  # Single closing bracket
        ("((()))", True),  # Deeply nested valid case
        ("((())", False),  # Unmatched opening bracket
    ],
)
def test_is_valid(s, expected):
    solution = Solution()
    assert solution.is_valid(s) == expected