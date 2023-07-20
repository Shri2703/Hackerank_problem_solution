'''
You are given a string .
Your task is to verify that  is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

 Number can start with +, - or . symbol.
For example:
✔
+4.50
✔
-1.0
✔
.5
✔
-.7
✔
+.4
✖
 -+4.5

 Number must contain at least  decimal value.
For example:
✖
 12.
✔
12.0  

 Number must have exactly one . symbol.
 Number must not give any exceptions when converted using .

Input Format

The first line contains an integer , the number of test cases.
The next  line(s) contains a string .

Constraints

Output Format

Output True or False for each test case.

Sample Input 0

4
4.0O0
-1.00
+4.54
SomeRandomStuff
Sample Output 0

False
True
True
False
Explanation 0

: O is not a digit.
: is valid.
: is valid.
SomeRandomStuff: is not a number.
'''


#solution


import re
for _ in range(int(input())):
    print(re.search(r'^([-\+])?\d*\.\d+$', input()) is not None)

'''
code Explanation

import re: This line imports the Python re module, which stands for regular expressions. Regular expressions are powerful tools used for pattern matching and manipulation of strings.

for _ in range(int(input())): This line initiates a for loop that will iterate a certain number of times based on the user's input. The number of iterations is determined by the integer entered by the user (converted using int(input())).

print(re.search(r'^([-\+])?\d*\.\d+$', input()) is not None): This line performs the main operation within the for loop:

input(): This function prompts the user to enter a string (specifically, a floating-point number in this case).

re.search(pattern, string): This function attempts to find the first occurrence of the pattern in the input string. It returns a match object if a match is found, or None if there is no match.

r'^([-\+])?\d*\.\d+$': This is the regular expression pattern that the code uses to check if the input string is a valid floating-point number.

^: Asserts the beginning of the string.
([-\+])?: Captures an optional positive or negative sign. The ? makes the sign group optional.
\d*: Matches zero or more digits (0-9).
\.: Matches the decimal point character.
\d+: Matches one or more digits after the decimal point.
$: Asserts the end of the string.
is not None: This part checks if the result of the re.search function is not None. If a match is found, it means the input string is a valid floating-point number.

print(...): Finally, the result of the expression (whether the input is a valid floating-point number or not) is printed.

To summarize, this code prompts the user to enter a certain number of strings, and for each string entered, it checks if it represents a valid floating-point number and prints the result (True or False) accordingly. The regular expression used ensures that the string adheres to the format of a floating-point number.
''' 