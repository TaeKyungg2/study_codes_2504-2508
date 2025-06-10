#include <iostream>
#include <vector>
#include <stdio.h>
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
    bool same = false;
    for (int i = 0; i < space; i++)
    {
        for (int j = 0; j < n; j++)
        {
            zMin = j;
            same = false;
            for (int z = j + 1; z < n; z++)
            {
                if (planet[i][zMin] > planet[i][z])
                {
                    zMin = z;
                    same = false;
                }
                if (planet[i][zMin] == planet[i][z])
                {
                    zMin = z;
                    same = true;
                }
            }
            if (same)
            {
                compare[i][j] = zMin + n;
            }
            else
            {
                compare[i][j] = zMin;
            }
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
                {
                    break;
                }

                if (compare[i][z] != compare[j][z])
                {
                    break;
                }

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
    if(result==0){
        result=int(result);
        cout << result << endl;
    }
    else
    {

        result=result/2;
        result=int(result);
        cout << result << endl;
    }
    
    return 0;
}