##########################################################################
# LeetCode Problem Number : 26
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
##########################################################################
from typing import List, Union


class SortedArray:
    def delete_duplicates(self, arr: List[int]) -> Union[int, List[int]]:
        write_index = 1

        for i in range(1, len(arr)):
            if arr[write_index - 1] != arr[i]:
                arr[write_index] = arr[i]
                write_index += 1

        return [write_index, arr[:write_index]]
