class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        for i in range(len(s) - k + 1):
            substring = s[i:i + k]
            if len(set(substring)) == 1:
                char = substring[0]
                if (i == 0 or s[i - 1] != char) and (i + k == len(s) or s[i + k] != char):
                    return True
        return False
