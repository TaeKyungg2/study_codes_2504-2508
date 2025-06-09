#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int num=0,minj=0,temp=0;
    cin >> num;
    int n[num];
    for(int i=0;i<num;i++){
        cin >> n[i];
    }
    for(int i=0;i<num-1;i++){
        minj=i;
        for(int j=i;j<num;j++){
            if(n[j]<n[minj]){
                minj=j;
            }
        }
        temp=n[i];
        n[i]=n[minj];
        n[minj]=temp;
    }
    for(int i=0;i<num;i++){
        cout << n[i] << endl;
    }
    return 0;
}

