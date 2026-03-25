#include <iostream>
using namespace std;

int main(){
    int have = 64;

    int X;
    cin>>X;
    int haveArr[7]={0,};
    haveArr[6]=1;

    //지민이가 가지고 있는 막대의 길이를 모두 더한다
    int t = 1;
    int haveSum=0;
    for (int i=0;i<7;i++){
        if(haveArr[i]>0){
            haveSum+=haveArr[i]*t;
        }
        t*=2;
    }
    
    //이때 합이 X보다 크다면, 아래 과정을 반복한다.
    while (haveSum>X){
        //가지고 있는 막대 중, 길이가 가장 짧은 것을 절반으로 자른다.
        int halfIndex=0;
        for (int i=0;i<7;i++){
            if(haveArr[i]>0){
                if (i!=0){
                    haveArr[i]-=1;
                    haveArr[i-1]+=2;
                    halfIndex=i-1;
                }
                break;
            }
        }
        //만약 위에서 자른 막대의 절반 중 하나를 버리고 남아있는 막대의 길이의 합이 X보다 크거나같다면
        int t = 1;
        haveSum=0;
        for (int i=0;i<7;i++){
            if(haveArr[i]>0){
                if (i==halfIndex)haveSum+=(haveArr[i]-1)*t;
                else haveSum+=haveArr[i]*t;
            }
            t*=2;
        }
        if (haveSum>=X){
            //하나를버린다.
            haveArr[halfIndex]-=1;
        }
        else{
            int t=1;
            for (int i=0;i<halfIndex;i++){
                t*=2;
            }
            haveSum+=t;
        }
        
    }
    
    int result=0;
    for (auto a:haveArr){
        if(a>0){
            result++;
        }
    }
    cout<<result;
}