from binary_tree.e_nary_pre_traversal import PreorderTreeTraversal
from binary_tree.node import Node


class TestPreorderTreeTraversal:
    def test_traversal_1(self):
        pr = PreorderTreeTraversal()
        rt = Node(1, children=[Node(3, children=[Node(5), Node(6)]), Node(2), Node(4)])

        ans = pr.traverse(rt)

        assert ans == [1, 3, 5, 6, 2, 4]

    def test_traversal_2(self):
        pr = PreorderTreeTraversal()
        rt = Node(
            1,
            children=[
                Node(2),
                Node(
                    3,
                    children=[
                        Node(6),
                        Node(7, children=[Node(11, children=[Node(14)])]),
                    ],
                ),
                Node(4, children=[Node(8, children=[Node(12)])]),
                Node(5, children=[Node(9, children=[Node(13)]), Node(10)]),
            ],
        )

        ans = pr.traverse(rt)

        assert ans == [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]

    def test_iterative_traversal_1(self):
        pr = PreorderTreeTraversal()
        rt = Node(
            10,
            children=[
                Node(11),
                Node(
                    12,
                    children=[
                        Node(15),
                        Node(16, children=[Node(17, children=[Node(20)])]),
                    ],
                ),
                Node(13, children=[Node(18, children=[Node(21)])]),
                Node(14, children=[Node(19, children=[Node(22)]), Node(23)]),
            ],
        )

        ans = pr.traverse_iterative(rt)

        assert ans == [10, 11, 12, 15, 16, 17, 20, 13, 18, 21, 14, 19, 22, 23]
