from stack.m_next_greater_element_II import NextGreaterElement


class TestNextGreaterElement:
    def test_lc_data_1(self):
        nge = NextGreaterElement()
        nums = [1, 2, 1]

        assert nge.calculate(nums) == [2, -1, 2]
        assert nge.calculate_opm(nums) == [2, -1, 2]

    def test_lc_data_2(self):
        nge = NextGreaterElement()
        nums = [4, 2, 3, 5, 10]

        assert nge.calculate(nums) == [5, 3, 5, 10, -1]
        assert nge.calculate_opm(nums) == [5, 3, 5, 10, -1]
