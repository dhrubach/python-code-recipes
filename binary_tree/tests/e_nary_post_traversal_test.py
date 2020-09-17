from binary_tree.e_nary_post_traversal import PostorderTreeTraversal
from binary_tree.node import Node


class TestPostorderTreeTraversal:
    def test_traversal_1(self):
        pr = PostorderTreeTraversal()
        rt = Node(1, children=[Node(3, children=[Node(5), Node(6)]), Node(2), Node(4)])

        ans = pr.traverse(rt)

        assert ans == [5, 6, 3, 2, 4, 1]

    def test_traversal_2(self):
        pr = PostorderTreeTraversal()
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

        assert ans == [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]

    def test_iterative_traversal_1(self):
        pr = PostorderTreeTraversal()
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

        assert ans == [11, 15, 20, 17, 16, 12, 21, 18, 13, 22, 19, 23, 14, 10]
