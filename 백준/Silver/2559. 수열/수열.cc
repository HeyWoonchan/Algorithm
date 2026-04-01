#include<iostream>
#include<algorithm>
using namespace std;
int temps[100000];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int N,K;
    cin>>N>>K;
    int tSum=0;
    for (int i=0;i<N;i++){
        cin>>temps[i];
    }
    
    for (int i=0;i<K;i++){
        tSum+=temps[i];
    }
    int l=0;
    int r = K-1;
    
    int ans = tSum;
    while (r<N){
        ans = max(ans,tSum);
        tSum-=temps[l++];
        tSum+=temps[++r];
    }
    
    cout<<ans;
    return 0;

}