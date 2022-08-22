import sys
input = sys.stdin.readline
full = 10000
stack = []
n = int(input())


for _ in range(n):
    text = list(map(str, input().rstrip().split()))
    stack_len = len(stack)
    if text[0] == 'push':
        stack.append(text[1])
    elif text[0] == 'top':
        if stack_len == 0:
            print('-1')
        else:
            print(stack[-1])
    elif text[0] == 'pop':
        if stack_len == 0:
            print('-1')
        else:
            print(stack.pop())
    elif text[0] == 'size':
        print(stack_len)
    elif text[0] == 'empty':
        if stack_len == 0:
            print('1')
        else:
            print('0')



