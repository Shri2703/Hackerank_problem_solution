'''
The first line contains an integer , the number of operations.
The next  lines contains the space separated names of methods and their values.

Constraints


Output Format

Print the space separated elements of deque .

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft
Sample Output

1 2

'''

#Solution

from collections import deque 

d = deque()

for i in range (int(input())):
    inp = input().split()
    getattr(d , inp[0])(*[inp[1]] if len(inp) > 1 else[])

print(*[item for item in d])


