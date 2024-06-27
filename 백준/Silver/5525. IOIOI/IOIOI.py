#IOIOI

# p1  IOI
# p2 IOIOI
# p3 IOIOIOI
# pn (O가 N개)

# input - N, M(S의 길이), S
# task - M길이의 S문자열에 pn이 몇개가 들어가있는가?

N = int(input())
M = int(input())
S = input()

find_str = ''
for _ in range(N):
    find_str+='I'
    find_str+='O'
find_str+='I'

count = 0
for i in range(len(S)-len(find_str)+1):
    # print(S[i:i+len(find_str)], find_str)
    if str(S[i:i+len(find_str)])==find_str:
        count+=1

print(count)
