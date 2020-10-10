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
                if len(stack) == 0:
                    return False

                prev_bracket = stack.pop()
                if brackets_map[prev_bracket] != ch:
                    return False

        return len(stack) == 0
