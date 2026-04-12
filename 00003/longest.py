class Solution:

    @staticmethod
    def length_of_longest(s: str) -> int:
        char_dic: dict[str, int] = {}
        max_len: int = 0
        start: int = 0

        for char_index, char in enumerate(s):

            if char in char_dic:
                max_len = max(len(char_dic), max_len)
                while char in char_dic:
                    del char_dic[s[start]]
                    start = start + 1

            char_dic[char] = char_index
                
        max_len = max(len(char_dic), max_len)
        return max_len


if __name__ == "__main__":
    s: str = "abccabqrc" # 5
    max_len = Solution.length_of_longest(s)
    print(f"len_of_longest str:{s} len:{max_len}")

    s = "abcabcbb" #3
    max_len = Solution.length_of_longest(s)
    print(f"len_of_longest str:{s} len:{max_len}")

    s = "aaaa" #1
    max_len = Solution.length_of_longest(s)
    print(f"len_of_longest str:{s} len:{max_len}")