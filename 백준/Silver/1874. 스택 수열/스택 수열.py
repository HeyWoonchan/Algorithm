from collections import deque
# 스택 수열

n = int(input())

target = [int(input())for i in range(n)]

stack = deque()


"""
12345678
12578
436
"""

result = []

result_n = []

now = 1

for i in range(n):
    while now<=target[i]:
        stack.append(now)
        now+=1
        result.append('+')
    result.append('-')
    result_n.append(stack.pop())
    
# print(result_n)

if result_n != target:
    print('NO')
else:
    print(*result, sep='\n')


