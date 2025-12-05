TC = int(input())

def main():
    N, D, A, B, F = map(float,input().split())
    N = int(N)
    print(N, F*(D/(A+B)))

if __name__=="__main__":
    for _ in range(TC):
        main()