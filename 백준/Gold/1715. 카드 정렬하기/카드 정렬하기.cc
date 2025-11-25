#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main(){
    priority_queue<int, vector<int>, greater<int>> pq;
    int N;
    cin>>N;
    for(int i=0;i<N;i++){
        int n;
        cin>>n;
        pq.push(n);
    }
    int tmp1=0;
    int tmp2=0;
    int result=0;
    while(pq.size()!=1){
        tmp1=pq.top();
        pq.pop();
        tmp2=pq.top();
        pq.pop();
        result+=tmp1+tmp2;
        pq.push(tmp1+tmp2);
    }
    cout<<result<<"\n";
    return 0;
}