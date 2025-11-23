import heapq
import sys
input = sys.stdin.readline

def main():
    N, K = map(int,input().split())

    jewel_info = []
    bag_info = []
    for _ in range(N):
        m,v = map(int,input().split())
        heapq.heappush(jewel_info, (m,v))

    for _ in range(K):
        c = int(input())
        bag_info.append(c)

    bag_info.sort()

    temp_heapq=[]
    answer = 0
    for c in bag_info:
        for _ in range(len(jewel_info)):
            m,v = jewel_info[0]
            if m<=c:
                heapq.heappop(jewel_info)
                heapq.heappush(temp_heapq,(-v,m))
            else:
                break
        if len(temp_heapq)>0:
            answer-=heapq.heappop(temp_heapq)[0]
    print(answer)

if __name__=="__main__":
    main()
