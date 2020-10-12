from stack.m_reverse_polish_notation import ReversePolishNotation


class TestReversePolishNotation:
    def test_equation_1(self):
        rpn = ReversePolishNotation()
        tokens = ["2", "1", "+", "3", "*"]

        ans = rpn.evaluate(tokens)
        assert ans == 9

    def test_equation_2(self):
        rpn = ReversePolishNotation()
        tokens = ["4", "13", "5", "/", "+"]

        ans = rpn.evaluate(tokens)
        assert ans == 6

    def test_equation_3(self):
        rpn = ReversePolishNotation()
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

        ans = rpn.evaluate(tokens)
        assert ans == 22

    def test_equation_4(self):
        rpn = ReversePolishNotation()
        tokens = ["10", "6", "+"]

        ans = rpn.evaluate(tokens)
        assert ans == 16
