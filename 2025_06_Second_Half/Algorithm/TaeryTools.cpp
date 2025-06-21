#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <sstream>
using namespace std;
vector<int> RowToInts() {
    string str;
    getline(cin, str);
    istringstream iss(str);    // istringstream에 str을 담는다.
    string buffer;   // 구분자를 기준으로 절삭된 문자열이 담겨지는 버퍼
    vector<int> result;
    // istringstream은 istream을 상속받으므로 getline을 사용할 수 있다.
    while (getline(iss, buffer, ' ')) {
        result.push_back(stoi(buffer));  // 절삭된 문자열을 vector에 저장
    }
    return result;
}

vector<vector<int>> NRowToInts() {
    vector<vector<int>> result;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        result.push_back(RowToInts());
    }
    return result;
}

vector<string> RowToStrs() {
    string str;
    getline(cin, str);
    istringstream iss(str);    // istringstream에 str을 담는다.
    string buffer;   // 구분자를 기준으로 절삭된 문자열이 담겨지는 버퍼
    vector<string> result;
    // istringstream은 istream을 상속받으므로 getline을 사용할 수 있다.
    while (getline(iss, buffer, ' ')) {
        result.push_back(buffer);  // 절삭된 문자열을 vector에 저장
    }
    return result;
}

vector<vector<string>> NRowToStrs() {
    vector<vector<string>> result;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        result.push_back(RowToStrs());
    }
    return result;
}

void OutList(vector<int> list) {
    for (int i = 0; i < list.size(); i++) {
        cout << list[i] << " ";
    }
    cout << endl;
}

int main()
{
    vector<vector<int>> a = NRowToInts();
    for (int i = 0; i < a.size(); i++) {
        for (int j = 0; j < a[i].size(); j++) {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}