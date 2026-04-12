import pytest
from median_v2 import Solution 

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("nums1, nums2, expected", [
    ([1,3], [2], 2.0),
    ([1,2], [3,4,5], 3.0),
    ([], [1,2,3], 2.0),
])
def test_find_median(solution, nums1, nums2, expected):
    print(f"Test expected{expected}")
    assert solution.find_median(nums1, nums2) == expected