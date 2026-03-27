#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>
using namespace std;

int main(){
    int N, X;
    long L,R;
    cin>>N>>L>>R>>X;
    vector<long> A(N);
    for (int i=0;i<N;i++){
        cin>>A[i];
    }
    int answer=0;
    for (long i=0;i<(1<<N);i++){
        // cout<<bitset<15>(i)<<"i\n";
        long tSum = 0;
        long minDifficulty=1000000000;
        long maxDifficulty=0;
        for(int j=0;j<N;j++){
            // cout<<bitset<15>((1L<<j))<<"1<<j\n";
            if (i&(1<<j)){
                tSum+=A[j];
                minDifficulty=min(minDifficulty,A[j]);
                maxDifficulty=max(maxDifficulty,A[j]);
            }
        }
        // cout<<tSum<<' '<<minDifficulty<<' '<<maxDifficulty<<'\n';
        if (tSum>=L && tSum<=R && (maxDifficulty-minDifficulty>=X)){
            answer++;
        }
    }

    cout<<answer;
    return 0;
}