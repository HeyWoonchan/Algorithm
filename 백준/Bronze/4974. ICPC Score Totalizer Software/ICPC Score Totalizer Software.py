while True:
    n = int(input())
    if n==0:
        break
    dataset = [int(input()) for _ in range(n)]
    dataset.sort()
    print(sum(dataset[1:-1])//(n-2))
