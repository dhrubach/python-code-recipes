from stack.m_sum_subarray_minimums import SubSubarrayMins


class TestSubSubarrayMins:
    def test_data_1(self):
        sm = SubSubarrayMins()
        A = [3, 1, 2, 4]
        ans = sm.calculate(A)

        assert ans == 17
