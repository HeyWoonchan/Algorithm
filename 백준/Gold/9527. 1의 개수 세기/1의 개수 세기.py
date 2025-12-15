"""
1<=A<=B<=10**16
이므로, 시간복잡도는 최대 O(logN)이어야 함.

어떤 숫자 A 의 이진수를 구하기 -> log2,N만큼 든다.

101을 예로 들 때, 

11까지의 1의 합
+
01까지의 1의 합 = n
+
1*(1+01)

dp(2)+재귀


"""

dp = {}
dp[0]=0
dp[1]=1

def sumOnes(bit):

    if bit in dp:
        return dp[bit]
    i = bin(bit)
    a = sumOnes((1<<(len(i)-3))-1)
    n = sumOnes(bit-(1<<(len(i)-3)))
    
    dp[bit] = a+n+1+bit-(1<<(len(i)-3))
    return dp[bit]

a,b = map(int,input().split())

print(sumOnes(b)-sumOnes(a-1))