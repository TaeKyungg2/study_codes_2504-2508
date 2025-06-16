#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int N;
    cin >> N;
    vector<int> A(N);
    for(int i=0;i<N;i++){
        cin >> A[i];
    }
    int v=0;
    int j=0;
    for(int z=0;z<N;z++){
            cout << A[z];
            if(z!=N-1){cout << " ";}
    }
    cout << "" << endl;
    for(int i=1;i<N;i++)
    {
        v=A[i];
        j=i-1;
        while(j>=0 && A[j]>v){
            A[j+1]=A[j];
            j--;
        }
        A[j+1]=v;
        for(int z=0;z<N;z++){
            cout << A[z];
            if(z!=N-1){cout << " ";}
        }
        cout << "" << endl;
    }
    return 0;
}
