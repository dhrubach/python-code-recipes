from stack.e_next_greater_element import NextGreaterElement


class TestNextGreaterElement:
    def test_lc_data_1(self):
        nge = NextGreaterElement()
        ans = nge.calculate([4, 1, 2], [1, 3, 4, 2])

        assert ans == [-1, 3, -1]

    def test_lc_data_2(self):
        nge = NextGreaterElement()
        ans = nge.calculate([2, 4], [1, 2, 3, 4])

        assert ans == [3, -1]
