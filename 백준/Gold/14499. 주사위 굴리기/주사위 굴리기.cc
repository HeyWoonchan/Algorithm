#include <iostream>
using namespace std;
struct _dice{
    int bot;
    int top;
    int up;
    int down;
    int left;
    int right;
} dice;
struct _dicePos{
    int r;
    int c;
} dicePos;
int N,M;
int grid[20][20];




void right(_dice &d){
    int tL, tB, tR, tT;
    tL=d.bot;
    tB=d.right;
    tR=d.top;
    tT=d.left;
    d.left=tL;
    d.bot=tB;
    d.right=tR;
    d.top=tT;
}

void left(_dice &d){
    int tL, tB, tR, tT;
    tL=d.top;
    tB=d.left;
    tR=d.bot;
    tT=d.right;
    d.left=tL;
    d.bot=tB;
    d.right=tR;
    d.top=tT;
}

void up(_dice &d){
    int tU,tB,tD,tT;
    tU = d.top;
    tB = d.up;
    tD = d.bot;
    tT = d.down;
    d.top = tT;
    d.bot = tB;
    d.up = tU;
    d.down = tD;
}

void down(_dice &d){
    int tU,tB,tD,tT;
    tU = d.bot;
    tB = d.down;
    tD = d.top;
    tT = d.up;
    d.top = tT;
    d.bot = tB;
    d.up = tU;
    d.down = tD;
}

void botWork(_dice &d, _dicePos &p){
        if (grid[p.r][p.c]==0){
            grid[p.r][p.c]=d.bot;
        }
        else{
            d.bot = grid[p.r][p.c];
            grid[p.r][p.c]=0;
        }
}

int main(){
    int K;
    cin>>N>>M>>dicePos.r>>dicePos.c>>K;
    for(int i=0;i<N;i++){
        for (int j=0;j<M;j++){
            cin>>grid[i][j];
        }
    }
    dice.top = 0;
    dice.left=0;
    dice.right=0;
    dice.up=0;
    dice.down=0;
    dice.bot=0;


    int commands[1000];
    for(int i=0;i<K;i++){
        cin>>commands[i];
    }

    
    
    for(int i=0;i<K;i++){
        int command = commands[i];
        switch(command){
            case 1:
                if (dicePos.c+1<M){
                    right(dice);
                    dicePos.c+=1;
                    botWork(dice,dicePos);
                    cout<<dice.top<<'\n';
                }
                break;
            case 2:
                if (dicePos.c-1>=0){
                    left(dice);
                    dicePos.c-=1;
                    botWork(dice,dicePos);
                    cout<<dice.top<<'\n';
                }
                break;
            case 3:
                if (dicePos.r-1>=0){
                    up(dice);
                    dicePos.r-=1;
                    botWork(dice,dicePos);
                    cout<<dice.top<<'\n';
                }
            break;
            case 4:
                if (dicePos.r+1<N){
                    down(dice);
                    dicePos.r+=1;
                    botWork(dice,dicePos);
                    cout<<dice.top<<'\n';
                
                }            
                break;
            default:
            break;
        }
    }
}