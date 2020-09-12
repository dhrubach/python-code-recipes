from binary_tree.deepest_leaves_sum import DeepestLeavesSum
from binary_search_tree.tree_node import TreeNode
from binarytree import build


class TestDeepestLeavesSum:
    def test_null_root(self):
        dl = DeepestLeavesSum()

        ans = dl.calculate(None)
        assert ans == 0

        ans = dl.calculate_optimized(None)
        assert ans == 0

    def test_root_node(self):
        dl = DeepestLeavesSum()

        ans = dl.calculate_optimized(TreeNode(1))
        assert ans == 1

        ans = dl.calculate(TreeNode(1))
        assert ans == 1

    def test_lc_data(self):
        dl = DeepestLeavesSum()
        nodes = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, None, None, 8]
        rt = build(nodes)

        ans = dl.calculate(rt)
        assert ans == 15

        ans = dl.calculate_optimized(rt)
        assert ans == 15
