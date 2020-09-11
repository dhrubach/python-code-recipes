from simple_array.k_diff_pairs import KDiffPairs


class TestKDiffPairs:
    def test_k_diff(self):
        kd = KDiffPairs()

        ans = kd.findPairs([3, 1, 4, 1, 5], 2)
        assert ans == 2

        ans = kd.findPairs([1, 2, 3, 4, 5], 1)
        assert ans == 4

        ans = kd.findPairs([3, 1, 4, 1, 5], 0)
        assert ans == 1
