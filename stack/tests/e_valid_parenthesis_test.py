from stack.e_valid_parenthesis import ValidParenthesis


class TestValidParenthesis:
    def test_is_valid(self):
        vp = ValidParenthesis()
        inputs = ["()", "(){}[]", "({})"]

        for ip in inputs:
            assert vp.isValid(ip) is True

    def test_is_invalid(self):
        vp = ValidParenthesis()
        inputs = ["(}", "(){]", "({)}"]

        for ip in inputs:
            assert vp.isValid(ip) is False

    def test_odd_parenthesis(self):
        vp = ValidParenthesis()
        inputs = ["(", "(){", "({}"]

        for ip in inputs:
            assert vp.isValid(ip) is False

    def test_only_right_parenthesis(self):
        vp = ValidParenthesis()
        inputs = ["]", "])", "]})"]

        for ip in inputs:
            assert vp.isValid(ip) is False

    def test_only_left_parenthesis(self):
        vp = ValidParenthesis()
        inputs = ["[", "{{", "({["]

        for ip in inputs:
            assert vp.isValid(ip) is False
