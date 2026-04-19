class Solution:

    def find_letter_combinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        num_dic: dict[str, str] = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": "",
        }

        combinations: list[str] = []
        self.backtrack(digits, num_dic, 0, "", combinations)
        return combinations
    
    def backtrack(self, digits: str, num_dic: dict[str, str], index: int, current: str, combinations: list[str]) -> None:
        if index == len(digits):
            combinations.append(current)
            return
        
        possible_letters = num_dic[digits[index]]
        for letter in possible_letters:
            self.backtrack(digits, num_dic, index+1, current+letter, combinations)
