#include <iostream>
#include <vector>
#include <stdio.h>
#include <stack>
#include <numeric>
using namespace std;

int main()
{
    string g;
    cin >> g;
    stack<int> st;
    vector<int> area;
    int i = 0;
    area.push_back(0);
    for (char x : g)
    {
        if (area.back() != 0 && x == '\\')
        {
            area.push_back(0);
        }
        if (x == '\\')
        {
            st.push(i);
        }
        else if (x == '/' && !st.empty())
        {
            int frontNum = st.top();
            st.pop();
            area.back() += i - frontNum;
        }
        i++;
    }
    if (area.back() == 0)
    {
        area.pop_back();
    }
    int sum = accumulate(area.begin(), area.end(), 0);
    cout << sum << endl;
    cout << area.size() << " ";
    for (auto it = area.begin(); it != area.end(); ++it)
    {
        cout << *it;
        if (next(it) != area.end())
        {
            cout << " ";
        }
    }
}