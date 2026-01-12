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
    # print("뽑음",start,end)
    while hq and start<nowEnd:
        end,start=heapq.heappop(hq)
        # print("끝나는것보다 시작이 빨라버림, 아닐때까지 더뽑음.",start,end)
    if start>=nowEnd:
        nowEnd=end
        # print("배정 완료,끝나는 시간 재설정",nowEnd)
        cnt+=1
print(cnt)