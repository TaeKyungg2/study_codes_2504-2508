# 사이킷런 Pipeline 완전 정리

Scikit-learn의 `Pipeline`은 전처리와 모델을 하나의 흐름으로 구성하여 **코드의 일관성**, **재현 가능성**, **GridSearchCV 통합** 등에 유용한 도구입니다.

---

## 🔷 1. Pipeline 기본 개념

`Pipeline`은 여러 단계의 작업을 **순서대로 묶은 객체**입니다. 각 단계는 `(이름, 객체)` 형태로 정의하며, 마지막 단계는 반드시 **예측기 (estimator)** 여야 합니다.

```python
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('step1', transformer1),
    ('step2', transformer2),
    ('model', estimator)  # 마지막은 예측기
])
````

---

## 🔷 2. 간단한 예제: 스케일링 + 로지스틱 회귀

```python
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

pipe = Pipeline([
    ('scaler', StandardScaler()),              
    ('clf', LogisticRegression())              
])

pipe.fit(X_train, y_train)
pred = pipe.predict(X_test)
```

---

## 🔷 3. GridSearchCV와 함께 사용

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'clf__C': [0.1, 1, 10]  # 'clf'는 Pipeline에서 설정한 이름
}

grid = GridSearchCV(pipe, param_grid, cv=5)
grid.fit(X_train, y_train)
```

---

## 🔷 4. ColumnTransformer와 함께 사용

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

df = pd.DataFrame({
    'height': [180, 175, 160],
    'gender': ['M', 'F', 'F'],
    'target': [1, 0, 1]
})

X = df.drop(columns='target')
y = df['target']

preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), ['height']),
    ('cat', OneHotEncoder(), ['gender'])
])

pipe = Pipeline([
    ('prep', preprocessor),
    ('clf', LogisticRegression())
])

pipe.fit(X, y)
```

---

## 🔷 5. 주요 메서드

| 메서드            | 설명                       |
| -------------- | ------------------------ |
| `fit(X, y)`    | 전체 파이프라인 학습              |
| `predict(X)`   | 전체 예측 수행                 |
| `score(X, y)`  | 모델 성능 평가                 |
| `get_params()` | 파라미터 조회                  |
| `set_params()` | 파라미터 설정 (GridSearch에 유용) |

---

## 🔷 6. 장점 요약

* 전처리와 모델을 **하나로 묶어서 재현성 확보**
* train/test split 시 **동일 전처리 자동 적용**
* 코드 구조 간결하고 유지보수 쉬움
* `GridSearchCV` 같은 튜닝 작업과 **매끄럽게 연동**

---

## 🔷 7. 커스텀 전처리기 사용법

### ✅ 방법 1. `FunctionTransformer` 사용

간단한 함수형 전처리를 빠르게 적용할 수 있음

```python
from sklearn.preprocessing import FunctionTransformer

def my_custom_func(X):
    X_new = X.copy()
    X_new[:, 0] = X_new[:, 0] * 2
    return X_new

custom_transformer = FunctionTransformer(my_custom_func)

pipe = Pipeline([
    ('custom', custom_transformer),
    ('clf', LogisticRegression())
])
```

---

### ✅ 방법 2. TransformerMixin 상속 (클래스 직접 정의)

복잡한 로직이나 `fit()` 단계에서 상태 저장 필요 시 사용

```python
from sklearn.base import BaseEstimator, TransformerMixin

class MyCustomTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, option=True):
        self.option = option

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_new = X.copy()
        if self.option:
            X_new[:, 0] = X_new[:, 0] + 100
        return X_new

pipe = Pipeline([
    ('custom', MyCustomTransformer(option=False)),
    ('clf', LogisticRegression())
])
```

---

### ✅ pandas를 활용한 커스텀 전처리기

```python
class MyPandasTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        df = X.copy()
        df['height'] = df['height'] / 100  # cm → m
        return df
```

---

### ✅ 커스텀 전처리 비교 요약

| 방법                         | 사용 시기                    | 특징                    |
| -------------------------- | ------------------------ | --------------------- |
| `FunctionTransformer`      | 간단한 함수형 전처리              | 빠르고 편리                |
| 커스텀 클래스 (TransformerMixin) | 복잡한 로직, fit/transform 분리 | 자유도 높음, GridSearch 가능 |

---

## 📎 관련 클래스

* `sklearn.pipeline.Pipeline`
* `sklearn.preprocessing.FunctionTransformer`
* `sklearn.base.TransformerMixin`, `BaseEstimator`
* `sklearn.compose.ColumnTransformer`
* `sklearn.model_selection.GridSearchCV`

