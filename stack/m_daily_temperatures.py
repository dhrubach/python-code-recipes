#########################################################
# LeetCode Problem Number : 739
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/daily-temperatures/
#########################################################
from typing import List
from collections import defaultdict


class DailyTemperature:
    def calculate_bf(self, T: List[int]) -> List[int]:
        """ create a hash-map of temperature vs day of occurrence
            example :
                {
                    71: [0],
                    72: [1,2]
                }
        """
        temperatures = defaultdict(list)
        for i, v in enumerate(T):
            temperatures[v].append(i)

        res = []

        for i, t in enumerate(T):
            res.insert(i, 0)
            for v in T[i + 1 :]:
                """ for each temperature T[i], find out a recorded
                    temperature T[v] where T[i] > T[v]
                """
                if v > t:
                    """ identify future days with T[v] temperature """
                    days = [day for day in temperatures[v] if day > i]
                    if len(days):
                        """ for multiple future days with T[v] temperature,
                            take the first occurrence to calculate the difference
                        """
                        res[i] = days[0] - i
                        break
        return res

    # runtime -> 88.03%, memory --> 12.28%
    # time complexity : O(n)
    def calculate_op_1(self, T: List[int]) -> List[int]:
        n, right_max = len(T), float("-inf")

        res = [0] * n

        for i in range(n - 1, -1, -1):
            """ run a loop from right to left """
            t = T[i]

            if right_max <= t:
                """ if T[i] is greater than current recorded max
                    temperature, then there are no future days which
                    is warmer than T[i]

                    update current max to T[i]

                    res[i] = 0
                """
                right_max = t
            else:
                days = 1
                """ if T[i] is less than current recorded max temperature,
                    then check if T[i] > T[i+1]

                    if false, it means that the following day is warmer than T[i]
                    set res[i] = 1

                    if true, it means that the following day is colder than T[i]
                    increase days by res[i + 1] and repeat till the next warmer
                    day is found. with this approach, we don't iterate over all the
                    future temperatures to find the next warmer one.
                """
                while T[i + days] <= t:
                    days += res[i + days]
                res[i] = days

        return res

    # runtime -> 88.03%, memory --> 12.28%
    # O(2n) for ascending order, since each day is accessed one time in the for loop and one time in the while loop
    # O(n) for descending order since each node is only accessed in the for loop
    # other cases is somewhere between O(n) and O(2n)
    def calculate_op_2(self, T: List[int]) -> List[int]:
        """ example input : [73, 74, 75, 71, 69, 72, 76, 73] """
        ans = [0] * len(T)
        stack = []

        for i, t in enumerate(T):
            """ check if the current temperature is greater than
                the temperature pointed by the index at the top of the stack

                example : i -> 1, t -> 74, stack -> [0]
                          T[stack[-1]] < t -> T[0] < t -> 73 < 74

                when True, pop index from stack and set answer to
                (current index - poped value)

                example : i -> 3, t -> 71, stack -> [2]
                          T[stack[-1]] < t -> T[2] < t -> 75 < 71

                when False, record current index in stack -> [2, 3]

                process a day only when another warmer day has been found
                i.e. process T[2] only when T[6] has been found
            """
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur

            """ insert current index into the stack """
            stack.append(i)

        return ans
