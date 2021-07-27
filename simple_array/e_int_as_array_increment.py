from typing import List


class IncrementArray:
    def plus_one(self, arr: List[int]) -> List[int]:
        """ increment least significant digit (LSD) by 1
            value of LSD will be in the range (1, 10)
        """
        arr[-1] += 1

        for i in reversed(range(1, len(arr))):
            if arr[i] != 10:
                break
            """ in case of a carry-out, set digit to 0 and add carry over
                to the previous digit
            """
            arr[i] = 0
            arr[i - 1] += 1

        if arr[0] == 10:
            """ in case of a carry-out, one extra digit will be required
                set first digit to 1 and append a 0 to the end
            """
            arr[0] = 1
            arr.append(0)

        return arr
