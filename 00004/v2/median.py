class Solution:

    def find_median(self, nums1: list[int], nums2: list[int]) -> float:
        
        count = len(nums1) + len(nums2)
        nums: list[int] = [0] * count
        i = 0
        i1 = 0
        i2 = 0

        while i1<len(nums1) and i2<len(nums2):
            if nums1[i1] < nums2[i2]:
                nums[i] = nums1[i1]
                i1 = i1 + 1
            else:
                nums[i] = nums2[i2]
                i2 = i2 + 1
            print(f"nums i{i} nums[i]:{nums[i]}")
            i = i + 1

        while i1 < len(nums1):
            nums[i] = nums1[i1]
            i1 = i1 + 1
            i = i + 1

        while i2 < len(nums2):
            nums[i] = nums2[i2]
            i2 = i2 + 1
            i = i + 1
        
        # 0 1 2 
        # 1 2 3 4 5     count=5
        #     ^

        # 0 1 2 3
        # 1 2 3 4 5 6     count=6
        #     ^ ^

        if (count % 2) == 1:
            index: int = count // 2
            print(f"index:{index}")
            return nums[index]
        else:
            index1: int = count // 2
            index2: int = (count // 2) - 1
            return (nums[index1] + nums[index2]) / 2


if __name__ == "__main__":
    nums1: list[int] = [1,3,5]
    nums2: list[int] = [2,4]        # 1 2 3 4 5
    sol = Solution()
    median: int = sol.find_median(nums1, nums2)
    print(f"V2 median: {median}")
