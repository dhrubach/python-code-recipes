from binary_tree.m_create_from_pre_in import BinaryTree


class TestBinaryTree:
    def test_lc_data_1(self):
        bt = BinaryTree()
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]

        ans = bt.buildFromPreInOrder(preorder=preorder, inorder=inorder)
        assert ans.val == 3
        assert ans.left.val == 9
        assert ans.right.left.val == 15

        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        ans = bt.buildFromPreInOrderOptimized(preorder=preorder, inorder=inorder)
        assert ans.val == 3
        assert ans.left.val == 9
        assert ans.right.left.val == 15

    def test_lc_data_2(self):
        bt = BinaryTree()
        preorder = [1, 2, 3]
        inorder = [1, 3, 2]

        ans = bt.buildFromPreInOrder(preorder=preorder, inorder=inorder)

        assert ans.val == 1
        assert ans.right.val == 2
        assert ans.right.left.val == 3

    def test_lc_data_3(self):
        bt = BinaryTree()
        preorder = [3, 9, 4, 2, 1, 5, 20, 15, 7]
        inorder = [2, 4, 1, 9, 5, 3, 15, 20, 7]

        ans = bt.buildFromPreInOrder(preorder=preorder, inorder=inorder)

        assert ans.val == 3
        assert ans.right.val == 20
        assert ans.left.left.right.val == 1
