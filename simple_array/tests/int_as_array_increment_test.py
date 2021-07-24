from simple_array.int_as_array_increment import IncrementArray


class TestIncrementArray:
    def test_plus_one(self):
        ina = IncrementArray()

        arr = [1, 2, 9]
        result = ina.plus_one(arr)
        assert result == [1, 3, 0]

        arr = [7, 4, 9, 9]
        result = ina.plus_one(arr)
        assert result == [7, 5, 0, 0]
