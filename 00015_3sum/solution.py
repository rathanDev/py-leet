class Solution:

    def find_3_sum(self, nums: list[int]) -> list[list[int]]:

        res: list[list[int]] = []
        nums.sort()

        for i in range(0, len(nums)-2):

            if (i>0) and (nums[i] == nums[i-1]):
                continue

            start: int = i + 1
            end: int = len(nums)-1
            n0: int = nums[i]

            while (start < end):

                n1: int = nums[start]
                n2: int = nums[end]
                sum: int = n0 + n1 + n2
                print(f"Sum: {sum}")

                if (sum == 0):
                    res.append([n0, n1, n2])
                    while start < end and (nums[start] == nums[start+1]):
                        start += 1
                    while end > start and (nums[end] == nums[end-1]):
                        end -= 1
                    start += 1
                    end -= 1
                    
                elif (sum < 0):
                    start += 1
                else:
                    end -= 1  

                
        return res
