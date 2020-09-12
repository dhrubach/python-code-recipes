from random import randint


def is_even(num):
    while True:
        r = randint(0, num)

        if 2 * r == num:
            return True

        if 2 * r + 1 == num:
            return False


print(is_even(21))
print(is_even(100))
