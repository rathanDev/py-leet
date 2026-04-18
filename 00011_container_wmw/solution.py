class Solution:

#  0  1  2  3  4  5  6  7  8
# [1, 8, 6, 2, 5, 4, 8, 3, 7]
#  ^                       ^
# 
# min(7,1)*8 = 1*8 = 8

    def find_max_vol(self, heights: list[int]) -> int:

        start: int = 0
        end: int = len(heights) - 1
        max_vol: int = 0

        while (start < end):
            sh: int = heights[start]
            eh: int = heights[end]
            vol: int = min(sh, eh) * (end - start)
            max_vol = max(max_vol, vol)

            if (sh < eh):
                start += 1
            else:
                end -= 1

        return max_vol


    
