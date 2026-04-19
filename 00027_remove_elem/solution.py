class Solution:

    def remove_elem(self, nums: list[int], val: int) -> int:
        if not nums:
            return 0
        
        i: int = 0
        j: int = 0

        while j<len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1

        return i