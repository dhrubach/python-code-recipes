from simple_array.e_shortest_cont_sub_array import ShortestSubArray


class TestShortestSubArray:
    def test_single_element(self):
        sbr = ShortestSubArray()
        length = sbr.findUnsortedSubarray([1])

        assert length == 0

    def test_sorted_array(self):
        sbr = ShortestSubArray()
        length = sbr.findUnsortedSubarray([1, 2])

        assert length == 0

    def test_lc_data(self):
        sbr = ShortestSubArray()
        length = sbr.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])

        assert length == 5

    def test_lc_data_concise(self):
        sbr = ShortestSubArray()
        length = sbr.findUnsortedSubarray_concise([2, 6, 4, 8, 10, 9, 15])

        assert length == 5

    def test_lc_data_nosort(self):
        sbr = ShortestSubArray()

        length = sbr.findUnsortedSubarray_no_sort([2, 6, 4, 8, 10, 9, 15])
        assert length == 5

        length = sbr.findUnsortedSubarray_no_sort([1, 3, 7, 2, 5, 4, 6, 10])
        assert length == 6
