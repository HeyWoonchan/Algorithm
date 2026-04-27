#include <string>
#include <vector>

using namespace std;

long long MOD = 1234567LL;

long long solution(int n) {
    long long answer = 0;
    long long dp[2001];
    dp[0]=0;
    dp[1]=1;
    dp[2]=2;
    for (int i=3;i<2001;i++){
        dp[i]=(dp[i-1]+dp[i-2])%MOD;
    }
    
    return dp[n]%MOD;
}