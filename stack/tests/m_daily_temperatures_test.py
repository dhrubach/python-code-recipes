from stack.m_daily_temperatures import DailyTemperature


class TestDailyTemperature:
    def test_lc_Data_1(self):
        dt = DailyTemperature()
        temp = [73, 74, 75, 71, 69, 72, 76, 73]

        ans = dt.calculate_bf(temp)
        assert ans[0] == 1
        assert ans[-1] == 0

        ans = dt.calculate_op_1(temp)
        assert ans[0] == 1
        assert ans[-1] == 0

        ans = dt.calculate_op_2(temp)
        assert ans[0] == 1
        assert ans[-1] == 0

    def test_lc_Data_2(self):
        dt = DailyTemperature()
        temp = [73]
        ans = dt.calculate_bf(temp)

        assert ans[0] == 0

    def test_lc_Data_3(self):
        dt = DailyTemperature()
        temp = [73, 75, 74, 71, 69, 72, 76]

        ans = dt.calculate_bf(temp)
        assert ans == [1, 5, 4, 2, 1, 1, 0]

        ans = dt.calculate_op_1(temp)
        assert ans == [1, 5, 4, 2, 1, 1, 0]

        ans = dt.calculate_op_2(temp)
        assert ans == [1, 5, 4, 2, 1, 1, 0]
