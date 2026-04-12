class Solution:

    def find_longest_palindrome(self, s: str) -> str:
        longest = ""
        for i in range(0,len(s)):

            l1 = self.expand(s, i, i)
            longest = self.find_longest(longest, l1)
            
            l2 = self.expand(s, i, i+1)
            longest = self.find_longest(longest, l2)

        return longest
    
    def expand(self, s: str, p1: int, p2: int) -> str:
        pal = ""
        while p1>=0 and p2<len(s) and s[p1]==s[p2]:
            p1 = p1-1
            p2 = p2+1
        pal = s[p1 + 1: p2]
        print(f"pal str{pal}")
        return pal

    def find_longest(self, current_longest: str, candidate: str) -> str:
        if len(candidate) > len(current_longest):
            return candidate
        else:
            return current_longest
