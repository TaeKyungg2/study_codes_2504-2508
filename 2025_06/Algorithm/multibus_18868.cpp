#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int space = 0, n = 0;
    cin >> space >> n;
    vector<vector<int>> planet(space, vector<int>(n));
    vector<vector<int>> compare(space, vector<int>(n));

    for (int j = 0; j < space; j++)
    {
        for (int i = 0; i < n; i++)
        {
            cin >> planet[j][i];
        }
    }
    int zMin = 0, temp = 0;
    for (int i = 0; i < space; i++)
    {
        for (int j = 0; j < n; j++)
        {
            zMin = j;
            for (int z = j + 1; z < n; z++)
            {
                if (planet[i][zMin] > planet[i][z])
                {
                    zMin = z;
                }
            }
            compare[i][j] = zMin;
            temp = planet[i][zMin];
            planet[i][zMin] = planet[i][j];
            planet[i][j] = temp;
        }
    }
    int result = 0;
    bool match = false;
    for (int i = 0; i < space; i++)
    {
        for (int j = 0; j < space; j++)
        {
            for (int z = 0; z < n; z++)
            {
                if (i == j)
                    break;
                if (compare[i][z] != compare[j][z])
                    break;
                if (z == n - 1)
                {
                    result++;
                    match = true;
                }
            }
            if (match)
            {
                match = false;
                break;
            }
        }
    }
    cout << result/2;
    return 0;
}