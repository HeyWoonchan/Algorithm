#include <iostream>
#include <cstring>
using namespace std;

const int MOD = 1000000000;
int dp[101][10][1 << 10];

int dfs(int pos, int nowNum, int mask, int N) {
    if (pos == N - 1) {
        return (mask == ((1 << 10) - 1)) ? 1 : 0;
    }

    int &ret = dp[pos][nowNum][mask];
    if (ret != -1) return ret;

    ret = 0;

    if (nowNum > 0) {
        ret = (ret + dfs(pos + 1, nowNum - 1, mask | (1 << (nowNum - 1)), N)) % MOD;
    }
    if (nowNum < 9) {
        ret = (ret + dfs(pos + 1, nowNum + 1, mask | (1 << (nowNum + 1)), N)) % MOD;
    }

    return ret;
}

int main() {
    int N;
    cin >> N;

    memset(dp, -1, sizeof(dp));

    int ans = 0;
    for (int i = 1; i < 10; i++) {
        ans = (ans + dfs(0, i, 1 << i, N)) % MOD;
    }

    cout << ans;
    return 0;
}