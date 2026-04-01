#include <iostream>
#include <bitset>
#include <algorithm>
#include <cstring>
#include <string>
using namespace std;
int N,P;
int C[16][16];
int dp[1<<16];
const int INF = 1e9;
//dp[nowOnMask]
//nowOnMask(현재 켜진 것)에서부터 앞으로 켜는 법의 최소비용.
//현재 켜진 것 들 중 i를 켜는 최솟값,다음 켤 것(i)
//이미 다 켜서 켤 것이 없다면 0?
int dfs(int nowOnMask){
    if (__builtin_popcount(nowOnMask)>=P)return 0;
    
    // cout<<bitset<5>(nowOnMask)<<'\n';
    int &ret=dp[nowOnMask];
    if (ret!=-1)return ret;
    
    ret = INF;
    for(int i=0;i<N;i++){ //i: 앞으로 켤 것
        if (nowOnMask&(1<<i))continue; //이미 켠 것은 또 켜지 말 것
        for (int j=0;j<N;j++){ //j 이미 켜진 것들 중에서 최소비용 볼 것.
            if ((nowOnMask&(1<<j))==0) continue; //켜지지 않은 것은 제외
            ret=min(ret, C[j][i]+dfs(nowOnMask|(1<<i))); //앞으로 켤 것 중 최솟값+지금 켠 것 포함 앞으로 켜질 것들 중 최솟값
        }
    }
    return ret;
}

int main(){
    memset(dp,-1,sizeof(dp));
    cin>>N;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin>>C[i][j];
        }
    }
    string s;
    cin>>s;
    cin>>P;
    int initMask=0;
    for(int i=0;i<N;i++){
        if(s[i]=='Y'){
            initMask|=(1<<i);
        }
    }
    if (__builtin_popcount(initMask)>=P){
        cout<<0;
        return 0;
    }
    int ans=dfs(initMask);
        // cout<<"ansTmp:"<<ans<<'\n'
    if (ans==INF){
        cout<<-1;
        return 0;
    }
    cout<<ans;

}