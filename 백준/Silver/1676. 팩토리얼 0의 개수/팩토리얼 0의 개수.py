# 팩토리얼 0의 개수

N = int(input())

factorial = 1

for i in range(N):
    factorial= (factorial * (i + 1))

answer = 0
while True:
    if factorial%10!=0:
        break
    else:
        answer += 1
        factorial //=10

print(answer)
