#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;
int N;
int T[15];
int P[15];
int dp[15];

int dfs(int nowDay){
    if (nowDay>=N) return 0;
    // cout<<nowDay<<" nowday\n";
    if (dp[nowDay]!=-1){
        return dp[nowDay];
    }
    int &ret=dp[nowDay];
    ret = dfs(nowDay+1); //안고르는경우
    //오늘 것을 고르는 경우(N일 안에 끝나야함) 
    if (nowDay+T[nowDay]<=N){
        ret=max(ret,dfs(nowDay+T[nowDay])+P[nowDay]);
    }
    
    //다음날로 넘어가는경우
    
    return ret;
}   

int main(){
    cin>>N;
    memset(dp,-1,sizeof(dp));
    for (int i=0;i<N;i++){
        cin>>T[i]>>P[i];
    }   

    cout<<dfs(0);

}