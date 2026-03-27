#include <iostream>
#include <bitset>
using namespace std;
static unsigned int bits[1048576]={0,};
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    while (1){

        int a;
        cin>>a;
        if (cin.eof()){
            break;
        }
        
        if(bits[a/32] & (1LL<<(a%32))){
            continue;
        }
        else{
            bits[a/32] |= (1LL<<(a%32));
            cout<<a<<' ';
        }
    }
    return 0;
}