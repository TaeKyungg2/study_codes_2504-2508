# 파이썬 주소 및 @dataclass 관련 정리

## 📌 변수의 주소 확인

파이썬에서 변수의 주소(참조값)를 확인하려면 `id()` 함수를 사용한다.

```python
a = 42
print(id(a))         # 정수 주소 (10진수)
print(hex(id(a)))    # 정수 주소 (16진수)
```

- `id(obj)`는 객체의 유일한 ID를 반환 (CPython에서는 메모리 주소와 동일)
- `hex(id(obj))`로 실제 메모리 주소처럼 출력 가능

---

## 📌 `in` 연산자: 값 비교

```python
x = 2
arr = [1, 2, 3]
print(x in arr)  # True
```

- `in`은 값(`==`) 기준으로 비교
- 객체의 주소가 달라도 값이 같으면 True

---

## 📌 사용자 정의 클래스 객체 비교

```python
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
p2 = Person("Alice")
print(p1 == p2)  # False (기본은 주소 비교)
```

- `==`는 내부적으로 `__eq__()` 사용
- 직접 정의하지 않으면 `is`처럼 동작 (주소 비교)

### 🔧 `__eq__()` 오버라이딩

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name
```

---

## 📌 `@dataclass`란?

데이터 저장용 클래스를 쉽게 정의할 수 있도록 도와주는 데코레이터

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
```

자동 생성되는 메서드:
- `__init__`
- `__repr__`
- `__eq__`
- (선택적으로) `__hash__`, `__lt__`, `__le__` 등

### 사용 예시

```python
p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
print(p1 == p2)  # True
print(p1)        # Person(name='Alice', age=30)
```

---

## 📌 메서드가 있는 클래스에도 사용 가능?

- 사용 가능 ✅
- 단, `@dataclass`가 자동 생성하는 메서드와 충돌하면 사용자가 정의한 것이 우선
- 후처리는 `__post_init__()`에서 가능

```python
@dataclass
class Person:
    name: str
    age: int

    def greet(self):
        print(f"Hi, I'm {self.name}")
```

---

## 📌 자동 생성되는 `__init__`

```python
@dataclass
class Person:
    name: str
    age: int
```

자동 생성되는 `__init__`:

```python
def __init__(self, name: str, age: int):
    self.name = name
    self.age = age
```

기본값이 있다면:

```python
@dataclass
class Person:
    name: str
    age: int = 20
```

→

```python
def __init__(self, name: str, age: int = 20):
    self.name = name
    self.age = age
```

---

생성일: 2025-06-17
