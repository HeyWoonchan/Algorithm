#include <iostream>
using namespace std;

bool isPelinedrome(string s, int l, int r){
    if (l>r || s.length()==1){
        return true;
    }
    if (s[l]!=s[r]) {
        return false;
    }
    return isPelinedrome(s,l+1,r-1);
}

long long satoi(string s){
    long long t=0;
    for (int i=0;i<s.length();i++){
        long long j = 1;
        for (int k=0;k<(s.length()-i-1);k++){
            j*=10;
        }
        t+=j*(s[i]-'0');
    }
    return t;
}
int main(){
    int n;
    long long ans=0;
    string tStr;
    cin>>n;
    getchar();
    
    for (int i=0;i<n;i++){
        cin>>tStr;
        if (isPelinedrome(tStr,0,tStr.length()-1)){
            ans+=satoi(tStr);
        }
    }
    cout<<ans;
    // for (string& a : strs){
    //     cout<<a<<endl;
    // }
    
    return 0;
}