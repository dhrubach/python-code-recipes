##########################################################################
# LeetCode Problem Number : 1376
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/time-needed-to-inform-all-employees/

##########################################################################
from collections import defaultdict, deque
from typing import List


class BinaryTree:
    # DFS runtime -> 60.51%, memory -> 26.25%
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        managerMap = defaultdict(list)

        """ create a dictionary which maps a manager to reporting employees """
        for i, v in enumerate(manager):
            managerMap[v].append(i)

        def dfs(mgr):
            """ minimum time taken at a given node :
                    time taken by an employee to inform his / her reportees at that node.
                    (this is given by informTime[i] for ith employee)
                    +
                    maximum time taken by each of his / her reportees to inform their reportees
                    (this is computed by the recursive call)
            """
            return max([dfs(emp) for emp in managerMap[mgr]] or [0]) + informTime[mgr]

        return dfs(headID)

    # BFS runtime -> 87.98%, memory -> 53.31%
    def numOfMinutesBFS(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        managerMap = defaultdict(list)

        for i, v in enumerate(manager):
            managerMap[v].append(i)

        res = 0
        queue = deque([(headID, 0)])

        while queue:
            mgr, time = queue.popleft()
            res = max(res, time)

            for emp in managerMap[mgr]:
                queue.append((emp, time + informTime[mgr]))

        return res
