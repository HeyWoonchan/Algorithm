sticks = [int(input()) for _ in range(4)]
sticks.sort()
print(min(sticks[2:])*(min(sticks[:2])))