#include<iostream>
#include<vector>
#include<stdio.h>
using namespace std;

int shellSort(vector<int> A,int n);

int main(){
    vector<int> A;
    int n=0;
    shellSort(A,n);
}
int cnt=0;
int insertionSort(vector<int> A,int n,int g)
{
    int j=0;
    int v=0;
    for(int i=g;i<n;i++){
        v=A[i];
        j=i-g;
        while(j>=0 && A[j]>v){
            A[j+g]=A[j];
            cnt++;
        }
        A[j+g]=v;
    }
}
int shellSort(vector<int> A,int n){
    cnt=0;
    int m=-1;
    vector<int> G={};
    for(int i=0;i<m;i++){
        insertionSort(A,n,G[i]);
    }
}


