from typing import List


class MinimumStepsToEnd:
    def calculate(self, arr: List[int]) -> int:
        max_reachable_index, end_index, steps = 0, len(arr) - 1, 0
        i = 0

        while i <= max_reachable_index and max_reachable_index < end_index:
            end_from_current_index = i + arr[i]
            if end_from_current_index > max_reachable_index:
                steps += 1
            max_reachable_index = max(max_reachable_index, end_from_current_index)
            i += 1

        return steps if max_reachable_index >= end_index else -1
