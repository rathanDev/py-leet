class Solution:

    def find_letter_combinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        num_dict: dict[str, str] = {
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
        self.backtrack(digits, num_dict, 0, "", combinations)
        return combinations
    
    def backtrack(self, digits: str, num_dict: dict, index: int, current: str, combinations: list[str]):
        if index == len(digits):
            combinations.append(current)
            return 
        
        letters: str = num_dict[digits[index]]
        for letter in letters:
            self.backtrack(digits, num_dict, index + 1, current + letter, combinations)
