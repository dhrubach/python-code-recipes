###############################################################
# LeetCode Problem Number : 880
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/decoded-string-at-index/
##############################################################

# TODO - Explanation


class DecodeString:
    def valueAtIndex_bf(self, S: str, K: int) -> str:
        stack = []

        for ch in S:
            if stack and ch.isdigit():
                stack = stack + (stack * (int(ch) - 1))
            else:
                stack.append(ch)

            if len(stack) >= K:
                break

        return stack[K - 1]

    # runtime -> 99.61%, memory -> 100%
    def valueAtIndex_opm(self, S: str, K: int) -> str:
        dlen = 0

        for i, c in enumerate(S):
            dlen = dlen * int(c) if c.isdigit() else dlen + 1
            if dlen >= K:
                break

        for j in range(i, -1, -1):
            ch = S[j]
            if ch.isdigit():
                dlen /= int(ch)
                K %= dlen
            else:
                if K == 0 or K == dlen:
                    return ch
                dlen -= 1

        return ""

    # runtime -> 76.45%, memory -> 100%
    def valueAtIndex_opm_2(self, S: str, K: int) -> str:
        A = [1]
        for x in S[1:]:

            if A[-1] >= K:
                break

            if x.isdigit():
                A.append(A[-1] * int(x))
            else:
                A.append(A[-1] + 1)

        for i in reversed(range(len(A))):
            K %= A[i]
            if not K and S[i].isalpha():
                return S[i]
