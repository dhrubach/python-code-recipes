from typing import List, Union


class RemoveElementFromArray:
    def delete_key(self, arr: List[int], key: int) -> Union[int, List[int]]:
        write_index = 0

        for i in range(len(arr)):
            if arr[i] != key:
                arr[write_index] = arr[i]
                write_index += 1

        return [write_index, arr[:write_index]]
