from functools import cmp_to_key


def version_comparator(v1: str, v2: str):
    """ check if both the versions are equal """
    if v1 == v2:
        return 0

    v1_components = v1.split(".")
    v2_components = v2.split(".")

    common_elements = min(len(v1_components), len(v2_components))

    for i in range(common_elements):
        """ if at a given index, element in v1 > element in v2,
            then v1 is greater than v2
        """
        if v1_components[i] > v2_components[i]:
            return 1

        """ if at a given index, element in v1 < element in v2,
            then v1 is less than v2
        """
        if v1_components[i] < v2_components[i]:
            return -1

    """ check of the 2 versions has a higher prefix
    """
    return 1 if len(v1_components) > len(v2_components) else -1


comparator_func = cmp_to_key(version_comparator)

""" test set 1 """
data = ["0.1.0", "3.2.1", "2.2.3", "0.1.1"]
print(sorted(data, key=comparator_func, reverse=True))

""" test set 2 """
data = [
    "1.3.0.9",
    "0.2.0",
    "3.1.2",
    "0.1.6",
    "5.0.0",
    "3.3.3.3",
    "3.3.3.3.3",
    "3.10",
    "0.2.0",
]
print(sorted(data, key=comparator_func, reverse=True))
