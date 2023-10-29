'''
You are given a string .
Your task is to find out whether  is a valid regex or not.

Input Format

The first line contains integer , the number of test cases.
The next  lines contains the string .

Constraints


Output Format

Print "True" or "False" for each test case without quotes.

Sample Input

2
.*\+
.*+
Sample Output

True
False
Explanation

.*\+ : Valid regex.
.*+: Has the error multiple repeat. Hence, it is invalid.
'''

#Solution

import re 
T = int(input())
for i in range(0,T):
    regex_raw = input()
    try:
        regex = re.compile(regex_raw)
    except re.error:
        print(False)
    else:
        print(True)        
