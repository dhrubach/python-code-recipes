from stack.e_previous_less_element import PreviousLessElement


class TestPreviousLessElement:
    def test_empty_input(self):
        ple = PreviousLessElement()

        assert ple.calculate([]) == []

    def test_ple_data_1(self):
        ple = PreviousLessElement()
        nums = [3, 7, 8, 4]
        ans = ple.calculate(nums)

        assert ans == [-1, 1, 1, 3]

    def test_ple_data_2(self):
        ple = PreviousLessElement()
        nums = [2, 9, 7, 8, 3, 4, 6, 1]
        ans = ple.calculate(nums)

        assert ans == [-1, 1, 2, 1, 4, 1, 1, -1]
