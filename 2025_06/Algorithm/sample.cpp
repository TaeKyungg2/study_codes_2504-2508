#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

int main()
{
    vector<int> s{1,2,3,4,5,6,7,8,9,10};
    vector<int> t(s.begin(),s.begin());
    cout << t.size() << endl;
    return 0;
}
