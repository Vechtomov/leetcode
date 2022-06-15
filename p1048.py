"""
1048. Longest String Chain
You are given an array of words where each word consists of 
lowercase English letters.
wordA is a predecessor of wordB if and only if we can insert 
exactly one letter anywhere in wordA without changing the order 
of the other characters to make it equal to wordB.
For example, "abc" is a predecessor of "abac", while "cba" is 
not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] 
with k >= 1, where word1 is a predecessor of word2, word2 is a 
predecessor of word3, and so on. A single word is trivially a 
word chain with k == 1.
Return the length of the longest possible word chain with words 
chosen from the given list of words.

Example 1:
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

Example 2:
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain 
["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

Example 3:
Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the 
longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of 
the letters is changed.
 
Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.
"""

from collections import defaultdict
from utils import are_equal
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        word_len = {}
        for w in words:
            l = len(w)
            if l not in word_len:
                word_len[l] = set()

            word_len[l].add(w)

        def helper(w):
            wl = len(w)

            if wl < 2:
                return wl

            if w in dp:
                return dp[w]

            if wl-1 not in word_len:
                dp[w] = 1
            else:
                possible_words = [w[:i] + w[i+1:] for i in range(wl)]
                existed_words = [
                    w for w in possible_words if w in word_len[wl-1]]
                if not existed_words:
                    dp[w] = 1
                else:
                    dp[w] = max(helper(w) for w in existed_words) + 1

            return dp[w]

        return max(helper(w) for w in words)


class BetterSolution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = defaultdict(int)

        for w in sorted(words, key=len):
            dp[w] = max([dp[w[:i]+w[i+1:]] for i in range(len(w))]) + 1

        return max(dp.values())


def test_solution():

    def test(words: List[str], expected: int):
        sol = BetterSolution()
        are_equal(sol.longestStrChain(words), expected)

    test(["a"], 1)
    test(["a", "b"], 1)
    test(["a", "ab"], 2)
    test(["a", "ba"], 2)
    test(["ab", "a"], 2)
    test(["ab", "abc"], 2)
    test(["ab", "cab"], 2)
    test(["ab", "bac"], 1)
    test(["a", "ab", "cde"], 2)
    test(["a", "ab", "bac"], 2)
    test(["a", "ab", "abc"], 3)
    test(["a", "cde", "ab", "cdef", "cdbef"], 3)

    test(["a", "b", "ba", "bca", "bda", "bdca"], 4)
    test(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"], 5)
    test(["abcd", "dbqca"], 1)


if __name__ == '__main__':
    test_solution()
