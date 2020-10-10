from stack.e_min_stack import MinStack


class TestMinStack:
    def test_stack_push(self):
        ms = MinStack()
        ms.push(1)
        ms.push(2)

        assert len(ms.arr) == 2
        assert ms.arr[-1] == (2, 1)

    def test_stack_pop(self):
        ms = MinStack()
        ms.push(1)
        ms.push(3)
        ms.push(2)

        ms.pop()

        assert len(ms.arr) == 2
        assert ms.arr[-1][0] == 3

    def test_stack_top(self):
        ms = MinStack()
        ms.push(1)
        ms.push(2)

        assert ms.top() == 2

    def test_stack_getmin(self):
        ms = MinStack()
        ms.push(0)
        ms.push(-1)
        ms.push(4)

        assert ms.getMin() == -1

        ms.pop()
        ms.pop()
        ms.push(10)

        assert ms.getMin() == 0
