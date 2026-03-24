#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N,M,n,t;
    cin>>N>>M;
    string command;
    vector<pair<int,int>> posts;
    for (int i=0;i<N;i++){
        cin>>command;
        if (command=="order"){
            cin>>n>>t;
            posts.push_back({t,n});
            cout<<"";
        }
        else if(command=="sort"){
            sort(posts.begin(),posts.end());
        }
        else{
            cin>>n;
            int find=-1;
            for (int i=0;i<posts.size();i++){
                if (posts[i].second==n){
                    find=i;
                    break;
                }
            }
            if(posts.size())posts.erase(posts.begin()+find);
        }
        if (posts.size()){
            for (pair<int,int> a:posts){
                cout<<a.second<<" ";
            }
        }
        else{
            cout<<"sleep";
        }
        cout<<'\n';
    }

    return 0;
}