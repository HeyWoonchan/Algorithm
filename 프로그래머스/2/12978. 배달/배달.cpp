#include <iostream>
#include <vector>
#include <algorithm>

int MAX = 1e9;
using namespace std;

int solution(int N, vector<vector<int>> road, int K) {
    int answer = 0;
    vector<vector<int>>adj_mat(N,vector<int>(N,MAX));
    
    for (int i=0;i<road.size();i++){
        int a,b,c;
        a = road[i][0];
        b = road[i][1];
        c = road[i][2];
        a--;b--;
        adj_mat[a][b]=min(adj_mat[a][b],c);
        adj_mat[b][a]=min(adj_mat[b][a],c);
    }
    
    for (int k=0;k<N;k++){
        for(int i=0;i<N;i++){
            for (int j=0;j<N;j++){
                if (i==j)continue;
                adj_mat[i][j] = min(adj_mat[i][j], adj_mat[i][k]+adj_mat[k][j]);
            }
        }
    }
    for (int i=1;i<N;i++){
        if (adj_mat[0][i]<=K){
            answer++;
        }
    }

    return answer+1;
}