from depth_first_search.m_target_sum import TargetSum


class TestTargetSum:
    def test_lc_data_1(self):
        ts = TargetSum()
        ans = ts.calculate_hashmap([1, 1, 1, 1, 1], 3)

        assert ans == 5
