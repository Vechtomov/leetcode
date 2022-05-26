"""
401. Binary Watch
A binary watch has 4 LEDs on the top which represent the hours (0-11), 
and the 6 LEDs on the bottom represent the minutes (0-59). 
Each LED represents a zero or one, with the least significant bit on the right.
For example, the below binary watch reads "4:51".
Given an integer turnedOn which represents the number of LEDs that are currently on, 
return all possible times the watch could represent. You may return the answer in any order.
The hour must not contain a leading zero.
For example, "01:00" is not valid. It should be "1:00".
The minute must be consist of two digits and may contain a leading zero.
For example, "10:2" is not valid. It should be "10:02".

Example 1:
Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

Example 2:
Input: turnedOn = 9
Output: []

Constraints:
0 <= turnedOn <= 10
"""

from typing import List

from utils import are_equal
from itertools import combinations, product


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for h in range(min(turnedOn, 3)+1):
            for m in range(min(5, turnedOn - h)+1):
                if turnedOn - h - m > 0:
                    continue
                hours = [sum([int(2**i) for i in h_ind])
                         for h_ind in combinations(range(4), h)] if h > 0 else [0]
                minutes = [sum([int(2**i) for i in m_ind])
                           for m_ind in combinations(range(6), m)] if m > 0 else [0]
                for hour, minute in product(hours, minutes):
                    if hour < 12 and minute < 60:
                        res.append(f"{hour}:{minute:02d}")
        return res


def test_solution():
    sol = Solution()

    def test(n: int, expected: List[str]):
        are_equal(set(sol.readBinaryWatch(n)), set(expected))

    test(0, ["0:00"])
    test(1, ["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"])
    test(8, ['7:55', '11:47', '7:47', '11:55', '11:59', '11:31', '7:31', '7:59'])
    test(9, [])
    test(10, [])


if __name__ == '__main__':
    test_solution()
