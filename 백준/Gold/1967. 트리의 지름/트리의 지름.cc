#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <queue>
#define INF INT_MAX
using namespace std;

vector <int> dijkstra(int start,vector <vector<pair<int,int>>>& graph){

    priority_queue<pair<int,int>, vector<pair<int,int>>,greater<pair<int,int>>> hq;

    vector <int> dist(graph.size(),INF);
    dist[start]=0;
    hq.push(make_pair(0,start));

    while (hq.size()){
        int nowNode = hq.top().second;
        int nowCost = hq.top().first;
        hq.pop();
        if (dist[nowNode]<nowCost){
            continue;
        }
        for (int i=0;i<graph[nowNode].size();i++){
            int nextNode = graph[nowNode][i].first;
            int newCost = nowCost+graph[nowNode][i].second;

            if (dist[nextNode]>newCost){
                dist[nextNode]=newCost;
                hq.push(make_pair(newCost,nextNode));
            }
        }
    }
    return dist;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin>>n;

    vector <vector<pair<int,int>>> graph(n+1);

    for (int i=0;i<n-1;i++){
        int a,b,c;
        cin>>a>>b>>c;
        graph[a].push_back(make_pair(b,c));
        graph[b].push_back(make_pair(a,c));
    }

    vector <int> first = dijkstra(1,graph);

    pair<int,int> firstMax;

    for (int i=0;i<first.size();i++){
        if (first[i]<INF){
            firstMax = {first[i],i};
            break;
        }
    }
    

    for (int i=0;i<first.size();i++){
        if (first[i]<INF){
        if (firstMax.first<first[i]){
            firstMax = {first[i],i};
        }}
    }
    // cout<<firstMax.first<<' '<<firstMax.second<<endl;
    
    vector<int> second = dijkstra(firstMax.second,graph);

    int secondMax = 0;
    for (int i=0;i<second.size();i++){
        if (second[i]>=INF){
            continue;
        }
        secondMax = max({secondMax,second[i]});

    }

    // for (auto a:second){
    //     cout<<a<<' ';
    // }
    cout<<secondMax;
    return 0;
}