#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#define INF 1LL<<60

using namespace std;

typedef long long LL;

vector <LL> dijkstra(int start, int end, vector <vector<pair<int,int>>>& graph){
    vector<LL> dist(graph.size(), INF);
    priority_queue<pair<LL,int>, vector<pair<LL,int>>, greater<pair<LL,int>>> hq;
    hq.push({0,start});
    dist[start]=0;
    while (hq.size()){
        LL nowCost = hq.top().first;
        LL nowNode = hq.top().second;
        hq.pop();

        if (dist[nowNode]<nowCost){
            continue;
        }
        for(auto nextPair: graph[nowNode]){
            LL nextNode = nextPair.first;
            LL newCost = nextPair.second+nowCost;

            if (dist[nextNode]>newCost){
                dist[nextNode]=newCost;
                hq.push({newCost,nextNode});
            }
            
        }
    }

    return dist;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N,E;
    cin>>N>>E;

    vector <vector<pair<int,int>>> graph(N+1);

    for (int i=0;i<E;i++){
        int a,b,c;
        cin>>a>>b>>c;
        graph[a].push_back({b,c});
        graph[b].push_back({a,c});
    }

    int v1,v2;
    cin>>v1>>v2;

    vector <LL> dist0 = dijkstra(1,N,graph);
    vector <LL> dist1 = dijkstra(v1,v2,graph);
    // vector <LL> dist2 = dijkstra(v2,N,graph);

    LL oneTov1,ontTov2,v1Tov2,v2Tov1,v1ToN,v2ToN;

    if (v1==1){
        oneTov1=0;
    }
    else {
        oneTov1=dist0[v1];
    }
    v1ToN=dist1[N];
    v1Tov2 = dist1[v2];
    ontTov2 = dist0[v2];
    if (v2==N){
        v2ToN=0;
    }
    else {
        v2ToN=dijkstra(v2,N,graph)[N];
    }
    LL firstOption = oneTov1+v1Tov2+v2ToN;
    LL secondOption = ontTov2+v1Tov2+v1ToN;
    LL ans = min({firstOption,secondOption});
   if (ans >= INF/2){
        cout<<-1;
    }
    else{
        cout<<ans;
    }
    // cout<<firstOption<<" "<<secondOption<<'\n';
    // cout<<"dist0\n";

    // cout<<'\n';

    return 0;


        


}