#############################################################################################
# LeetCode Problem Number : 1466
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
#############################################################################################
from typing import List
from collections import defaultdict


class BinaryTree:
    # runtime -> 63.59%, memory -> 18.86%
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """ capture current connections present in the input in
            the form city 'i' -> city 'j'
        """
        roads = set()

        """ create a graph of connections between input cities """
        graph = defaultdict(list)

        for i, j in connections:
            """ populate the graph """
            graph[i].append(j)
            graph[j].append(i)

            """ populate input connections """
            roads.add((i, j))

        def dfs(node, parent):
            res = 0

            """ if there exists a road from parent to child
                in the given connections, it needs to be reversed
            """
            if (parent, node) in roads:
                res += 1

            for child in graph[node]:
                """ if the current child is the parent, then
                    skip this connection
                """
                if child != parent:
                    res += dfs(child, node)

            return res

        return dfs(0, -1)
