#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
int dp[1<<15][15][10];
int C[15][15];
int ans=0;

void dfs(int depth, int mask, int nowArtist, int lastCost, int maxPeople){
    // cout<<"dfs"<<depth<<'\n';
    ans = max(ans,depth);

    int &res = dp[mask][nowArtist][lastCost];
    if (res!=-1){
        return;
    }
    res=1;

    for(int nextArtist=0;nextArtist<maxPeople;nextArtist++){
        if ((mask&(1<<nextArtist))==0 && (lastCost<=C[nowArtist][nextArtist])){
            
            dfs(depth+1,mask|(1<<nextArtist),nextArtist,C[nowArtist][nextArtist],maxPeople);
            
        }  
    }

}

int main(){
    memset(dp,-1, sizeof(dp));

    int N;
    cin>>N;
    string s;
    for(int i=0;i<N;i++){
        cin>>s;
        for(int j=0;j<N;j++){
            C[i][j]=(int)(s[j]-'0');
        }
    }
    // cout<<C[1][0];
    dfs(1,1,0,0,N);
    cout<<ans;
}