#include <iostream>
using namespace std;

int main()
{
    int space=0,n=0;
    cin >> space >> n;
    int planet[space][n];
    int compare[space][n];

    for(int j=0;j<space;j++){
        for(int i=0;i<n;i++){
            cin >> planet[j][i];
            if(i==0) {
                compare[j][i]=0;
                continue;
            }
            if(planet[j][i]<planet[j][i-1]){
                compare[j][i]=1;
            }
            else if(planet[j][i]<planet[j][i-1]){
                compare[j][i]=2;
            }
            else if(planet[j][i]==planet[j][i-1]){
                compare[j][i]=3;
            }
        }
    }
    int zMin=0;
    for(int i=0;i<space;i++){
        for(int j=0;j<n;j++){
            zMin=j;
            for(int z=j;z<n;z++){
                if(planet[i][zMin]>planet[i][z]){
                    zMin=z;
                }
            }
            for(int v=zMin;v>=j;v--){
                
            }
        }
    }

    int result=0;
    bool match=false;
    for(int i=0;i<space;i++){
        for(int j=0;j<space;j++){
            for(int z=0;z<n;z++){
                if(i==j) break;
                if(compare[i][z]!=compare[j][z]) break;
                if(z==n-1) {
                    result++;
                    match=true;
                }
            if(match) {
                match=false;
                break;
            }
            
        }
    }
    cout << result;
}