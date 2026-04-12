class TwoSum:

    @staticmethod
    def find_two_sum(nums: list[int], target: int) -> list[int]:
        seen_dic: dict[int, int] = {}
        for i, num in enumerate(nums):
            comp: int = target - num
            if comp in seen_dic:
                return [i, seen_dic[comp]]
            seen_dic[num] = i        
        return []
        
if __name__ == "__main__":
    nums: list[int] = [1,2,3,4,5,6]
    target: int = 7
    res = TwoSum.find_two_sum(nums, target)
    print(f"TwoSumV2 Target:{target} Res:{res}")
