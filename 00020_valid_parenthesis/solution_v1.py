class Solution:

    def is_valid(self, s: str) -> bool:
        if not s or len(s) < 2:
            return False
        
        pair_dict: dict[str, str] = {
            ")", "(",
            "]", "[",
            "}", "{",
        }

        stack: list[str] = []

        for char in s:
            if char in pair_dict: # if it's a closing brace
                top = stack.pop() if stack else "_" # pop from stack, if stack has elem, else a dummy val
                if pair_dict[char] != top:
                    return False
            else:                   # if it's an opening brace
                stack.append(char)

        return not stack # Return true if stack is empty 
    
    

