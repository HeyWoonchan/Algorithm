from functools import cmp_to_key
def solution(numbers):
    return str(int(''.join(sorted([str(n) for n in numbers], key=cmp_to_key(lambda a,b:0 if a+b==b+a else 1 if a+b<b+a else -1)))))