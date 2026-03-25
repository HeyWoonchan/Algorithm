#include <iostream>
#include <math.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int M;
    cin>>M;
    long long S= 0;
    while(M--){
        string command;
        int x;
        cin>>command;
        if (command=="add"){
            cin>>x;
            S |= 1<<x;
        }
        else if (command=="remove"){
            cin>>x;
            S&= ~(1<<x);
        }
        else if (command=="check")
        {
            cin>>x;
            int res=S&(1<<x)?1:0;
            cout<<res<<'\n';
        }
        else if (command=="toggle"){
            cin>>x;
            if (S&(1<<x)){
                S&=~(1<<x);
            }
            else{
                S|=(1<<x);
            }
        }
        else if (command=="all")
        {
            S=(1<<21)-1;
        }
        else{
            S=0;
        }
        
        
        
    }
    return 0;
}