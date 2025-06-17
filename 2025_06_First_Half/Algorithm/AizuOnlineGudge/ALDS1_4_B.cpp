#include <iostream>
#include <vector>
using namespace std;

// bool binarySearch(vector<int> s, int key)
// {

//     int mid = s.size() / 2;
//     if (s[mid] == key)
//     {
//         return true;
//     }
//     else if (s.size() == 1)
//     {
//         return false;
//     }
//     else if (s[mid] > key)
//     {
//         return binarySearch(vector<int>(s.begin(), s.begin() + mid - 1), key);
//     }
//     else if (s[mid] < key)
//     {
//         return binarySearch(vector<int>(s.begin() + mid + 1, s.end() - 1), key);
//     }
// }
bool binarySearch(vector<int> s, int key)
{
    int mid = s.size() / 2;
    int right = s.size() - 1;
    int left = 0;
    while (left <= right)
    {
        mid = (left + right) / 2;
        if (s[mid] == key)
        {
            return true;
        }
        else if (s[mid] > key)
        {
            right = mid - 1;
        }
        else if (s[mid] < key)
        {
            left = mid + 1;
        }
    }
    return false;
}
int main()
{
    int sNum = 0, tNum = 0;
    cin >> sNum;
    vector<int> s(sNum);
    for (int i = 0; i < sNum; i++)
    {
        cin >> s[i];
    }
    cin >> tNum;
    vector<int> t(tNum);
    for (int i = 0; i < tNum; i++)
    {
        cin >> t[i];
    }
    int count = 0;
    int key = 0;
    for (int i = 0; i < tNum; i++)
    {
        key = t[i];
        if (binarySearch(s, key))
        {
            count++;
            t[i] = -1;
        }
    }
    cout << count << endl;
}
