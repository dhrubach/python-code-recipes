########################################################
# LeetCode Problem Number : 20
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/valid-parentheses/
########################################################
class ValidParenthesis:
    # runtime -> 81.06%
    def isValid(self, s: str) -> bool:
        brackets_map = {"(": ")", "{": "}", "[": "]"}
        open_brackets = ["(", "[", "{"]

        stack = []

        for ch in s:
            if ch in open_brackets:
                stack.append(ch)
            else:
                """cannot get to the else block with an empty list.
                this means the expression starts with an 'close'
                parenthesis or there is an orphaned 'close' parenthesis
                """
                if len(stack) == 0:
                    return False

                prev_bracket = stack.pop()
                if brackets_map[prev_bracket] != ch:
                    return False

        """ stack should be empty at the end of the loop.
            this means for each 'open' parenthesis, there
            is a matching 'close' parenthesis
        """
        return len(stack) == 0
