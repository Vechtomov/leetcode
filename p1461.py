"""
1461. Check If a String Contains All Binary Codes of Size K
Given a binary string s and an integer k, return true if every binary code 
of length k is a substring of s. Otherwise, return false.
 
Example 1:
Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". 
They can be all found as substrings at indices 0, 1, 3 and 2 respectively.

Example 2:
Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear 
that both exist as a substring. 

Example 3:
Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and does not exist in the array.

Constraints:
1 <= s.length <= 5 * 105
s[i] is either '0' or '1'.
1 <= k <= 20
"""

from utils import are_equal
from itertools import combinations


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        unique = set()
        for i in range(len(s) - k + 1):
            unique.add(s[i:i+k])
        return len(unique) == 2**k


def test_solution():
    sol = Solution()

    def test(s: str, k: int, expected: int):
        are_equal(sol.hasAllCodes(s, k), expected)

    test("0", 1, False)
    test("1", 1, False)
    test("01", 1, True)
    test("01", 2, False)
    test("0011", 2, False)
    test("0110", 2, False)
    test("00110", 2, True)
    test("11001", 2, True)


def generate_s(k: int):
    arr = list(range(k))
    for i in range(k+1):
        for comb in combinations(arr, i):
            line = ['0'] * k
            for j in comb:
                line[j] = '1'
            yield ''.join(line)


if __name__ == '__main__':
    test_solution()
    # k = 20
    # s = ''.join(list(generate_s(k)))
    s = input()
    k = int(input())
    print(len(s))
    import time
    start = time.time()
    sol = Solution()
    res = sol.hasAllCodes(s, k)
    print(res)
    print(time.time() - start)
