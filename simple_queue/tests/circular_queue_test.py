from simple_queue.circular_queue import CircularQueue


class TestCircularQueue:
    def test_is_empty(self):
        cq = CircularQueue(3)
        assert cq.isEmpty() is True

        cq.enqueue(1)
        assert cq.isEmpty() is False

        cq.dequeue()
        assert cq.isEmpty() is True

    def test_is_full(self):
        cq = CircularQueue(3)

        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)
        assert cq.isFull() is True

        cq.dequeue()
        assert cq.isFull() is False

    def test_is_front(self):
        cq = CircularQueue(3)

        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)

        assert cq.front() == 1

    def test_is_rear(self):
        cq = CircularQueue(3)

        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)

        assert cq.rear() == 3

    def test_sample_case(self):
        cq = CircularQueue(3)

        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)

        assert cq.enqueue(4) is False
        assert cq.rear() == 3
        assert cq.isFull() is True

        cq.dequeue()
        cq.enqueue(4)

        assert cq.rear() == 4

    def test_sample_case_2(self):
        cq = CircularQueue(6)

        commands = [
            "enQueue",
            "Rear",
            "Rear",
            "deQueue",
            "enQueue",
            "Rear",
            "deQueue",
            "Front",
            "deQueue",
            "deQueue",
            "deQueue",
        ]
        inputParams = [[6], [], [], [], [5], [], [], [], [], [], []]
        result = []
        expected_result = [True, 6, 6, True, True, 5, True, -1, False, False, False]

        for c, p in zip(commands, inputParams):
            result.append(cq.executeCommands(c, p))

        assert result == expected_result
