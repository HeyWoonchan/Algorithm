K = int(input())
N = int(input())

now = K
duration = 0
target = 3*60+30
for _ in range(N):
    T, Z = input().split()
    T = int(T)
    if duration+T>target:
        print(now)
        break
    if Z=="T":
        now = (now)%8 +1
    duration+=T
