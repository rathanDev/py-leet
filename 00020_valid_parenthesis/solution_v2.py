class Solution:

    def is_valid(self, s: str) -> bool:
        if not s or len(s) < 2:
            return False
        
        stack: list[str] = []
        brack_dict: dict[str, str] = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for char in s:
            if char in brack_dict: # if closing brack
                top: str = stack.pop() if stack else "_"
                if brack_dict[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack # return true if stack is empty
