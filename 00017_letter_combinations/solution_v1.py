class SolutionV1:

    def find_letter_combinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        num_dic: dict[str,str] = {
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

        def backtrack(index: int, path: str):
            if index == len(digits):
                combinations.append(path)
                return
            
            possible_letters = num_dic[digits[index]]
            for letter in possible_letters:
                backtrack(index+1, path+letter)

        combinations = []
        backtrack(0, "")
        return combinations