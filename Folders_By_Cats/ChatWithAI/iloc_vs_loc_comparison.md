# `.iloc` vs `.loc` — Pandas 인덱싱 비교

| 항목 | `.iloc` | `.loc` |
|------|---------|--------|
| **키워드 의미** | **i**nteger **loc**ation | **loc**ation (레이블) |
| **기준(What it indexes by)** | **정수 위치** (0,1,2…) | **인덱스/컬럼 레이블** |
| **슬라이스 규칙** | `start:stop` → **stop 미포함** | `start:stop` → **stop 포함** |
| **존재하지 않는 키** | 위치 벗어나면 `IndexError` | 레이블 없으면 `KeyError` |
| **주요 인덱서 타입** | 정수, 정수 리스트, 슬라이스, 불리언 배열 | 레이블, 레이블 리스트, 슬라이스, 불리언 배열 |
| **대표 사용 예** | “0~99번째 행”, “첫 컬럼” | “2024‑01‑01~03 범위”, “컬럼 `'price'`” |

---

## 1. 기본 예시

```python
import pandas as pd
df = pd.DataFrame(
    {'A': [10, 20, 30],
     'B': [100, 200, 300]},
    index=['a', 'b', 'c']
)

# 위치 기반
df.iloc[0]          # 첫 번째 행 (index 'a')
df.iloc[:, 1]       # 두 번째 열 (컬럼 'B')

# 레이블 기반
df.loc['b']         # 인덱스 'b' 행
df.loc[:, 'B']      # 컬럼 'B' 열
```

---

## 2. 슬라이스 차이

```python
# iloc: stop 행 **미포함**
df.iloc[0:2]        # 행 0, 1 (a, b)

# loc: stop 행 **포함**
df.loc['a':'b']     # 행 'a', 'b'
```

---

## 3. 숫자 레이블이 섞인 경우

```python
ts = pd.Series([1, 2, 3], index=[0, 1, 2])

ts.loc[1]   # 레이블 1 (값 2)
ts.iloc[1]  # 위치 1  (값 2) 같은 결과지만 개념은 다름

ts.index = [10, 20, 30]
ts.loc[20]  # 레이블 20 (값 2)
ts.iloc[1]  # 두 번째 행 (값 2)
```

---

## 4. 불리언 마스크

```python
mask = df['A'] > 15
df[mask]          # df.loc[mask]와 동일
df.loc[mask]      # ✔️ 권장
df.iloc[mask]     # ⚠️ 위치·레이블 혼용으로 가독성↓
```

---

## 5. 암기법

> **i**loc → **i**nteger  
> loc → **label**

- **순번(숫자 위치) → `iloc`**  
- **이름(레이블) → `loc`**  
- 슬라이스: `iloc`은 **stop 미포함**, `loc`은 **stop 포함**
