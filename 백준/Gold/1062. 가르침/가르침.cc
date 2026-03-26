#include<iostream>
#include<string>
#include<algorithm>
#include <bitset>
typedef long long LL;

using namespace std;
int N, K;
int result=0;

int dfsNum=0;

void dfs(int depth,int idx, LL mask,vector<LL> &wordsBit){
    // dfsNum++;
    if (depth==K-5){
        // cout<<bitset<26>(mask)<<"dfs"<<'\n';
        int tRes=0;
        for (int i=0;i<N;i++){
            if ((wordsBit[i] & ~mask) ==0){
                tRes++;
            }
        }
        result = max(result,tRes);
        return;
    }
    
    for (int i=idx;i<26;i++){
        if ((mask&(1LL<<i))==0){
            dfs(depth+1,i+1, mask|(1LL<<i),wordsBit);
        }
    }

}

int main(){
    
    cin>>N>>K;
    string S;
    vector <LL> wordsBit(N,0);
    for (int i=0;i<N;i++){
        cin>>S;
        for (int j=0;j<S.length();j++){
            wordsBit[i] |= (1LL<<(S[j]-'a'));
        }
    }
    if (K<5){
        cout<<0;
        return 0;
    }
    long long base = 0;
    base |= (1LL << ('a' - 'a'));
    base |= (1LL << ('n' - 'a'));
    base |= (1LL << ('t' - 'a'));
    base |= (1LL << ('i' - 'a'));
    base |= (1LL << ('c' - 'a'));
    dfs(0,0,base,wordsBit);
    // cout<<dfsNum<<'\n';
    cout<<result;
    
    return 0;
}