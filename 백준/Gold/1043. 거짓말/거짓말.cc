#include <iostream>
#include <vector>
using namespace std;


int find(int a, vector<int>& parent){
    if (parent[a]==-1){
        return a;
    }
    return find(parent[a], parent);
}

void unionn(int a, int b,vector<int>& parent){
    int aP = find(a,parent);
    int bP = find(b,parent);
    if (aP==bP){
        return;
    }
    if (aP<bP){
        parent[bP]=aP;
    }
    else{
        parent[aP]=bP;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N,M,t;
    cin>>N>>M;
    vector <int> parent(N+1,-1);
    int knowersN;
    cin>>knowersN;

    if (knowersN==0){
        cout<<M;
        return 0;
    }


    vector <int> knowers;
    vector <vector <int>> parties(M);
    for (int i=0;i<knowersN;i++){
        cin>>t;
        knowers.push_back(t);
    }
    for (int i=0;i<M;i++){
        cin>>t;
        for (int j=0;j<t;j++){
            int att;
            cin>>att;
            parties[i].push_back(att);
        }
    }

    //union작업시작
    for (int i=1;i<knowersN;i++){
        unionn(knowers[0],knowers[i],parent);
    }
    for (int i=0;i<M;i++){
        for (int j=1;j<parties[i].size();j++){
            unionn(parties[i][0], parties[i][j],parent);
        }
    }

    int ans=0;
    int knowershead = find(knowers[0],parent);

    for (int i=0;i<M;i++){
        bool flag = false;
        for (int j=0;j<parties[i].size();j++){
            if (find(parties[i][j],parent)==knowershead){
                flag=true;
                break;
            }
        }
        if (flag==0){
            ans+=1;
        }
    }

    cout<<ans;
    return 0;
}