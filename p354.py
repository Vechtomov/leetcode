"""
354. Russian Doll Envelopes
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] 
represents the width and the height of an envelope.
One envelope can fit into another if and only if both the width and height 
of one envelope are greater than the other envelope's width and height.
Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).
Note: You cannot rotate an envelope.

Example 1:
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

Example 2:
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1

Constraints:
1 <= envelopes.length <= 105
envelopes[i].length == 2
1 <= wi, hi <= 105
"""
from bisect import bisect_left
from typing import List
from utils import are_equal


class Solution:
    def maxEnvelopes(self, a: List[List[int]]) -> int:
        a.sort(key=lambda x: (x[0], -x[1]))
        print(a)

        # LIS by height
        dp = [0 for i in range(len(a) + 1)]
        l = 1
        dp[0] = a[0][1]

        for i in range(1, len(a)):
            if a[i][1] > dp[l-1]:
                dp[l] = a[i][1]
                l += 1
            else:
                dp[bisect_left(dp, a[i][1], 0, l-1)] = a[i][1]
        return l


def test_solution():
    sol = Solution()

    def test(envelopes: List[List[int]], expected: int):
        are_equal(sol.maxEnvelopes(envelopes), expected)

    test([[1, 1]], 1)
    test([[1, 1], [2, 2]], 2)
    test([[1, 1], [2, 1]], 1)
    test([[1, 1], [1, 2]], 1)
    test([[1, 10], [2, 20], [2, 2], [3, 3], [3, 30], [5, 5], [6, 6]], 4)
    test([[1, 1], [1, 1], [1, 1]], 1)
    test([[5, 4], [6, 4], [6, 7], [2, 3]], 3)
    test([[1, 3], [3, 5], [6, 7], [6, 8], [8, 4], [9, 5]], 3)
    test([[46, 89], [50, 53], [52, 68], [72, 45], [77, 81]], 3)


if __name__ == '__main__':
    test_solution()
