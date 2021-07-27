from typing import List


class AdvanceByOffsets:
    def can_reach_end(self, arr: List[int]) -> bool:
        max_reachable_index, end_index = 0, len(arr) - 1
        i = 0

        while i <= max_reachable_index and max_reachable_index <= end_index:
            """ furthest index reachable from 'i'th index --> i + A[i]
            """
            max_reachable_index = max(max_reachable_index, i + arr[i])
            i += 1

        return max_reachable_index >= end_index
