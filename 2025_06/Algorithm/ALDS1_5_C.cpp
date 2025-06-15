#include <iostream>
#include <vector>
#include <stdio.h>
#include <cmath>
using namespace std;

const float PI = 3.141592653589793f;

void koch(int n,vector<pair<float,float>> &point)
{
    int i=0;
    if (n == 0)
        return;
    float x = point[i].first;
    float y = point[i].second;
    float xx= point[point.size()-i-1].first;
    float yy= point[point.size()-i-1].second;
    
    point.insert(point.begin()+i,{(xx-x)/3,(yy-y)/3});
    point.insert(point.begin()+i+1,{(xx-x)/3*2,(yy-y)/3*2});
    point.insert(point.begin()+i,{(xx-x)/2,(xx-x)/3*sin(PI/3)})
}

int main()
{
    int n;
    cin >> n;
    vector<pair<float,float>> point;
    point.push_back({0,0});
    point.push_back({100,0});



    koch(n,point);
}
