#############################################################################
# LeetCode Problem Number : 80
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
#############################################################################
from typing import List, Union


class SortedArray:
    def delete_duplicates(self, arr: List[int]) -> Union[int, List[int]]:
        write_index = 2

        if len(arr) <= 2:
            return write_index

        for i in range(2, len(arr)):
            if (arr[write_index - 1] != arr[i]) or (
                arr[write_index - 1] == arr[i]
                and arr[write_index - 1] != arr[write_index - 2]
            ):
                arr[write_index] = arr[i]
                write_index += 1

        return [write_index, arr[:write_index]]
