N, K = map(int, input().split())

def combi(n,k):
    if k==0 or n==k:
        return 1
      
    return combi(n-1,k)+combi(n-1,k-1)
print(combi(N,K))