###############################################################
# LeetCode Problem Number : 561
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/array-partition-i/
###############################################################
class ArrayPartition:
    def arrayPairSum(self, num: [int]) -> int:
        """sort the input array"""
        sn = sorted(num)

        """ initialize 2 pointers """
        l, r = 0, len(sn) - 2
        sum = 0

        """ checking for input with 2 items - [1, 2]
            return the first element as the result
        """
        if l == r:
            return sn[0]

        while l < r:
            sum += sn[l] + sn[r]
            l, r = l + 2, r - 2

            """ when both pointers point at the same element,
                we have reached the mid-point. Add the current element
                to the result
            """
            sum += sn[l] if l == r else 0

        return sum


if __name__ == "__main__":
    p = ArrayPartition()
    print(p.arrayPairSum([1, 5, 2, 6, 4, 8, 9, 3, 7, 10]))
    print(p.arrayPairSum([7, 3, 1, 0, 0, 6]))
