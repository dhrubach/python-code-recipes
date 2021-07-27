from simple_array.m_int_as_array_multiply import MultiplyArray


class TestMultiplyArray:
    def test_calculate(self):
        ma = MultiplyArray()

        result = ma.calculate([1, 2, 3], [9, 8, 7])
        assert result == [1, 2, 1, 4, 0, 1]
