from simple_array.e_arr_remove_key import RemoveElementFromArray


class TestRemoveElementFromArray:
    def test_remove_key(self):
        re = RemoveElementFromArray()

        input = [2, 3, 5, 6, 5, 8, 9, 5]
        key = 5
        result = re.delete_key(input, key)
        assert result[0] == 5
        assert result[1] == [2, 3, 6, 8, 9]

    def test_all_identical(self):
        re = RemoveElementFromArray()

        input = [2, 2, 2, 2]
        key = 2
        result = re.delete_key(input, key)
        assert result[0] == 0
        assert result[1] == []

    def test_no_key(self):
        re = RemoveElementFromArray()

        input = [2, 3, 4, 5, 6]
        key = 7
        result = re.delete_key(input, key)
        assert result[0] == 5
        assert result[1] == [2, 3, 4, 5, 6]
