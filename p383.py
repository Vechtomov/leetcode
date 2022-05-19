"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

from collections import defaultdict
from utils import are_equal


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        d = defaultdict(int)
        for c in magazine:
            d[c] += 1
        for c in ransomNote:
            if d[c] == 0:
                return False
            d[c] -= 1
        return True


def test():
    s = Solution()
    are_equal(s.canConstruct("a", "b"), False)
    are_equal(s.canConstruct("aa", "ab"), False)
    are_equal(s.canConstruct("aa", "aab"), True)
    are_equal(s.canConstruct("ab", "a"), False)
    are_equal(s.canConstruct("ab", "ab"), True)
    are_equal(s.canConstruct("ab", "ba"), True)


if __name__ == "__main__":
    test()
