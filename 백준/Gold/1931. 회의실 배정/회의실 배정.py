#회의실 배정 문제 - 일찍 끝나는 회의부터 배정하면 된다
#항상 미래의 가능성이 많은 것을 그리디하게 뽑는 것.
import sys,heapq
input=sys.stdin.readline
N=int(input())
hq=[]
for _ in range(N):
    start,end=map(int,input().split())
    heapq.heappush(hq,(end,start))

cnt=0
nowEnd=0
while hq:
    end,start=heapq.heappop(hq)
    while hq and start<nowEnd:
        end,start=heapq.heappop(hq)
    if start>=nowEnd:
        nowEnd=end
        cnt+=1
print(cnt)