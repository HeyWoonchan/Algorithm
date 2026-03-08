#include <iostream>
#include <vector>

using namespace std;

int main(){
    int N,M;
    cin>>N>>M;
    
    vector <int> firstTable;
    for (int i=0;i<N;i++){
        int rank;
        cin>>rank;
        firstTable.insert(firstTable.begin()+rank-1, i);

    }
    vector <int> secondTable;
    for (int i=0;i<M;i++){
        int rank;
        cin>>rank;
        secondTable.insert(secondTable.begin()+rank-1,firstTable[M-1-i]);
    }
    for (int i=0;i<3;i++){
        cout<<secondTable[i]+1<<'\n';
    }
    return 0;
}