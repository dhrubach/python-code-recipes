from binary_tree.e_univalue_path import LongestUnivaluePath
from binarytree import build


class TestLongestUnivaluePath:
    def test_lc_data_1(self):
        lv = LongestUnivaluePath()
        nodes = [1, 4, 5, 4, 4, 5, None]
        bt = build(nodes)

        ans = lv.calculate(bt)

        assert ans == 2

    def test_lc_data_2(self):
        lv = LongestUnivaluePath()
        nodes = [5, 4, 5, 1, 1, 5, None]
        bt = build(nodes)

        ans = lv.calculate(bt)

        assert ans == 2

    def test_lc_data_3(self):
        lv = LongestUnivaluePath()
        nodes = [1, 1, 1]
        bt = build(nodes)

        ans = lv.calculate(bt)

        assert ans == 2

    def test_lc_data_4(self):
        lv = LongestUnivaluePath()
        nodes = [1, 2, 2, 2, 2, 2]
        bt = build(nodes)

        ans = lv.calculate(bt)

        assert ans == 2
