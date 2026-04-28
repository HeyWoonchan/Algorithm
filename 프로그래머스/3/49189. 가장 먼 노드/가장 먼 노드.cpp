#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    int ans = 0;
    vector<vector<int>> graph(n);
    for(int i=0;i<edge.size();i++){
        int a,b;
        a = edge[i][0];
        b = edge[i][1];
        a--;
        b--;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    
    queue<pair<int,int>> q;
    vector<int> visited(n,-1);
    q.push({0,0});
    visited[0]=1;
    while (!q.empty()){
        int node, cnt;
        node = q.front().first;
        cnt = q.front().second;
        q.pop();
      
        for(int i=0;i<graph[node].size();i++){
       
            int nextNode=graph[node][i];
            if (visited[nextNode]==-1){
                visited[nextNode]=cnt+1;
                q.push({nextNode, cnt+1});
            }
        }
    }
    
    for(int i=0;i<n;i++){
        ans = max(ans,visited[i]);
        // cout<<visited[i]<<' ';
    }
    int cnt=0;
    for(int i=0;i<n;i++){
        if(ans==visited[i])cnt++;
    }
    
    return cnt;
}