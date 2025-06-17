#include <iostream>
#include <vector>
#include <stdio.h>
#include <cctype>
#include <string>
#include <sstream>
using namespace std;

vector<string> input(){
    vector<string> formula;
    string all,word;
    getline(cin,all,'\n');
    istringstream iss(all);
    while(iss >> word){
        formula.push_back(word);
    }
    return formula;
}  

int main()
{
    string right="n",left="n";
    vector<string> formula=input();
    int num;
    string x;
    while(formula.size()!=1){
        x=formula.back();
        formula.pop_back();
        if(isdigit(x[0])){
            if(right!="n"){right=x;}
            else{left=x;}
        }
        else{
            switch(x[0]){
                case '+':num=stoi(left)+stoi(right); break;
                case '-':num=stoi(left)-stoi(right); break;
                case '/':num=stoi(left)/stoi(right); break;
                case '*':num=stoi(left)*stoi(right); break;
            }
            right="n";
            left="n";
        }
        formula.push_back(to_string(num));
    }
    cout << formula[0] << endl;
}
