"""
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

from typing import List
from utils import are_equal


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        d = [float('inf')] * (amount + 1)
        for i in range(1, amount+1):
            for c in coins:
                if i - c == 0:
                    d[i] = 1
                elif i - c > 0:
                    d[i] = min(d[i], d[i - c] + 1)
        return d[-1] if d[-1] < float('inf') else -1


def test():
    s = Solution()
    are_equal(s.coinChange([1, 2, 5], 11), 3)
    are_equal(s.coinChange([2], 3), -1)
    are_equal(s.coinChange([1], 0), 0)
    are_equal(s.coinChange([1], 10), 10)
    are_equal(s.coinChange([1, 2], 10), 5)


if __name__ == '__main__':
    test()
