from binary_search_tree.m_bst_from_preorder import BstFromPreOrder


class TestBstFromPreOrder:
    def test_single_node(self):
        bst = BstFromPreOrder()
        preorder = [8]
        ans = bst.create(preorder)

        assert ans.val == 8

    def test_lc_data_1(self):
        bst = BstFromPreOrder()
        preorder = [8, 5, 1, 3, 4, 7, 10, 12]
        ans = bst.create(preorder)

        assert ans.left.val == 5
        assert ans.right.right.val == 12

    def test_lc_data_2(self):
        bst = BstFromPreOrder()
        preorder = [18, 9, 6, 3, 15, 12, 27, 24, 21, 30]
        ans = bst.create(preorder)

        assert ans.left.right.left.val == 12
        assert ans.right.right.val == 30

    def test_inorder_lc_data_1(self):
        bst = BstFromPreOrder()
        preorder = [8, 5, 1, 3, 4, 7, 10, 12]
        ans = bst.create_inorder(preorder)

        assert ans.left.val == 5
        assert ans.right.right.val == 12

    def test_inorder_lc_data_2(self):
        bst = BstFromPreOrder()
        preorder = [18, 9, 6, 3, 15, 12, 27, 24, 21, 30]
        ans = bst.create_inorder(preorder)

        assert ans.left.right.left.val == 12
        assert ans.right.right.val == 30
