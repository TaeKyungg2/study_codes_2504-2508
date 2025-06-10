#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;
int main(){
    vector<int> A;
    A.push_back(4);
    A.push_back(2);     
    A.push_back(3);
    A.push_back(4);
    A.push_back(7);

    cout << *A.begin() <<"begin" << endl;
    cout << *A.end() <<"end" << endl;
}