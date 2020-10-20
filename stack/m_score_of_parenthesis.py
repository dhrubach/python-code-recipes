###########################################################
# LeetCode Problem Number : 856
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/score-of-parentheses/
###########################################################
class ScoreOfParenthesis:
    # runtime -> 75.90%, memory -> 100%
    def calculate(self, S: str) -> int:
        stack = []

        for tk in S:
            if tk == ")":
                temp = 0
                while stack:
                    op = stack.pop()
                    if op != "(":
                        """ add the current score """
                        temp += op
                    else:
                        """for each closing parenthesis, multiply
                        current score by 2 with minimum set to 1
                        """
                        stack.append(max(temp * 2, 1))
                        break
            else:
                stack.append(tk)

        return sum(stack)

    # runtime -> 75.90%, memory -> 100%
    def calculate_optimized(self, S: str) -> int:
        """final sum will be a sum of powers of 2, as every core
        (a substring (), with score 1) will have it's score multiplied
        by 2 for each exterior set of parentheses that contains that core.

        example input : (()())
        calculate as : (()) + (())
        """
        ans = level = 0

        for i, x in enumerate(S):
            if x == "(":
                """ increase level with each open parenthesis """
                level += 1
            else:
                """ devrease level with each open parenthesis """
                level -= 1
                if S[i - 1] == "(":
                    """for every matching pair, calculate score
                    at that level by raising current level to power 2
                    """
                    ans += 1 << level

        return ans
