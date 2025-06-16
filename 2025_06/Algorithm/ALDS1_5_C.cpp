#include <iostream>
#include <vector>
#include <stdio.h>
#include <cmath>
#include <cstdlib>
using namespace std;

const float PI = 3.141592653589793f; //No Complete......

void koch(int n, pair<float, float> p1, pair<float, float> p2)
{
    if (n == 0)
        return;
    float x1 = p1.first;
    float y1 = p1.second;
    float x2 = p2.first;
    float y2 = p2.second;
    float TriLength = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) / 3;
    float sinValue = abs((y2 - y1) / (TriLength * 3));
    float cosValue = abs((x2 - x1) / (TriLength * 3));
    float HeightTri = TriLength * sin(PI / 3);
    float xDif = abs(x2 - x1);
    float yDif = abs(y2 - y1);
    pair<float, float> n1 = {x1 + xDif / 3, y1 + yDif / 3};
    pair<float, float> n2 = {x1 + xDif / 2 + HeightTri * sinValue,
                             y1 + yDif / 2 + HeightTri * cosValue};
    pair<float, float> n3 = {x1 + xDif * 2 / 3, y1 + yDif * 2 / 3};
    koch(n - 1, p1, n1);
    cout << n1.first << " " << n1.second << endl;
    koch(n - 1, n1, n2);
    cout << n2.first << " " << n2.second << endl;
    koch(n - 1, n2, n3);
    cout << n3.first << " " << n3.second << endl;
    koch(n - 1, n3, p2);
}

int main()
{
    int n;
    cin >> n;
    cout << 0 << " " << 0 << endl;
    koch(n, {0, 0}, {100, 0});
    cout << 100 << " " << 0 << endl;
}
