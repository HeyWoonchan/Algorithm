#include <string>
#include <vector>
#include <queue>
#include <map>

using namespace std;

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    
    
    int visited[50]={0,};
    queue<pair<string, int>> q;
    q.push({begin,0});

    while (q.size()){
        string nowStr = q.front().first;
        int cnt = q.front().second;
        q.pop();

        if (nowStr == target){
            return cnt;
        }

        for (int i=0;i<words.size();i++){
            int diffCnt=0;
            for (int j=0;j<words[i].length();j++){
                if (nowStr[j]!=words[i][j]){
                    diffCnt++;
                }
            }
            if (diffCnt==1 && visited[i]==0){
                visited[i]=1;
                q.push({words[i],cnt+1});
            }
        }

    }
    
    
    return 0;
}