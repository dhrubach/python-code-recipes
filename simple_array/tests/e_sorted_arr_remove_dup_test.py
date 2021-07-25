from simple_array.e_sorted_arr_remove_dup import SortedArray


class TestSortedArray:
    def test_delete_duplicates(self):
        sa = SortedArray()

        input = [2, 3, 5, 5, 6, 7, 7]
        result = sa.delete_duplicates(input)
        assert result[0] == 5
        assert result[1] == [2, 3, 5, 6, 7]

    def test_no_duplicates(self):
        sa = SortedArray()

        input = [
            2,
            3,
            5,
        ]
        result = sa.delete_duplicates(input)
        assert result[0] == 3
        assert result[1] == [2, 3, 5]

    def test_all_identical(self):
        sa = SortedArray()

        input = [2, 2, 2, 2]
        result = sa.delete_duplicates(input)
        assert result[0] == 1
        assert result[1] == [2]
