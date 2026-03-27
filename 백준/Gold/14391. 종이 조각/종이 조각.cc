#include <iostream>
#include <vector>
#include <bitset>
#include <algorithm>
using namespace std;
int main(){
    int N,M;
    cin>>N>>M;
    vector<vector<int>> board(N, vector<int>(M));
    for(int i=0;i<N;i++){
        string s;
        cin>>s;
        for (int j=0;j<M;j++){
            board[i][j]=(int)(s[j]-'0');
        }
    }
    int ans=0;
    for(int i=0;i<(1<<(N*M));i++){
        // cout<<bitset<10>(i)<<'\n';
        int nowSum=0;
        
        //가로더하기 시작
        for (int r=0;r<N;r++){
            int fSum=0;
            int tSum=0;
            int conFlag=1;
            for(int c=0;c<M;c++){
                if (i&(1<<(M*r+c))){
                    if (conFlag){
                        tSum = tSum*10+board[r][c];
                    }
                    else{
                        fSum+=tSum;
                        tSum=board[r][c];
                        conFlag=1;
                    }
                }
                else{
                    conFlag=0;
                }
            }
            nowSum+=fSum+tSum;
        }
        // int j= ((1<<(N*M))-1)^i;
        for (int c=0;c<M;c++){
            int fSum=0;
            int tSum=0;
            int conFlag=1;
            for(int r=0;r<N;r++){
                if ((i&(1<<(M*r+c)))==0){
                    if (conFlag){
                        tSum = tSum*10+board[r][c];
                    }
                    else{
                        fSum+=tSum;
                        tSum=board[r][c];
                        conFlag=1;
                    }
                }
                else{
                    conFlag=0;
                }
            }
            nowSum+=fSum+tSum;
        }
        ans=max(ans,nowSum);
    }
    cout<<ans;
}