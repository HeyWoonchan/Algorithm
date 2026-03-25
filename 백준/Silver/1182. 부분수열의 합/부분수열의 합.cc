#include <iostream>
#include <bitset>
using namespace std;

int main(){
    int N,S;
    cin>>N>>S;
    int arr[N];
    for (int i=0;i<N;i++){
        int x;
        cin>>x;
        arr[i]=x;
    }
    int max = (1<<N);
    
    int res=0;
    for (int i=0;i<max;i++){
        int nowSum=0;
        int index=0;
        for (int mask=1;mask<=max;mask<<=1,index++){
            if (mask&i){
                nowSum+=arr[index];
            }
            
        }
        if (i!=0 && nowSum==S){
            res++;
        }
    }
    cout<<res;
    return 0;
    
}