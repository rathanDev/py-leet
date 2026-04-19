class Solution:

    def find_first(self, haystack: str, needle: str) -> int:

        for hp in range(0, (len(haystack)-len(needle)+1)):

            if haystack[hp] == needle[0]:
                sp: int = hp
                np: int = 0

                while sp < (hp + len(needle)) and haystack[sp] == needle[np]:
                    sp += 1
                    np += 1

                if np == len(needle):
                    return hp

        return -1