#include <iostream>
#include <vector>
using namespace std;
vector<vector<int>> dp(2000, vector<int>(2000, -1));
vector<int> A;
bool isCan(int m, int i)
{
    if (m < 0)
        return false;
    else if (dp[i][m] != -1)
        return dp[i][m];
    else if (m == 0)
        dp[i][m] = 1;
    else if (i >= A.size())
        dp[i][m] = 0;
    else if (isCan(m, i + 1))
        dp[i][m] = 1;
    else if (isCan(m - A[i], i + 1))
        dp[i][m] = 1;
    else
        dp[i][m] = 0;
    return dp[i][m];
}
int main()
{
    int n;
    cin >> n;
    A.resize(n);
    int q;
    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
    }
    cin >> q;
    int m = 0;
    for (int i = 0; i < q; i++)
    {
        cin >> m;
        if (isCan(m, 0))
            cout << "yes" << endl;
        else
            cout << "no" << endl;
    }
    return 0;
}
