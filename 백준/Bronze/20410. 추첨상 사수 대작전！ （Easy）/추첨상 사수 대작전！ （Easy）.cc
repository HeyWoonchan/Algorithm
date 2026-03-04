#include <iostream>
using namespace std;

int main(){
    int m, seed, X1, X2;
    cin>>m>>seed>>X1>>X2;
    for (int i=0;i<m;i++){
        for (int j=0;j<m;j++){
            if (X1==(i*seed+j)%m && X2==(i*X1+j)%m){
                cout<<i<<' '<<j;
                return 0;
            }
        }
    }
    return 0;
}