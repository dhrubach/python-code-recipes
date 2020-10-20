from stack.m_score_of_parenthesis import ScoreOfParenthesis


class TestScoreOfParenthesis:
    def test_single_pair(self):
        sp = ScoreOfParenthesis()
        ans = sp.calculate("()")
        assert ans == 1

        ans = sp.calculate_optimized("()")
        assert ans == 1

    def test_two_pairs(self):
        sp = ScoreOfParenthesis()
        ans = sp.calculate("()()")
        assert ans == 2

        ans = sp.calculate_optimized("()()")
        assert ans == 2

    def test_nested_pairs(self):
        sp = ScoreOfParenthesis()
        ans = sp.calculate("(())")
        assert ans == 2

        ans = sp.calculate_optimized("(())")
        assert ans == 2

    def test_nested_pairs_2(self):
        sp = ScoreOfParenthesis()
        ans = sp.calculate("(()())")
        assert ans == 4

        ans = sp.calculate_optimized("(()())")
        assert ans == 4

    def test_nested_pairs_3(self):
        sp = ScoreOfParenthesis()

        ans = sp.calculate("(()(()))")
        assert ans == 6

        ans = sp.calculate_optimized("(()(()))")
        assert ans == 6

    def test_three_pairs(self):
        sp = ScoreOfParenthesis()

        ans = sp.calculate("()()()")
        assert ans == 3

        ans = sp.calculate_optimized("()()()")
        assert ans == 3
