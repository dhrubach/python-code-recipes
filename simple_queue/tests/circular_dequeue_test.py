from simple_queue.circular_dequeue import CircularDeQueue


class TestCircularDeQueue:
    def test_is_empty(self):
        cq = CircularDeQueue(3)
        assert cq.isEmpty() is True

        cq.insertLast(1)
        assert cq.isEmpty() is False

        cq.deleteFront()
        assert cq.isEmpty() is True

    def test_is_full(self):
        cq = CircularDeQueue(3)

        cq.insertLast(1)
        cq.insertLast(2)
        cq.insertFront(3)
        assert cq.isFull() is True

        cq.deleteLast()
        assert cq.isFull() is False

    def test_is_front(self):
        cq = CircularDeQueue(3)

        cq.insertFront(1)
        cq.insertLast(2)
        cq.insertFront(3)

        assert cq.getFront() == 3

    def test_is_rear(self):
        cq = CircularDeQueue(3)

        cq.insertLast(1)
        cq.insertFront(2)
        cq.insertLast(3)

        assert cq.getRear() == 3

    def test_sample_case(self):
        cq = CircularDeQueue(3)

        cq.insertFront(1)
        cq.insertFront(2)
        cq.insertLast(3)

        assert cq.insertLast(4) is False
        assert cq.getRear() == 3
        assert cq.isFull() is True

        cq.deleteFront()
        cq.insertFront(4)

        assert cq.getFront() == 4

    def test_sample_case_2(self):
        cq = CircularDeQueue(6)

        commands = [
            "insertFront",
            "getRear",
            "insertLast",
            "getRear",
            "insertFront",
            "getFront",
            "deleteLast",
            "getFront",
            "deleteLast",
            "deleteFront",
            "deleteFront",
            "getFront",
            "insertFront",
            "getRear",
        ]
        inputParams = [[6], [], [3], [], [5], [], [], [], [], [], [], [], [10], []]
        result = []
        expected_result = [
            True,
            6,
            True,
            3,
            True,
            5,
            True,
            5,
            True,
            True,
            False,
            -1,
            True,
            10,
        ]

        for c, p in zip(commands, inputParams):
            result.append(cq.executeCommands(c, p))

        assert result == expected_result

    def test_sample_case_3(self):
        cq = CircularDeQueue(3)

        commands = [
            "insertLast",
            "insertLast",
            "insertFront",
            "insertFront",
            "getRear",
            "isFull",
            "deleteLast",
            "insertFront",
            "getFront",
        ]
        inputParams = [[1], [2], [3], [4], [], [], [], [4], []]
        result = []
        expected_result = [True, True, True, False, 2, True, True, True, 4]

        for c, p in zip(commands, inputParams):
            result.append(cq.executeCommands(c, p))

        assert result == expected_result
