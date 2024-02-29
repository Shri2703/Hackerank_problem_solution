'''
You are given a string .
 contains alphanumeric characters only.
 Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string .

Constraints

Output Format

Output the sorted string .

Sample Input

Sorting1234
Sample Output

ginortS1324

'''

#Solution


def f(c):
    code = 0
    if c.isupper():
        code = 10 ** 3
    elif c.isdigit():
        code = 10 ** 6
        if ord(c) % 2 == 0:
            code = 10 ** 9
    return code + ord(c)

print(*sorted(input(), key=lambda c: f(c)), sep='')