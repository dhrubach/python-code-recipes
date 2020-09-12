from simple_array.kth_largest import KLargestElement


class TestKLargestElement:
    def test_empty_array(self):
        kl = KLargestElement()
        ans = kl.find_bubble_sort(None, 2)

        assert ans is None

    def test_bubble_sort(self):
        kl = KLargestElement()

        nums = [3, 2, 1, 5, 6, 4]
        ans = kl.find_bubble_sort(nums, 2)
        assert ans == 5

        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        ans = kl.find_bubble_sort(nums, 4)
        assert ans == 4
