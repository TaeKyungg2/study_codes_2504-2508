#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

int main()
{
    int sNum = 0, tNum = 0;
    cin >> sNum;
    vector<int> s(sNum);
    for (int i = 0; i < sNum; i++)
    {
        cin >> s[i];
    }
    cin >> tNum;
    vector<int> t(tNum);
    for (int i = 0; i < tNum; i++)
    {
        cin >> t[i];
    }
    int count = 0;
    for (int i = 0; i < sNum; i++)
    {
        for (int j = 0; j < tNum; j++)
        {
            if (s[i] == t[j])
            {
                count++;
                t[j] = -1;
            }
        }
    }
    cout << count << endl;
}
