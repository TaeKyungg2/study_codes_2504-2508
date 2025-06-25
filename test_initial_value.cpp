#include <iostream>
using namespace std;

int main() {
    // 동적 할당 - 초기값 정의되지 않음
    int* ptr1 = new int;
    cout << "동적 할당된 int의 초기값: " << *ptr1 << endl;
    
    // 명시적 초기화
    int* ptr2 = new int(0);  // 0으로 초기화
    cout << "0으로 초기화된 int: " << *ptr2 << endl;
    
    int* ptr3 = new int(42); // 42로 초기화
    cout << "42로 초기화된 int: " << *ptr3 << endl;
    
    // 배열 동적 할당
    int* arr = new int[5];  // 초기값 정의되지 않음
    cout << "배열의 초기값들: ";
    for(int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    // 메모리 해제
    delete ptr1;
    delete ptr2;
    delete ptr3;
    delete[] arr;
    
    return 0;
} 