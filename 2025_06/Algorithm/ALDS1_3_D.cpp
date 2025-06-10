#include <iostream>
#include <vector>
#include <stdio.h>
#include <stack>
using namespace std;

int main()
{
    string g;
    cin >> g;
    // stack<char> st;
    int slope=0,depth=0;
    vector<float> area;
    area.push_back(0);
    int high=0;
    for(char x :g)
    {
        if(x=='\\'){
            depth+=1;
            area.back()+=depth-0.5;
        }
        else if(x=='/'){
            depth-=1;
            area.back()+=depth+0.5;
        }
        else if(x=='_'){
            area.back()+=depth;
        }
        if(depth==0){
            area.push_back(0);
        }
        if(depth<0){
            depth=0;
        }
    }
    cout << area.size() << " ";
    for(int i : area){
        cout << i << " ";
    }
}