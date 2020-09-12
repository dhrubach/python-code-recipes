###############################################################
# LeetCode Problem Number : 344
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/reverse-string/
###############################################################
class ReverseString:
    def reverse(self, input: [str]):
        if len(input) == 0:
            print("invalid input")

        start_ptr = 0
        end_ptr = len(input) - 1

        while start_ptr < end_ptr:
            input[start_ptr], input[end_ptr] = input[end_ptr], input[start_ptr]
            start_ptr += 1
            end_ptr -= 1

        print(input)


if __name__ == "__main__":
    reverse_obj = ReverseString()
    reverse_obj.reverse(["h", "e", "l", "l", "o"])
    reverse_obj.reverse(["H", "a", "n", "n", "a", "h"])
