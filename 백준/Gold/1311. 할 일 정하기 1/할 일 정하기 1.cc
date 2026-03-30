#include<iostream>
#include<vector>

using namespace std;
const int INF = 1e9;
int D[20][20];
vector<vector<int>> dp(1<<20,vector<int>(20,INF));

int dfs(int nowPerson, int selected, int n){
    
    if (selected==((1<<n)-1)){
        return 0;
    }
    if (dp[selected][nowPerson]!=INF){
        return dp[selected][nowPerson];
    }
    dp[selected][nowPerson]=INF;
    // cout<<"dfs"<<" "<<nowPerson<<'\n';
    

    for (int i=0;i<n;i++){
        if (selected&(1<<i))continue;
        dp[selected][nowPerson] = min(dp[selected][nowPerson], D[nowPerson][i]+dfs(nowPerson+1,selected|(1<<i),n));
    }
    return dp[selected][nowPerson];
}


int main(){
    
    int N;
    cin>>N;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin>>D[i][j];
        }
    }
    
    //dp[mask][now]=지금까지 고른거에서 출발해서 다고른..것
    dp[0][0]=dfs(0,0,N);
    cout<<dp[0][0];
    return 0;
}