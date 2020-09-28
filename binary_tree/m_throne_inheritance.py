###############################################################
# LeetCode Problem Number : 139
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/sum-root-to-leaf-numbers/
###############################################################
from collections import defaultdict
from typing import List


# runtime -> 92.76%, memory -> 66.24%
class ThroneInheritance:
    def __init__(self, kingName: str):
        self.kingName = kingName
        self.dead = set()
        self.kingdom = defaultdict(list)

    def birth(self, parentName: str, childName: str) -> None:
        self.kingdom[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[int]:
        def dfs(member: str) -> List[str]:
            curOrder = []

            if member not in self.dead:
                curOrder.append(member)

            for child in self.kingdom[member]:
                curOrder += dfs(child)

            return curOrder

        return dfs(self.kingName)
