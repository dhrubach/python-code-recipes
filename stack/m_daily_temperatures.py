#########################################################
# LeetCode Problem Number : 739
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/daily-temperatures/
#########################################################
from typing import List
from collections import defaultdict


class DailyTemperature:
    def calculate_bf(self, T: List[int]) -> List[int]:
        temperatures = defaultdict(list)
        for i, v in enumerate(T):
            temperatures[v].append(i)

        res = []

        for i, t in enumerate(T):
            res.insert(i, 0)
            for v in T[i + 1 :]:
                if v > t:
                    days = [day for day in temperatures[v] if day > i]
                    if len(days):
                        res[i] = days[0] - i
                        break
        return res

    # runtime -> 88.03%, memory --> 12.28%
    def calculate_op_1(self, T: List[int]) -> List[int]:
        n, right_max = len(T), float("-inf")

        res = [0] * n

        for i in range(n - 1, -1, -1):
            t = T[i]

            if right_max <= t:
                right_max = t
            else:
                days = 1
                while T[i + days] <= t:
                    days += res[i + days]
                res[i] = days

        return res

    # runtime -> 88.03%, memory --> 12.28%
    def calculate_op_2(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = []

        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)

        return ans
