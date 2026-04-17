class Solution:

    def reverse(self, x: int) -> int:       # 123
        neg: bool = x < 0
        temp: int = abs(x)
        rev: int = 0

        while temp != 0:
            digit: int = temp % 10      # 3   2     1
            rev = (rev * 10) + digit    # 3   32    321
            print(f"Rev:{rev}")
            temp = temp // 10            # 12  1     0

        if (neg):
            rev = -rev

        if rev < -(2**31) or rev > (2**31 - 1):
            return 0

        return rev
