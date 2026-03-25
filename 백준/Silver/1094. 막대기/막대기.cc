#include <iostream>
using namespace std;

int main(){
    int X;
    cin>>X;
    int check=64;
    int result=0;
    while(check>0){
        if (check & X){
            result+=1;
        }
        check>>=1;
    }
    cout<<result;
    return 0;
}