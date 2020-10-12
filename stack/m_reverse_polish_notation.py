#######################################################################
# LeetCode Problem Number : 150
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/evaluate-reverse-polish-notation/
#######################################################################
from typing import List
from math import trunc


class ReversePolishNotation:
    # runtime -> 99.31%, memory -> 76.52%
    def evaluate(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for tk in tokens:
            if tk in operators:
                op1 = stack.pop()
                op2 = stack.pop()
                t = 0

                if tk == "+":
                    t = op2 + op1
                elif tk == "-":
                    t = op2 - op1
                elif tk == "/":
                    t = trunc(op2 / op1)
                else:
                    t = op2 * op1

                stack.append(t)
            else:
                stack.append(int(tk))

        return stack[0]
