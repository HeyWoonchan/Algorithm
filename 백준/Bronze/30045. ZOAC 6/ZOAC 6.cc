#include <iostream>
#include <string>
using namespace std;
int main(){
    int N,result=0;
    cin>>N;
    string s;
    

    for (int i=0;i<N;i++){
        cin>>s;
        if (s.find("01")!=string::npos or s.find("OI")!=string::npos){
            result+=1;
        }
    }
    cout<<result;
    return 0;
}