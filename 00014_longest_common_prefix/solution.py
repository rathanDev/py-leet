class Solution:

    def find_prefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        prefix: str = strs[0]

        for word in strs[1:]:

            while not word.startswith(prefix):
                prefix = prefix[:-1] # Remove the last char from the prefix
                if not prefix:
                    return ""
                
        return prefix





    def find_longest_common_prefix_v1(self, strs: list[str]) -> str:
        shortest: str = strs[0]
        for word in strs:
            if len(word) < len(shortest):
                shortest = word

        prefix: str = ""
        for i in range(0, len(shortest)):
            pc: str = shortest[0:i]

            for word in strs:
                if pc not in word:
                    return prefix
                
            prefix = pc

        return prefix