class Solution:

    def find_longest(self, s: str) -> str:
        longest = ""
        for i in range(0,len(s)-1):

            l1 = self.expand(s, i, i)
            if len(l1) > len(longest):
                longest = l1
            
            l2 = self.expand(s, i, i+1)
            if len(l2) > len(longest):
                longest = l2

        return longest
    
    def expand(self, s: str, p1: int, p2: int):
        pal = ""
        while p1>=0 and p2<len(s) and s[p1]==s[p2]:
            pal = s[p1: p2 + 1]
            print(f"pal str{pal}")
            p1 = p1-1
            p2 = p2+1
        return pal

