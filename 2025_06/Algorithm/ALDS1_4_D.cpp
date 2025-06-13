#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
using namespace std;
// not completed..
vector<int> input(int n)
{
    vector<int> w(n);
    for (int i = 0; i < n; i++)
    {
        cin >> w[i];
    }
    return w;
}

int main() // to return minimum weight.(P)
{
    int n, k;
    cin >> n >> k; // k is the number of trucks
    vector<int> w = input(n);
    vector<int> truck(k, 0);
    sort(w.begin(), w.end(), greater<int>());
    int P = w[n - 1];
    vector<int>::iterator it;
    while (true)
    {
        int sum = 0;
        int j = 0;
        int sign = 1;

        for (it = w.begin(); it != w.end(); it++)
        {
            truck[j] += *it;

            if (j % (k - 1) == 0)
            {
                it++;
                truck[j] += *it;
                sign *= -1;
            }
            j += sign;
            if (truck[j] > P)
            {
                truck[j] -= *it;
                it = upper_bound(it, w.end(), truck[j] - P);
                if (it == w.end())
                {
                    break;
                }
            }
        }
        P++;
    }
}
