class Solution:

    def string_to_int(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        
        neg: bool = False
        i: int = 0

        while i < len(s) and s[i] == ' ':   # Skip leading whitespaces
            i += 1

        while i < len(s) and (s[i]=='-' or s[i]=='+'):  # Check for sign
            neg = s[i] == '-'
            i = i + 1

        num: int = 0
        while i < len(s) and s[i].isdigit():    # Process numeric only
            num = (num * 10) + int(s[i])
            i += 1

        if neg:
            num = -num

        # Clamp the result to 32-bit signed integer range
        num = max(-(2**31), min(num, 2**31 - 1))
        
        return num
    
    