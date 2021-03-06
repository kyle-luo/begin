# We are to write the letters of a given string S, from left to right into lines. Each line has maximum width 100 units, and if writing a letter would cause the width of the line to exceed 100 units, it is written on the next line. We are given an array widths, an array where widths[0] is the width of 'a', widths[1] is the width of 'b', ..., and widths[25] is the width of 'z'.
#
# Now answer two questions: how many lines have at least one character from S, and what is the width used by the last such line? Return your answer as an integer list of length 2.
#
#
# Example :
# Input:
# widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
# S = "abcdefghijklmnopqrstuvwxyz"
# Output: [3, 60]
# Explanation:
# All letters have the same length of 10. To write all 26 letters,
# we need two full lines and one line with 60 units.
#
#
# Example :
# Input:
# widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
# S = "bbbcccdddaaa"
# Output: [2, 4]
# Explanation:
# All letters except 'a' have the same length of 10, and
# "bbbcccdddaa" will cover 9 * 10 + 2 * 4 = 98 units.
# For the last 'a', it is written on the second line because
# there is only 2 units left in the first line.
# So the answer is 2 lines, plus 4 units in the second line.



def numberOfLines(widths, S):
    output = [1, 0]
    for char in S:
        output[1] += widths[ord(char) - 97]
        if output[1] > 100:
            output[0] += 1
            output[1] = widths[ord(char) - 97]
    return output

print(numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz"))
print(numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa"))


def numberOfLines(widths, S):
    dic = {}
    for x in range(97, 97+26):
        dic[chr(x)] = widths[x - 97]
    output = [1, 0]
    for char in S:
        output[1] += dic[char]
        if output[1] > 100:
            output[0] += 1
            output[1] = dic[char]
    return output

print(numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz"))
print(numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa"))


def numberOfLines(widths, S):
    line, length = 1, 0
    for char in S:
        length += widths[ord(char) - 97]
        if length > 100:
            line += 1
            length = widths[ord(char) - 97]
    return line, length

print(numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz"))
print(numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa"))