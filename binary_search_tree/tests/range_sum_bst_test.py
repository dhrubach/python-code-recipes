from binary_search_tree.range_sum_bst import RangeSumBST
from binary_search_tree.tree_node import TreeNode

from binarytree import build, tree


class TestRangeSumBST:
    def test_single_node(self):
        rs = RangeSumBST()
        ans = rs.calculate(TreeNode(10, None, None), 6, 11)

        assert ans == 10

    def test_three_level_sum(self):
        rs = RangeSumBST()
        nodes = [10, 5, 15, 3, 7, None, 18]
        bst = build(nodes)
        ans = rs.calculate(bst, 7, 15)

        assert ans == 32

    def test_four_level_sum(self):
        rs = RangeSumBST()
        nodes = [10, 5, 15, 3, 7, 13, 18, 1, None, 6]
        bst = build(nodes)
        ans = rs.calculate(bst, 6, 10)

        assert ans == 23

    def test_lc_data(self):
        rs = RangeSumBST()
        nodes = [18, 9, 27, 6, 15, 24, 30, 3, None, 12, None, 21]
        bst = build(nodes)
        ans = rs.calculate(bst, 18, 24)

        assert ans == 63
