#include<stdio.h>
#include <vector>
#include <iostream>
using namespace std;
int main()
{
    int length=0;
    cin >> length;
    int num=0,max=0,min=1000000000,dif=0,difMax=-1000000000;
    for(int i=0;i<length;i++){
        cin >> num;
        if(num<min&&num<max){
            dif=max-min;
            min=num;
            max=0;
        }
        if(num>max){
            max=num;
            dif=max-min;
        }
        if(min>max){
            dif=min-max;
        }
        if(difMax<dif){
            difMax=dif;
        }
    }
    
    cout << difMax << endl;
}