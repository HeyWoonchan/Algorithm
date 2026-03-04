#include <iostream>
#include <vector>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, t, ans=0;
    cin>>N;
    vector<vector<int>> originGrid(N, vector<int>(N,0));
    vector <vector<vector <int>>> dp(3, vector<vector<int>>(N,vector<int>(N,0)));

    for (int i=0;i<N;i++){
        for (int j=0;j<N;j++){
            cin>>t;
            originGrid[i][j]=t;
        }
    }
    dp[0][0][1]=1;
    for (int i=0;i<N;i++){
        for (int j=2;j<N;j++){
            if (originGrid[i][j]==1) continue;
            dp[0][i][j]+=dp[0][i][j-1]+dp[1][i][j-1];
            if (i>0){
                if (!(originGrid[i][j-1]==1 || originGrid[i-1][j]==1)){
                    for(int k=0;k<3;k++){
                        dp[1][i][j]+=dp[k][i-1][j-1];
                    }
                }
            }
            if (i>0){
                dp[2][i][j]+=dp[2][i-1][j]+dp[1][i-1][j];
            }
        }
    }
    for(int i=0;i<3;i++){
        ans+=dp[i][N-1][N-1];
    }
    // for(auto& a: dp){
    //     ans+=a[N-1][N-1];
    // }
    cout<<ans;
    return 0;
}