###################################################
# LeetCode Problem Number : 204
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/count-primes/
###################################################


from typing import List, Union


class PrimeNumber:
    def generate_primes(self, n: int) -> Union[int, List[int]]:
        primes = []
        is_prime = [False, False] + [True] * (n - 1)

        for i in range(2, n + 1):
            if is_prime[i]:
                primes.append(i)

                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        return [len(primes), primes]
