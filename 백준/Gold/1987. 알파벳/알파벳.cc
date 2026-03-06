#include <iostream>
#include <algorithm>
using namespace std;

void solve(int depth, int r, int c, int R, int C, int visited[][20], int grid[][20],int* alphaM, int* ans){
    *ans = max({*ans, depth});
    // cout<<"solve징입"<<'\n';
    pair<int, int> D[4]= {{0,1},{0,-1},{1,0},{-1,0}};
    // cout<<grid[0][0]<<endl;
    for (int i=0;i<4;i++){
        int dr, dc, nr, nc;
        pair<int, int> dPair = D[i];
        dr = dPair.first;
        dc = dPair.second;

        nr = r+dr;
        nc = c+dc;
        if (!((0<=nr && nr<R) && (0<=nc && nc<C))){
            continue;
        }
        if (visited[nr][nc]==0 && alphaM[grid[nr][nc]-'A']==0){
            alphaM[grid[nr][nc]-'A']=1;
            visited[nr][nc]=1;
            solve(depth+1,nr,nc,R,C,visited,grid,alphaM,ans);
            alphaM[grid[nr][nc]-'A']=0;
            visited[nr][nc]=0;
        }
    }
}

int main(){
    int R, C;
    cin>>R>>C;

    int grid[20][20];

    for (int i=0;i<R;i++){
        string s;
        cin>>s;
        for (int j=0;j<C;j++){
            grid[i][j]=s[j];
        }
    }

    int visited[20][20];
    for (int i=0;i<R;i++){
        for (int j=0;j<C;j++){
            visited[i][j]=0;
        }
    }
    int Ans=1;
    int alphaVisited[26]={0,};

    alphaVisited[grid[0][0]-'A']=1;
    visited[0][0]=1;
    // cout<<"진입전"<<'\n';
    solve(1,0,0,R,C,visited,grid,alphaVisited,&Ans);
    cout<<Ans;
}