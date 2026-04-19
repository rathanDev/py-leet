class Solution:

    # [0,0,1,1,1,2,2,3,3,4]
    # [0,1,1,1,1,2,2,3,3,4]
    #    ^       ^
    #    i       j

    def remove_dups(self, nums: list[int]) -> int:

        i: int = 0
        j: int = 1

        while i < j and j < len(nums):
            if nums[j] != nums[i]:
                nums[i + 1] = nums[j]
                i += 1
            j += 1

        return i+1

