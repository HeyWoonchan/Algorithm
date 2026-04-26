#include <string>
#include <queue>
#include <vector>
#include <algorithm>
#include <iostream>

typedef long long LL;

using namespace std;
int solution(vector<int> queue1, vector<int> queue2) {
    // 실행 불가 조건: 모든 원소의 합이 홀수일 경우, 1개밖에 없는 상황에서 둘이 다를 경우
    LL qSums[2]={0,0};
    queue<int> q1;
    queue<int> q2;
    for(int i=0;i<queue1.size();i++){
        qSums[0]+=(LL)queue1[i];
        qSums[1]+=(LL)queue2[i];
        q1.push(queue1[i]);
        q2.push(queue2[i]);
    }
    if (queue1.size()==1 && queue1[0]!= queue2[0]){
        return -1;
    }
  
    int MAXCNT = queue1.size()*4;
    int answer = -2;
    int cnt=0;
    while (qSums[0]!=qSums[1] && cnt<MAXCNT){
        if (qSums[0]>qSums[1]){
            int q1p=q1.front();
            q1.pop();
            q2.push(q1p);
            qSums[0]-=q1p;
            qSums[1]+=q1p;
        }
        else{
            int q2p=q2.front();
            q2.pop();
            q1.push(q2p);
            qSums[1]-=q2p;
            qSums[0]+=q2p;
        }
        cnt++;
    }
    
    if (cnt>=MAXCNT){
        return -1;
    }
    return cnt;
}