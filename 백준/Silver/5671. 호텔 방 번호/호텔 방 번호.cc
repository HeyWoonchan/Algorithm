#include <iostream>
#include <string>
using namespace std;

bool check(int i){
    string target=to_string(i);
    int nums[10]={0,};
    for (char a:target){
        nums[a-'0']++;
    }
    for (int i : nums){
        if (i>1){
            return true;
        }
    }
    return false;
}

int main(){
    int N,M;
    int test=0;
    while (1){
        test=0;
        cin>>N>>M;
        if (cin.eof())break;
        for (int i=N;i<=M;i++){
            if (!check(i)){
                test++;
            }
        }
        cout<<test<<'\n';
    }
    return 0;
}