from simple_array.e_min_steps_to_end import MinimumStepsToEnd


class TestMinimumStepsToEnd:
    def test_calculate(self):
        ms = MinimumStepsToEnd()

        min_steps = ms.calculate([3, 3, 1, 0, 2, 0, 1])
        assert min_steps == 3

        min_steps = ms.calculate([3, 3, 1, 0, 3, 0, 1])
        assert min_steps == 3

        min_steps = ms.calculate([3, 2, 0, 0, 2, 0, 1])
        assert min_steps == -1
