#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int num=0;
    cin >> num;
    vector<string> arr(num);
    string command="";
    string key="";
    for(int i=0;i<num;i++){
        cin >> command;
        if(command=="insert"){
            cin >> arr[i];
        }
        else if(command=="find"){
            cin >> key;
            if(find(arr.begin(),arr.end(),key)!=arr.end()){
                cout << "yes" << endl;
            }
            else{
                cout << "no" << endl;
            }
        }
    }
}
