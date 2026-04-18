class Solution:

    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev: int = 0
        temp: int = x

        while temp != 0:
            digit = temp % 10
            rev = (rev * 10) + digit
            temp //= 10

        return rev == x
    