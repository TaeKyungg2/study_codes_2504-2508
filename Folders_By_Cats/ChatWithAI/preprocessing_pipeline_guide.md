# Train / Test 전처리 가이드 (Scikit‑learn & Kaggle)
한국어로 정리한 **트레이닝/테스트 데이터 전처리** 핵심 노트입니다.  
모든 예시는 `scikit‑learn 1.4+`, `pandas`, `xgboost` 기준입니다.

---

## 1. 왜 전처리를 분리해야 하나?
| 목적 | 이유 |
|------|------|
| **데이터 누수(Leakage) 방지** | 테스트셋 정보를 사용하면 실제 성능이 과대평가됩니다. |
| **재현성** | 같은 파이프라인이면 어디서 실행해도 identical 결과 |
| **워크플로 단순화** | 코드 두 배 작성 X. `Pipeline`·`ColumnTransformer` 에 전처리 로직을 캡슐화 |

---

## 2. 전처리 기본 단계 체크리스트
1. **결측치(Impute)**  
   - 수치형: `SimpleImputer(strategy='median')`  
   - 범주형: `SimpleImputer(strategy='most_frequent')`
2. **스케일링 / 정규화**  
   - `StandardScaler`, `MinMaxScaler`
3. **인코딩**  
   - One‑Hot: `OneHotEncoder(handle_unknown='ignore')`  
   - Ordinal: `OrdinalEncoder`
4. **특성 선택 / 파생 변수**  
   - `PolynomialFeatures`, `FeatureHasher`, custom `FunctionTransformer`
5. **파이프라인화**  
   - 위 모듈들을 `Pipeline`, `ColumnTransformer` 로 묶기

---

## 3. 파이프라인 예제 코드

```python
import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from xgboost import XGBClassifier

# ── 1. 데이터 분리
target = 'label'
X = train.drop(columns=[target])
y = train[target]
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ── 2. 컬럼 타입별 구분
num_cols = X.select_dtypes(include=['int', 'float']).columns
cat_cols = X.select_dtypes(include=['object', 'category']).columns

# ── 3. 전처리 파이프
numeric_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler',  StandardScaler())
])

categorical_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('ohe',     OneHotEncoder(handle_unknown='ignore'))
])

preprocess = ColumnTransformer([
    ('num', numeric_pipe, num_cols),
    ('cat', categorical_pipe, cat_cols)
])

# ── 4. 전체 파이프라인
model = Pipeline([
    ('prep', preprocess),
    ('clf',  XGBClassifier(
                n_estimators=400,
                max_depth=5,
                learning_rate=0.05,
                subsample=0.8,
                colsample_bytree=0.8,
                random_state=42,
                use_label_encoder=False,
                eval_metric='logloss'))
])

model.fit(X_train, y_train)
print("validation score:", model.score(X_valid, y_valid))

# ── 5. 테스트 예측
test_pred = model.predict(test)  # 전처리 자동 적용
```

---

## 4. 동작 흐름 다이어그램

```
        fit() 호출                    predict() 호출
┌───────────────┐                  ┌───────────────┐
│  X_train, y   │                  │    X_test     │
└──────┬────────┘                  └──────┬────────┘
       │                               transform
   fit + transform                      (no fit)
       ▼                                   ▼
┌───────────────┐                  ┌───────────────┐
│ preprocess    │   ──►            │ preprocess    │
│ (ColumnTrans) │                  │ (fitted)      │
└──────┬────────┘                  └──────┬────────┘
       │                                   │
       │ fit                               │ predict
       ▼                                   ▼
┌───────────────┐                  ┌───────────────┐
│  XGBClassifier│                  │  XGBClassifier│
└───────────────┘                  └───────────────┘
```

---

## 5. 자주 발생하는 오류 & 해결
| 오류 메시지 | 원인 | 해결 |
|-------------|------|------|
| `ValueError: could not convert string to float` | 문자형 컬럼이 숫자 파이프에 섞임 | ColumnTransformer 로 타입 분리 |
| `Invalid classes inferred ...` | 타깃이 문자열 | `LabelEncoder` 로 숫자 인코딩 |
| `NaN not allowed` | 예측값에 NaN 있음 | 전처리 후 `isna().sum()` 체크 |
| `shape mismatch` | train/test 전처리 다르게 적용 | 같은 **preprocess** 객체 사용 |

---

## 6. Tips
* **`fit`은 오직 학습 데이터에만!**  
  테스트·배포 단계에서는 `transform`만 호출.
* **캐글 노트북 커밋**: `Pipeline` 덕분에 단 한 줄(`model.predict(test)`)로 예측 가능.
* **GridSearchCV**도 파이프라인 전체를 넘겨 하이퍼파라미터 튜닝 가능.

---

_작성: ChatGPT / 2025‑07‑07_
