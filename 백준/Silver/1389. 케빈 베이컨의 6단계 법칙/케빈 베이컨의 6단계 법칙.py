N, M =map(int, input().split())

# relation = [tuple(map(int, input().split())) for _ in range(M)]

graph= [[1e9]*N for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1]=1
    graph[b-1][a-1]=1

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] =min(graph[i][j], graph[i][k]+graph[k][j])


for i in range(N):
    for j in range(N):
        if i==j:
            graph[i][j]=0

mins = []
for i in range(N):
    mins.append(sum(graph[i]))

result_min = min(mins)

for i in range(N):
    if mins[i]==result_min:
        print(i+1)
        break





