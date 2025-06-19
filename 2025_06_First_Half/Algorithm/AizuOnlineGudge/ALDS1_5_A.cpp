#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

bool isCan(vector<int> A, int m, int i)
{
    
    if (m == 0)
        return true;
    if (m < 0)
        return false;
    if (i >= A.size())
        return false;
    return isCan(A, m - A[i], i + 1) ||
            isCan(A, m, i + 1);
}

int main()
{
    int n;
    cin >> n;
    vector<int> A(n);
    int q;
    vector<int> M(q);
    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
    }
    cin >> q;
    for (int i = 0; i < q; i++)
    {
        cin >> M[i];
    }
    for (int i = 0; i < q; i++)
    {
        if (isCan(A, M[i], 0))
        {
            cout << "yes" << endl;
        }
        else
        {
            cout << "no" << endl;
        }
    }
}
