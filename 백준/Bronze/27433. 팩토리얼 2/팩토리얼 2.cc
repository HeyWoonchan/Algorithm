#include <iostream>

using namespace std;

int main(){
    long long int f=1;
    long long int n;
    cin>>n;
    for(long long int i=1;i<=n;i++){
        f*=i;
    }
    cout<<f;
}