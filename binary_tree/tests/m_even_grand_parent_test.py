from binary_tree.m_even_grand_parent import EvenGrandParent
from binarytree import build


class TestEvenGrandParent:
    def test_null_tree(self):
        ev = EvenGrandParent()
        assert ev.calculate(None) == 0

    def test_no_grand_parent(self):
        ev = EvenGrandParent()
        nodes = [1, 2, 3]
        rt = build(nodes)

        assert ev.calculate(rt) == 0

    def test_lc_data_1(self):
        ev = EvenGrandParent()
        nodes = [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]
        rt = build(nodes)

        ans = ev.calculate(rt)
        assert ans == 18
