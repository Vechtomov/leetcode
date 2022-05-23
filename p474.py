from typing import List
from utils import are_equal


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        counter = [[s.count("0"), s.count("1")] for s in strs]

        for zeroes, ones in counter:
            for i in range(m, zeroes-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], 1+dp[i-zeroes][j-ones])

        return dp[-1][-1]


def test():
    s = Solution()
    are_equal(s.findMaxForm(strs=["10", "0", "1"], m=1, n=1), 2)
    are_equal(s.findMaxForm(
        strs=["10", "0001", "111001", "1", "0"], m=5, n=3), 4)
    are_equal(s.findMaxForm(["1100", "100000", "011111"], 6, 6), 2)


if __name__ == '__main__':
    test()
