#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int n;
    cin>>n;
    int tmp;
    vector<int> arr;
    for(int i=0;i<n;i++){
        cin>>tmp;
        arr.push_back(tmp);
    }
    sort(arr.begin(), arr.end());
    for(int i=0;i<n;i++){
        cout<<arr[i]<<'\n';
    }
    return 0;
}