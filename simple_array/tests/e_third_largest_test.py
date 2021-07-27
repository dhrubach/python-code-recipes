from simple_array.e_third_largest import ThirdLargestNumber


class TestThirdLargestNumber:
    def test_two_element(self):
        th = ThirdLargestNumber()
        ans = th.find([3, 4])

        assert ans == 4

    def test_duplicate_ele(self):
        th = ThirdLargestNumber()
        ans = th.find([3, 4, 2, 2, 1])

        assert ans == 2

    def test_lc_data(self):
        th = ThirdLargestNumber()
        ans = th.find([1, 4, 5, 2, 7, 8, 9, 3, 4])

        assert ans == 7
