from stack.e_next_less_element import NextLessElement


class TestNextLessElement:
    def test_empty_input(self):
        nle = NextLessElement()
        ans = nle.calculate([])

        assert ans == []

    def test_ple_data_1(self):
        nle = NextLessElement()
        nums = [3, 7, 8, 4]
        ans = nle.calculate(nums)

        assert ans == [-1, 2, 1, -1]

    def test_ple_data_2(self):
        nle = NextLessElement()
        nums = [2, 9, 7, 8, 3, 4, 6, 1]
        ans = nle.calculate(nums)

        assert ans == [7, 1, 2, 1, 3, 2, 1, -1]
