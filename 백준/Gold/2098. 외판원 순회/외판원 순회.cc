#include <iostream>
#include <algorithm>
using namespace std;

const int INF = 1e9;
int W[16][16];

int main(){
    int N;
    cin>>N;
    for (int i=0;i<N;i++){
        for (int j=0;j<N;j++){
            cin>>W[i][j];
        }
    }
    // cout<<N<<'\n';
    vector<vector<int>> dp((1<<N),vector<int>(N,INF));
    dp[1][0]=0;
    //dp[mask|(1<<nextNode)][nextNode] = min(dp[mask][nextNode], dp[Mask|(1<<nextNode)][]+W[prev][nowNode])
    for(int mask=0;mask<(1<<N)-1;mask++){
        for(int now=0;now<N;now++){
            if ((mask&(1<<now))==0){ //현재 방문 마스크 확인
                continue;
            }
            for (int next=0;next<N;next++){
                if (W[now][next]==0){
                    continue;
                }
                if (mask&(1<<next)){
                    continue;
                }

                dp[mask|(1<<next)][next]=min(dp[mask|(1<<next)][next], dp[mask][now]+W[now][next]);

            }
        }    
    }
    int ans=INF;
    for(int i=1;i<N;i++){
        if (W[i][0]==0)continue;
        ans = min(ans,dp[(1<<N)-1][i]+W[i][0]);
    }
    cout<<ans;
}