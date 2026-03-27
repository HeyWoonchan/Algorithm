#include <iostream>
#include <vector>
#include <queue>
#include <bitset>
using namespace std;

typedef long long LL;

int bfs(int node, vector<vector<int>> &graph, LL mask){
    int N = graph.size();
    vector<int> visited(N,0);
    visited[node]=1;

    queue<int> q;
    q.push(node);
    while (q.size()){
        int nowNode = q.front();
        q.pop();

        for (int i=0;i<graph[nowNode].size();i++){
            int nextNode = graph[nowNode][i];
            if ((mask&(1<<nextNode))==0)continue;
            if (visited[nextNode]==0){
                visited[nextNode]=1;
                q.push(nextNode);
            }
        }
    }
    //요구하는 마스크의 노드가 모두 방문 되었는지 확인

    for (int i=0;i<N;i++){
        if ((mask&(1LL<<i)) && visited[i]==0){
            return 0;
        }
    }
    return 1;
}

int main(){
   
    int N; 
    cin>>N;
    vector<int> population(N);
    vector<vector<int>> graph(N);

    for(int i=0;i<N;i++){
        cin>>population[i];
    }
    for(int i=0;i<N;i++){
        int M;
        cin>>M;
        for (int j=0;j<M;j++){
            int near;
            cin>>near;
            graph[i].push_back(near-1);
            graph[near-1].push_back(i);
        }
    }

    int answer = 902;
    for (LL i=1;i<(1LL<<N)-2;i++){
        for (LL j=i+1;j<(1LL<<N)-1;j++){
            if (((i&j)==0) && ((i|j)==(1<<N)-1)){
                int iNode=0;
                int jNode=0;
                while ((i & (1LL<<iNode))==0){
                    iNode++;
                }
                while ((j & (1LL<<jNode))==0){
                    jNode++;
                }
                bool iConnectedFlag = bfs(iNode,graph,i); //i 선거구가 이어져있는지 확인
                bool jConnectedFlag = bfs(jNode,graph,j); //j 선거구가 이어져있는지 확인

                if (iConnectedFlag&&jConnectedFlag){
                    int iSum=0;
                    int jSum=0;
                    for (int k=0;k<N;k++){
                        if (i&(1LL<<k)){
                            iSum+=population[k];
                        }
                    }
                    for (int k=0;k<N;k++){
                        if (j&(1LL<<k)){
                            jSum+=population[k];
                        }
                    }
                    answer = min(answer,abs(iSum-jSum));
                }
            }
        }
    }

    if (answer==902){
        cout<<-1;
    }
    else{
        cout<<answer;
    }
    return 0;

}