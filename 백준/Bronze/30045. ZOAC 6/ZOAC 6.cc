#include <iostream>
#include <string>
using namespace std;
int main(){
    int N,result=0;
    cin>>N;
    string s[N];
    for (int i=0;i<N;i++){
        cin>>s[i];
    }

    for (int i=0;i<N;i++){
        if (s[i].find("01")!=string::npos or s[i].find("OI")!=string::npos){
            result+=1;
        }
    }
    cout<<result;
    return 0;
}