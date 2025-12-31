N = int(input())
arr = [input() for _ in range(N)]
arr=list(set(arr))
arr.sort(key=lambda x:(len(x),x))
print(*arr,sep='\n')