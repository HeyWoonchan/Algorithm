#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

int main(){
    int grid[100][100];
    int visited[100][100];
    int N,M,r,c,len,nr,nc;
    int dr[4]={0,0,1,-1};
    int dc[4]={1,-1,0,0};
    string s;
    memset(visited,0,sizeof(visited));

    cin>>N>>M;
    for(int i=0;i<N;i++){
        cin>>s;
        for(int j=0;j<M;j++){
            grid[i][j]=(int)(s[j]-'0');
        }
    }
    

    queue<pair<int,pair<int,int>>> q;
    q.push({0,{0,0}});
    while(q.size()){
        len=q.front().first;
        r=q.front().second.first;
        c=q.front().second.second;
        q.pop();
        if (r==N-1 && c==M-1){
            cout<<len+1;
            return 0;
        }

        for (int i=0;i<4;i++){
            nr=r+dr[i];
            nc=c+dc[i];
            if (nr<0 || nr>=N || nc<0 || nc>=M){
                continue;
            }
            if (visited[nr][nc]==0 && grid[nr][nc]==1){
                visited[nr][nc]=1;
                q.push({len+1,{nr,nc}});
            }
        }
        
        
    }
    return 0;
}