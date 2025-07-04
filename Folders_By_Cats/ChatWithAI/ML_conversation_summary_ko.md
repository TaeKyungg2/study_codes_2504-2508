
# 머신러닝 대화 요약

다음은 이 채팅방에서 다뤘던 머신러닝 관련 핵심 내용을 **한글**로 정리한 것입니다. **Conda 관련 내용은 제외**하고, 시각화부터 고차원 선형 모델까지 자세하게 설명합니다.

---

## 1. 데이터 시각화 (Matplotlib & Pandas)

### 1.1 `pd.plotting.scatter_matrix`
- **기능**: DataFrame의 모든 열 쌍에 대한 산점도와 대각선의 히스토그램을 한 번에 그려주는 함수  
- **주요 매개변수**  
  - `c`: 점의 색상을 지정하는 배열 (레이블별 색 구분)  
  - `figsize`: 출력 크기(가로, 세로 인치)  
  - `marker`: 점 모양 (예: `'o'`, `'^'`)  
  - `hist_kwds`: 대각선 히스토그램 옵션 (`{'bins':20, 'density':True}` 등)  
  - `s`: 점 크기 (포인트 단위)  
  - `alpha`: 투명도 (0.0~1.0)  
  - `cmap`: 컬러맵 (예: `'viridis'`, `mglearn.cm3`)

### 1.2 히스토그램(Histogram)
- **x축**: 데이터를 일정 구간(bin)으로 나눈 값 범위  
- **y축**: 각 구간에 속하는 데이터 개수(기본) 또는 확률밀도(`density=True`)  
- **bins**  
  - 정수 지정 시: 전체 범위를 동일한 폭으로 나눔  
  - 리스트 지정 시: 구간 경계를 직접 설정 가능  
- **어원**:  
  - `histo-` (그리스어 *histós*: 기둥)  
  - `-gram` (그리스어 *gramma*: 그린 그림)  

### 1.3 Matplotlib 상태 관리
- `plt` 모듈은 **전역 상태(stateful)** 를 사용  
- `plt.show()` 호출 시 **모든 열린 Figure**를 한 번에 렌더링  
- 객체지향 API 권장:  
  ```python
  fig, ax = plt.subplots()
  ax.plot(...)
  ax.set_title(...)
  plt.show()
  ```

### 1.4 여러 서브플롯 만들기
```python
fig, axes = plt.subplots(1, 3, figsize=(10, 3))
# axes[0], axes[1], axes[2] 각각에 개별 그래프를 그림
```

---

## 2. mglearn 유틸리티

### 2.1 `mglearn.plots.plot_knn_classification(n_neighbors)`
- 내부 합성 데이터셋 **forge**(2차원, 26개 샘플) 사용  
- 좌측: k-NN 결정 경계(decision boundary),  
- 우측: 특정 이웃 개수 설정 시의 예측 방식 시각화  

### 2.2 `mglearn.plots.plot_2d_separator(...)`
- **기능**: 학습된 분류기 `clf`의 결정 영역을 2D 평면에 채워 그림  
- 주요 매개변수:  
  - `clf`: 학습된 모델 객체  
  - `X`: 훈련 데이터 (shape=(n_samples,2))  
  - `fill=True`: 영역 채우기  
  - `eps`: 데이터 최소·최대값 범위에 추가 여유(margin)  
  - `ax`: Matplotlib `Axes` 객체  
  - `alpha`: 배경 투명도  

### 2.3 `mglearn.discrete_scatter(...)`
- **기능**: 클래스별로 다른 색·모양의 산점도를 같은 축(`ax`)에 그림  
- 예시:
  ```python
  mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=0.4)
  mglearn.discrete_scatter(X[:,0], X[:,1], y, ax=ax)
  ```

---

## 3. 고차원 선형 모델 & 과대적합

### 3.1 고차원에서 선형 모델이 잘 작동하는 이유
1. **선형 분리 가능성 증가**  
   - 고차원일수록 데이터 포인트가 퍼질 수 있는 방향이 많아져, 서로 다른 클래스가 자연스럽게 분리됨  
2. **거리 집중 현상**  
   - 고차원에서는 점들 사이 거리가 비슷해지고, 임의의 두 클래스가 거의 직교하게 분포  
3. **정규화의 활용**  
   - L2(릿지), L1(라쏘)를 통해 과적합 제어 및 특성 선택 효과  

### 3.2 초평면(hyperplane)의 차원
- 입력 공간: \(d\)차원에서 방정식 \(w^T x + b = c\)는 **\(d-1\)차원 초평면**  
- 입력+출력 공간: \((d+1)\)차원에서 모델 그래프는 **\(d\)차원 초평면**

### 3.3 VC 차원
- 선형 분류/회귀 모델의 VC 차원은 **\(d+1\)**  
- 샘플 수 \(n \le d+1\) 시 훈련 데이터에 완벽히 맞춤 가능 → 과적합 위험

### 3.4 과대적합 발생 예시
- **2D/3D**라도 노이즈, 샘플 수 부족, 특성 간 강한 상관관계 시 과대적합 발생  
- 간단한 실험으로 확인 가능:
  ```python
  from sklearn.linear_model import LinearRegression
  from sklearn.model_selection import cross_val_score
  # n_samples=50, d_features=2 또는 3 등
  ```

### 3.5 과대적합 방지 전략
- **교차검증**으로 일반화 성능 확인  
- **릿지/라쏘** 등 **정규화** 사용  
- **PCA** 또는 **특성 선택**  
- **샘플 수 증가** 또는 **앙상블** 기법  

---

## 4. 기타 중요 개념

- **`np.linspace(-3,3,1000).reshape(-1,1)`**  
  - -3~3 구간을 균등 분할한 1차원 배열 → `(1000,)`  
  - `.reshape(-1,1)`로 `(1000,1)` 형태(열 벡터)  
- **`loc='best'`**  
  - `plt.legend(loc='best')`: 범례를 자동으로 최적 위치에 배치  
- **`plt` 모듈**  
  - 전역 상태 기반, 싱글톤은 아니지만 하나의 상태 머신처럼 동작  
