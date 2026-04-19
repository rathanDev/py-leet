import pytest
from solution import Solution

@pytest.mark.parametrize(
    "nums, expected_length, expected_nums",
    [
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([1, 1, 2], 2, [1, 2]),
        # ([1, 1, 1], 1, [1]),
        # ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        # ([], 0, []),
        # ([1], 1, [1]),
    ],
)
def test_remove_dups(nums, expected_length, expected_nums):
    solution = Solution()
    result_length = solution.remove_dups(nums)
    assert result_length == expected_length
    assert nums[:result_length] == expected_nums