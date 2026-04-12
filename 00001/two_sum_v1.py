
def two_sum(nums: list[int], target: int) -> list[int]:
    seen_dic: dict[int, int] = {}
    for index, num in enumerate(nums):
        comp: int = target - num
        if comp in seen_dic:
            comp_index: int = seen_dic[comp]
            return [index, comp_index]
        seen_dic[num] = index
    res: list[int] = []
    return res

if __name__ == "__main__":
    nums: list[int] = [1, 2, 3, 4, 5, 6]
    target: int = 7
    res = two_sum(nums, target)
    print(f"Res: {res}")