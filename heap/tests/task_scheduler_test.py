from heap.task_scheduler import TaskScheduler


class TestTaskScheduler:
    def test_all_unique(self):
        tsc = TaskScheduler()
        result = tsc.leastInterval(["A", "B", "C"], 2)

        assert result == 3

    def test_all_same(self):
        tsc = TaskScheduler()
        result = tsc.leastInterval(["A", "A", "A"], 2)

        assert result == 7

    def test_sample_case_1(self):
        tsc = TaskScheduler()
        result = tsc.leastInterval(["A", "A", "A", "A", "B", "B", "D", "E"], 2)

        assert result == 10

    def test_sample_case_2(self):
        tsc = TaskScheduler()
        result = tsc.leastInterval(
            ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2
        )

        assert result == 16
