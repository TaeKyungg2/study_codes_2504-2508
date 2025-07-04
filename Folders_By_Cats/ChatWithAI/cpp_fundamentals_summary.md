# C++ 관련 주요 개념 정리

## 📌 포인터와 지역 변수

### 지역 변수 주소 반환 (위험!)

```cpp
int* makePointer() {
    int x = 10;     // 지역 변수
    return &x;      // 위험: x는 함수 종료 후 소멸됨
}
```

- 함수가 끝나면 지역 변수는 스택에서 사라짐 → 댕글링 포인터 발생
- 안전한 방법:
  - `new`로 힙에 할당 후 반환
  - 값을 복사해서 반환

### 안전한 예시

```cpp
int* makePointer() {
    int* x = new int(10);
    return x;  // 사용 후 delete 필요
}
```

---

## 📌 클래스와 생성자에서의 지역 변수 vs 멤버 변수

### 잘못된 예

```cpp
Red_Black_Tree(int data) {
    Node root(data, false);  // 지역 변수임, 멤버 아님
}
```

### 올바른 예

```cpp
class Red_Black_Tree {
    Node* root;
    Red_Black_Tree(int data) {
        root = new Node(data, false);
    }
};
```

또는 값 타입일 경우:

```cpp
class Red_Black_Tree {
    Node root;
    Red_Black_Tree(int data) : root(data, false) {}
};
```

---

## 📌 기본형 변수 초기화

### `int i;` vs `int i = int();`

| 표현               | 초기화 여부 | 설명                 |
| ---------------- | ------ | ------------------ |
| `int i;`         | ❌ 없음   | 쓰레기 값 (stack의 기존값) |
| `int i = int();` | ✅ 있음   | 0으로 명시적 초기화        |

- `int i;` → **초기화되지 않음** (지역 변수일 경우)
- `int i = int();` → `0`으로 초기화됨
- 안전하게 하려면 항상 명시적으로 초기화 (`int i = 0;`, `int i{};` 등)

---

## 📌 쓰레기 값 (Garbage Value)

- 초기화하지 않은 지역 변수는 **스택의 기존 값**을 그대로 사용
- 예측 불가한 값이 출력됨

```cpp
void func() {
    int x;
    std::cout << x << std::endl;  // 쓰레기 값
}
```

- 전역 변수나 static 변수는 자동으로 0으로 초기화됨

---

## 📌 `this` 포인터

- C++의 `this`는 **현재 객체의 포인터**
- 클래스의 멤버 함수를 통해 호출될 때 암시적으로 전달됨

```cpp
class MyClass {
    int data;
public:
    void set(int val) {
        this->data = val;  // 명확하게 멤버를 지정
    }
};
```

---

## 📌 구조체에서 초기화 및 공유 여부

- C++ 구조체는 클래스처럼 생성자, 멤버 함수, 초기화 가능

```cpp
struct Node {
    int data = 0;
    Node* left = nullptr;
    Node* right = nullptr;
    Node(int dat) : data(dat) {}
};
```

- 멤버 변수는 각 구조체 인스턴스마다 별도로 존재함 → Python 클래스 변수처럼 **공유되지 않음**

---

## 📌 const와 초기화

- `const` 변수는 **선언 시 반드시 초기화**해야 함
- 초기값을 변경할 수 없음

```cpp
const int x = 5;  // OK
const int y;      // ❌ 오류: 초기화 누락
```

---

필요하면 이 내용에 클래스 설계, 메모리 구조, 트리 구현, 포인터 예제 등을 더 추가할 수 있습니다.

