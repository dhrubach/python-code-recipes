###################################################################################
# LeetCode Problem Number : 1443
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
###################################################################################
import collections
from typing import List


class BinaryTree:
    def minTimeTree(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """ below solution assumes a specific order of the nodes --> [parent, child]. it
            fails when a node is represented as [child, parent].
        """

        """ use a `default dictionary` to map each node to its child nodes.
            https://docs.python.org/3/library/collections.html#collections.defaultdict

            defaulting to a `list` makes it easier to iterate over
            child nodes in later stages of the algorithm
        """
        routes = collections.defaultdict(list)
        for u, v in edges:
            routes[u].append(v)

        visited = set()

        def dfs(node: int) -> int:
            if node in visited:
                return 0
            visited.add(node)

            cost = 0

            """ iterate over child nodes in each level """
            for child in routes[node]:
                cost += dfs(child)

            """ node with an apple or with a sub-tree
                which has an apple
            """
            if cost or hasApple[node]:
                return cost + 1

            """ leaf node with no apples """
            return 0

        """ start iterating from the vertex denoted by node 0 """
        res = dfs(0)

        """ multiply response by 2 to account for to & from distance.
            subtract 1 from the response to account for root node.
        """
        return 2 * (res - 1) if res else 0

    # runtime -> 99.10%, memory -> 72.69%
    def minTimeGraph(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """ works for both [parent, child] & [child, parent]
        """
        routes = [[] for _ in range(n)]
        for k, v in edges:
            routes[k].append(v)
            routes[v].append(k)

        """ maintain a list of visited nodes to prevent double counting """
        visited = set()

        def dfs(node):
            """ return 0 if a node has been already visited """
            if node in visited:
                return 0
            """ mark a node as visited """
            visited.add(node)

            cost = 0
            for child in routes[node]:
                cost += dfs(child)

            """ node with an apple or with a sub-tree
                which has an apple
            """
            if cost or hasApple[node]:
                return 1 + cost

            """ leaf node with no apples """
            return 0

        """ multiply response by 2 to account for to & from distance.
            subtract 1 from the response to account for root node.
        """
        return max(2 * (dfs(0) - 1), 0)
