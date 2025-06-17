# `@dataclass` 객체와 `in` 연산자 관련 정리

## ✅ 상황 요약

- `@dataclass`를 사용해 만든 클래스 객체 2개가 있음
- 두 객체는 **멤버 변수 값이 동일**
- 그중 하나는 배열(set/list)에 들어 있음
- `객체 in 배열` 연산을 했는데 결과가 `False`로 나옴

---

## ✅ 기본 원리: `in` 연산자

파이썬의 `x in 리스트` 구문은 내부적으로 다음과 같이 작동함:

```python
for item in 리스트:
    if x == item:
        return True
return False
```

즉, **`==` 비교가 사용됨**

---

## ✅ `@dataclass`는 `__eq__()`를 자동 정의함

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
```

이렇게 선언하면 내부적으로 아래와 같은 `__eq__()`가 생성됨:

```python
def __eq__(self, other):
    return isinstance(other, Person) and self.name == other.name and self.age == other.age
```

따라서 일반적으로는 아래처럼 작동해야 함:

```python
p1 = Person("Alice", 30)
p2 = Person("Alice", 30)

print(p1 == p2)       # True
print(p1 in [p2])     # True
```

---

## ❗ 그런데 `False`가 나오는 경우

### 1. `compare=False` 옵션 사용 시
```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str = field(compare=False)
    age: int
```
→ `name` 필드는 `__eq__` 비교에서 제외됨

### 2. 클래스가 다르면 (`MyClass` vs `MySubClass`)
```python
p1 = MyClass(1)
p2 = MySubClass(1)
p1 == p2  # False 가능
```

### 3. 직접 `__eq__` 오버라이딩한 경우
```python
def __eq__(self, other):
    return False  # 강제로 False 반환
```

### 4. 비교 대상이 같은 타입이 아닌 경우

예: 리스트 안에 `MyClass(1)`인데, 바깥은 `MyClass(1.0)` → float vs int → False

---

## 🔍 요약

- `@dataclass` 객체는 일반적으로 값이 같으면 `==` → True
- `in` 연산은 내부적으로 `==` 사용
- **값이 같은데 `in`이 False라면**, `__eq__()` 로직이나 `compare=False` 설정 확인 필요

---

## 🧠 관련 개념

### `None`과 `==`, `is`

- `a == None` → `__eq__()`가 호출될 수 있음
- `a is None` → **항상 주소 비교**, 더 안전함

### `None`은 싱글턴

```python
id(None)  # 항상 동일한 주소
None is None  # 항상 True
```

---

## 🔄 조건부 표현식 평가 순서

```python
x = node.parent.id if node.parent != -1 else -1
```

- `node.parent != -1`이 `False`면 `node.parent.id`는 **실행되지 않음**
- `if` 앞의 표현식은 **조건이 True일 때만 평가됨**

---

생성일: 2025-06-17
