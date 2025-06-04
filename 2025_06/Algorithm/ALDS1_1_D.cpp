#include<stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    int length=0;
    cin >> length;
    int num=0,max=-2000000000,min=2000000000,dif=0;
    for(int i=0;i<length;i++){
        cin >> num;
        max=std::max(max,num-min);
        min=std::min(min,num);
        
    }
    cout << max << endl;
}