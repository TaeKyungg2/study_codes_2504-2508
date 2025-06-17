#include <iostream>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

int main()
{
    queue<pair<string, int>> qu;
    int n, qms, time = 0;
    cin >> n >> qms;
    pair<string, int> temp;
    for (int i = 0; i < n; i++)
    {
        cin >> temp.first >> temp.second;
        qu.push(temp);
    }
    while (!qu.empty())
    {
        temp = qu.front();
        qu.pop();
        if (temp.second > qms)
        {
            temp.second -= qms;
            qu.push(temp);
            time += qms;
        }
        else
        {
            time += temp.second;
            cout << temp.first << " " << time << endl;
        }
    }
    return 0;
}
