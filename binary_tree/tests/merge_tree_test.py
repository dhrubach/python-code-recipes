from binary_tree.merge_tree import BinaryTreeMerge
from binarytree import build


class TestBinaryMergeTree:
    def test_single_tree(self):
        btm = BinaryTreeMerge()
        nodes = [1, 4, 6]
        bt = build(nodes)

        ans = btm.mergeTrees(bt, None)

        assert ans.val == 1
        assert ans.right.val == 6

    def test_lc_dataset(self):
        btm = BinaryTreeMerge()
        nodes = [1, 3, 2, 5, None, None, None]
        bt1 = build(nodes)

        nodes = [2, 1, 3, None, 4, None, 7]
        bt2 = build(nodes)

        ans = btm.mergeTrees(bt1, bt2)

        assert ans.val == 3
        assert ans.left.left.val == 5
        assert ans.right.left is None
