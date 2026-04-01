#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int N;
    cin>>N;
    int T[N];
    int P[N];
    for (int i=0;i<N;i++){
        cin>>T[i]>>P[i];
    }
    vector<int>dp(N+1,0);
    for(int i=N-1;i>=0;i--){
        dp[i]=dp[i+1];
        if (i+T[i]>N)continue;
        dp[i]=max(dp[i],dp[i+T[i]]+P[i]);
    }
    cout<<dp[0];



}