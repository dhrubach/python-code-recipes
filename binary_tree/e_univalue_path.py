#############################################################
# LeetCode Problem Number : 687
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/longest-univalue-path/
#############################################################
from binary_search_tree.tree_node import TreeNode


class LongestUnivaluePath:
    def calculate(self, root: TreeNode) -> int:
        if not root:
            return 0

        (lpath, lval) = self.calculatePath(root.left, 0, root.val)
        (rpath, rval) = self.calculatePath(root.right, 0, root.val)

        if lval == rval and lval == root.val:
            return lpath + rpath
        else:
            return lpath if lpath > rpath else rpath

    def calculatePath(self, node: TreeNode, cpath: int, cval: int) -> (int, int):
        if not node:
            return (cpath, None)

        npath = 1 if node.val == cval else 0
        nval = cval if node.val == cval else node.val

        (lpath, lval) = self.calculatePath(node.left, npath, nval)
        (rpath, rval) = self.calculatePath(node.right, npath, nval)

        if nval == lval:
            npath += lpath
        if nval == rval:
            npath += rpath
        if nval != lval and lval and npath < lpath:
            npath = lpath
            nval = lval
        if nval != rval and rval and npath < rpath:
            npath = rpath
            nval = rval

        return (npath, nval)
