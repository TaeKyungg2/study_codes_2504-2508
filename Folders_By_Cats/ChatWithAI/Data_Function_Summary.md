

# 📘 파이썬 수치 계산 패키지 함수 어원 정리

## 1. SymPy 함수 어원

| 함수 | 어원 (뜻) | 설명 | 사용 예시 |
| --- | --- | --- | --- |
| `subs` | substitute (대체하다) | 변수에 값을 대입 | `expr.subs(x, 3)` |
| `solve` | solve (풀다) | 방정식의 해를 구함 | `solve(x**2 - 4, x)` |
| `simplify` | simplify (단순화하다) | 수식을 간단한 형태로 바꿈 | `simplify((x**2 - 1)/(x - 1))` |
| `expand` | expand (전개하다) | 괄호 풀기 등 | `expand((x + 1)**2)` |
| `factor` | factor (인수 분해하다) | 수식을 인수 분해 | `factor(x**2 - 1)` |
| `diff` | differentiate (미분하다) | 도함수 계산 | `diff(x**2, x)` |
| `integrate` | integrate (적분하다) | 정적분/부정적분 계산 | `integrate(x**2, x)` |
| `limit` | limit (극한) | 극한 계산 | `limit(sin(x)/x, x, 0)` |
| `evalf` | evaluate float (실수로 계산) | 근삿값 구하기 | `pi.evalf()` |
| `lambdify` | lambda + -ify (람다 함수화하다) | 수식을 파이썬 함수로 변환 | `f = lambdify(x, x**2)` |

---

## 2. NumPy 함수 어원

| 함수 | 어원 (뜻) | 설명 | 사용 예시 |
| --- | --- | --- | --- |
| `array` | array (배열) | 배열 생성 | `np.array([1, 2, 3])` |
| `reshape` | re + shape (모양 바꾸다) | 배열 형태 변경 | `a.reshape((2, 3))` |
| `flatten` | flat (평평하게 하다) | 1차원 배열로 변환 | `a.flatten()` |
| `transpose` | transpose (전치하다) | 행렬 전치 | `a.transpose()` |
| `dot` | dot product (내적) | 벡터∙행렬 곱 | `np.dot(a, b)` |
| `sum` | sum (합계) | 합산 | `a.sum()` |
| `mean` | mean (평균) | 평균 계산 | `a.mean()` |
| `std` | standard deviation (표준편차) | 분산/표준편차 계산 | `a.std()` |
| `linspace` | linear + space | 균일 간격 수열 생성 | `np.linspace(0, 1, 5)` |
| `arange` | array + range | 숫자 범위로 배열 생성 | `np.arange(0, 10, 2)` |
| `where` | where (어디서) | 조건에 맞는 인덱스 | `np.where(a > 0)` |
| `concatenate` | con + catenate (함께 묶다) | 배열 결합 | `np.concatenate([a, b])` |
| `vstack` | vertical + stack | 수직 결합 | `np.vstack([a, b])` |
| `hstack` | horizontal + stack | 수평 결합 | `np.hstack([a, b])` |

---

## 3. Pandas 함수 어원

| 함수 | 어원 (뜻) | 설명 | 사용 예시 |
| --- | --- | --- | --- |
| `read_csv` | read + CSV (읽다) | CSV 파일 읽기 | `pd.read_csv("data.csv")` |
| `head` | head (머리) | 상위 몇 행 출력 | `df.head()` |
| `tail` | tail (꼬리) | 하위 몇 행 출력 | `df.tail()` |
| `groupby` | group + by | 기준 컬럼으로 그룹화 | `df.groupby("col")` |
| `merge` | merge (합치다) | 병합(join) | `pd.merge(df1, df2, on="id")` |
| `concat` | concatenate (연결하다) | 데이터 연결 | `pd.concat([df1, df2])` |
| `pivot` | pivot (축) | 데이터 재구성 | `df.pivot(index="A", columns="B", values="C")` |
| `melt` | melt (녹이다) | wide → long 변환 | `pd.melt(df, id_vars=["A"])` |
| `drop` | drop (버리다) | 행/열 삭제 | `df.drop("col", axis=1)` |
| `fillna` | fill + NA | 결측치 채우기 | `df.fillna(0)` |
| `isnull` | is + null | NaN 여부 판별 | `df["col"].isnull()` |
| `apply` | apply (적용하다) | 함수 적용 | `df["col"].apply(func)` |
| `map` | map (매핑하다) | 값 변환 | `df["col"].map(mapping_dict)` |

## 4. SciPy 함수 어원 (+ 사용 예시)

| 함수 | 어원 (뜻) | 설명 | 사용 예시 |
| --- | --- | --- | --- |
| `optimize` | optimize (최적화하다) | 최적화 도구 모음 | `from scipy import optimize` |
| `minimize` | minimize (최소화하다) | 함수의 최소값 찾기 | `optimize.minimize(fun, x0)` |
| `curve_fit` | curve + fit | 비선형 곡선 피팅 | `popt, _ = curve_fit(model, x, y)` |
| `root` | root (방정식의 해) | 비선형 방정식 근 | `optimize.root(f, x0)` |
| `linprog` | linear programming | 선형계획 최적화 | `optimize.linprog(c, A_ub, b_ub)` |
| `fsolve` | find + solve | 방정식 수치 해법 | `optimize.fsolve(f, x0)` |
| `quad` | quadrature (적분) | 1-D 수치적분 | `quad(func, 0, 1)` |
| `dblquad` / `tplquad` | double / triple quadrature | 2-D·3-D 적분 | `dblquad(f, 0,1, 0,1)` |
| `nquad` | n-dimensional + quadrature | 다중 적분 | `nquad(f, [[0,1],[0,1]])` |
| `odeint` | ODE + integrate | 상미분방정식 풀이 | `odeint(f, y0, t)` |
| `interp1d` | interpolate + 1d | 1-D 선형/스플라인 보간 | `f = interp1d(x, y)` |
| `splrep` | spline representation | 스플라인 파라미터화 | `tck = splrep(x, y)` |
| `splev` | spline evaluation | 스플라인 값 계산 | `y2 = splev(x2, tck)` |
| `fft` / `ifft` | Fast Fourier Transform | 푸리에 변환 / 역변환 | `X = fft(x)` |
| `convolve` | convolve (합성곱) | 1-D/ND 합성곱 | `convolve(a, b)` |
| `correlate` | correlate (상관) | 상관 함수 | `correlate(a, b)` |
| `stats` | statistics | 통계 분포 모음 | `from scipy import stats` |
| `pdf` | probability density function | 확률밀도 | `stats.norm.pdf(x)` |
| `cdf` | cumulative distribution function | 누적분포 | `stats.norm.cdf(x)` |
| `ppf` | percent point function | 역 CDF (분위수) | `stats.norm.ppf(q)` |
| `rvs` | random variates | 무작위 표본 | `stats.norm.rvs(size=100)` |
| `zscore` | z-score | 표준 점수 | `stats.zscore(data)` |
| `ttest_ind` | t-test independent | 독립표본 t-검정 | `stats.ttest_ind(a, b)` |

---

# 📊 Plotly 함수 이름 어원 정리

## 1. plotly.express — 간편·빠른 API (+ 사용 예시)

| 함수 | 어원 (뜻) | 설명 | 사용 예시 |
| --- | --- | --- | --- |
| `scatter` | scatter plot | 산점도 | `px.scatter(df, x="x", y="y")` |
| `line` | line plot | 선 그래프 | `px.line(df, x="date", y="value")` |
| `bar` | bar chart | 막대그래프 | `px.bar(df, x="cat", y="cnt")` |
| `box` | box plot | 상자그림 | `px.box(df, y="score", x="group")` |
| `violin` | violin plot | 분포+밀도 | `px.violin(df, y="score", x="group")` |
| `strip` | strip plot | 1-D 점 분포 | `px.strip(df, x="group", y="score")` |
| `histogram` | histogram | 히스토그램 | `px.histogram(df, x="age")` |
| `density_contour` | density + contour | 밀도 등고선 | `px.density_contour(df, x="x", y="y")` |
| `density_heatmap` | density + heatmap | 밀도 히트맵 | `px.density_heatmap(df, x="x", y="y")` |
| `imshow` | image + show | 행렬/이미지 | `px.imshow(img_arr)` |
| `line_3d` | 3-D line plot | 3-D 선 | `px.line_3d(df, x="x", y="y", z="z")` |
| `scatter_3d` | 3-D scatter | 3-D 산점도 | `px.scatter_3d(df, x="x", y="y", z="z")` |
| `line_polar` | polar coords | 극좌표 선 | `px.line_polar(df, r="r", theta="θ")` |
| `scatter_mapbox` | map + box | Mapbox 산점도 | `px.scatter_mapbox(df, lat="lat", lon="lon")` |
| `scatter_geo` | geographic scatter | Geo 산점도 | `px.scatter_geo(df, lat="lat", lon="lon")` |
| `treemap` | tree + map | 계층 트리맵 | `px.treemap(df, path=["A","B"], values="val")` |
| `sunburst` | 원형 계층 | 선버스트 | `px.sunburst(df, path=["A","B"], values="val")` |
| `funnel` | funnel | 퍼널 분석 | `px.funnel(df, x="stage", y="val")` |

---

## 2. plotly.graph_objects — 정교한 객체 API (+ 사용 예시)

| 객체 | 어원 (뜻) | 설명 | 사용 예시 |
| --- | --- | --- | --- |
| `Figure` | figure | 전체 그래프 컨테이너 | `fig = go.Figure()` |
| `go.Scatter` | scatter plot | 선/점 trace | `go.Scatter(x=[1,2], y=[3,4])` |
| `go.Bar` | bar chart | 막대 trace | `go.Bar(x=cat, y=cnt)` |
| `go.Pie` | pie chart | 원형 차트 | `go.Pie(values=v, labels=lab)` |
| `go.Box` | box plot | 상자 trace | `go.Box(y=data)` |
| `go.Heatmap` | heat + map | 히트맵 trace | `go.Heatmap(z=z_mat)` |
| `go.Contour` | contour | 등고선 trace | `go.Contour(z=z_mat)` |
| `go.Surface` | surface | 3-D 표면 | `go.Surface(z=z_mat)` |
| `go.Mesh3d` | mesh | 3-D 메시 | `go.Mesh3d(x, y, z, i, j, k)` |
| `go.Indicator` | indicator | 숫자/게이지 | `go.Indicator(mode="number", value=42)` |
| `go.Layout` | layout | 레이아웃 설정 | `fig.update_layout(title="My Plot")` |
| `go.Annotation` | annotation | 주석 | `fig.add_annotation(text="Note", x=1, y=1)` |

## 💡 Plotly 내부 네이밍 규칙 요약

- `scatter`, `line`, `bar` 등은 모두 **시각화 기법의 이름**을 그대로 따름
- `go`는 `graph_objects`의 줄임말 → 객체 기반 인터페이스를 의미
- `express`는 "빠르고 간편한" 인터페이스를 뜻함

# 📊 Plotly 그래프를 만들 때 넣어야 하는 **입력 객체** 요약

## 1. plotly.express (px) ― “간단·빠른” 방식

| 특징 | 입력 형식 | 예시 코드 |
| --- | --- | --- |
| **대부분의 px 함수** (`px.scatter`, `px.line`, `px.bar` …) | **`pandas.DataFrame`** + 열 이름 문자열 (`x="열"`, `y="열"`, `color="열"` …) | `import plotly.express as px, pandas as pd
df = pd.DataFrame({"x":[1,2,3], "y":[3,1,2]})
fig = px.scatter(df, x="x", y="y")
fig.show()` |
| `px.imshow` | 2-D 배열 / 이미지 행렬 | `fig = px.imshow(img_array)` |
| 3-D·지도 함수 (`px.line_3d`, `px.scatter_mapbox` 등) | 위·경도, 3-D 좌표 컬럼 포함한 DataFrame | `fig = px.scatter_mapbox(df, lat="lat", lon="lon")` |

> px 함수는 내부에서 자동으로 go.Figure를 만들어 반환하므로, fig.show()만 호출하면 바로 시각화!
> 

---

## 2. plotly.graph_objects (go) ― “정교·유연” 방식

| 구성 요소 | 역할 | 입력 형식 | 예시 |
| --- | --- | --- | --- |
| `go.<TraceType>`<br>(예: `go.Scatter`, `go.Bar`, `go.Surface`) | **데이터 시리즈(trace)** 생성 | 리스트, `np.array`, 파이썬 숫자 시퀀스 | `trace = go.Scatter(x=[1,2,3], y=[10,20,15])` |
| `go.Figure` | **그래프 전체 객체** | Trace(s) + 레이아웃(dict) | `fig = go.Figure(trace)` |
| `fig.show()` | 브라우저 / 노트북에 출력 | — | `fig.show()` |

> go.Scatter 단독으로는 화면에 아무것도 안 뜸.
> 
> 
> **항상 `go.Figure`에 담은 뒤 `.show()`** 해야 시각화된다.
> 

---

## 3. Jupyter Notebook 특이사항

- 노트북 셀 마지막 줄이 `fig` 객체면 `fig.show()` 없이도 **자동 렌더**.
    
    ```python
    fig = px.line(x=[1,2,3], y=[2,4,1])
    fig    # 셀 실행 시 바로 그래프 표시
    ```
    

# 📐 Pandas・SymPy 그래프 함수에 넣는 **데이터 타입 요약**

## 1. Pandas — `Series.plot()`, `DataFrame.plot()` 계열

| 호출 패턴 | 넣는 인자 | 기대 타입 | 비고 |
| --- | --- | --- | --- |
| `Series.plot()` | (선택) `kind="line" \| "bar" …` | **`pandas.Series`** | 시리즈 값이 y축, 인덱스가 x축 |
| `DataFrame.plot()` | (선택) `x=`, `y=` | **`pandas.DataFrame`** | 여러 열을 한 번에 — 열 이름으로 매핑 |
| `df.plot.scatter(x="col1", y="col2")` | `x`, `y` | **문자열(열 이름)** | 두 열을 지정한 산점도 |
| `df.plot(kind="hist")` | (없음) | DF/Series 내부 **수치형 칼럼 자동 선택** | 복수 열이면 겹쳐 그리기 |
| `df["col"].plot(kind="hist")` | (없음) | **Series** | 단일 열 히스토그램 |
| `df.plot.box()` | (없음) | DataFrame | 각 열별 박스플롯 |
| `df.plot()` + 매개변수 축약 | `use_index=True/False`, `secondary_y` 등 | **bool 또는 list-like** | 축 지정, 2차 y축 등 |

**허용되는 “데이터”**

- 내부적으로는 **`numpy.ndarray` 형으로 변환**되므로*Python 리스트*, *NumPy 배열*도 `DataFrame/Series` 로 감싸면 사용 가능
- 인덱스가 **`DatetimeIndex`*이면 시계열 축으로 자동 처리

---

## 2. SymPy — `plot`, `plot_implicit`, `plot3d` 등

| 함수 | 대표 시그니처 | 넣는 인자 타입 | 설명 |
| --- | --- | --- | --- |
| `plot` | `plot(expr, (var, a, b))` | **`Expr`** (수식), **`Symbol`**, **숫자** | 2-D 단일 함수<br>예: `plot(sin(x), (x, 0, 2*pi))` |
| (다중) | `plot(expr1, expr2, …, (var, a, b))` | **여러 Expr** | 같은 범위에 여러 곡선 |
| `plot_parametric` | `plot_parametric(expr_x, expr_y, (t, a, b))` | **두 Expr** | 파라미트릭 2-D |
| `plot3d` | `plot3d(expr, (x, a, b), (y, c, d))` | **`Expr`(x,y)** | 3-D 표면 |
| `plot_implicit` | `plot_implicit(Eq(expr, 0))` | **`Eq`** 또는 **불리언** | 암시적 곡선/영역 |
| `plot_vector` | `plot_vector(vector_field, range_tuple(s))` | **Tuple of Expr** | 2-D/3-D 벡터장 화살표 |
| `plot3d_parametric_line` | `plot3d_parametric_line(x(t), y(t), z(t), (t, a, b))` | **3 Expr** | 3-D 파라미트릭 선 |

### SymPy 인자 규칙 한눈에

| 필요 요소 | 허용 타입 |
| --- | --- |
| **수식** | `sympy.Expr` (`sin(x)`, `x**2` …) |
| **변수** | `sympy.Symbol` (`x`, `y`, `t`) |
| **구간** | `(Symbol, start, end)` tuple — `start`, `end`은 **수 또는 Expr** |
| **방정식/부등식** | `Eq`, `Gt`, `Lt` … (암시적 그래프용) |

> 🔸 SymPy는 순수 파이썬 수식만 받으며, NumPy 배열·리스트 직접 전달은 불가
> 
> 
> 🔸 내부적으로 Matplotlib으로 렌더링하지만 **데이터 준비 단계**는 전부 “심볼릭 객체”
> 

---

## 📝 기억 포인트

1. **Pandas**: 대부분 `DataFrame`/`Series` 기반, `x=`, `y=` 인자에 **“열 이름(문자열)”**을 넣어 칼럼을 매핑.
2. **SymPy**: 순수 기호 + 수식 + 범위 `tuple` 조합이 필수. 리스트·배열이 아니라 **`Expr`, `Symbol`** 중심.
3. Pandas가 받지 못하는 Python 원시 시퀀스는 `Series`/`DataFrame`으로 래핑하면 해결, SymPy는 수식으로 변환해야 한다.

# 📈 파이썬 데이터/수학 관련 모듈에서 나오는 주요 그래프 종류 정리

---

## 📌 1. SymPy — 수학 수식 시각화

| 그래프 종류 | 함수 | 특징 | 사용 예 |
| --- | --- | --- | --- |
| 2D 함수 그래프 | `plot()` | 단순 수식 그래프 (선형, 다항, 지수 등) | `plot(x**2 - 3*x)` |
| 2D 암시적 그래프 | `plot_implicit()` | 암시적 방정식의 해 영역 표현 | `plot_implicit(Eq(x**2 + y**2, 1))` |
| 3D 곡면 그래프 | `plot3d()` | \( z = f(x, y) \) 형태 함수 시각화 | `plot3d(x**2 + y**2)` |

> ✔ 대수식 기반 시각화 / 내부적으로 matplotlib 사용
> 
> 
> ✔ 대체로 **기초 수학/공식 검증용 시각화**에 적합
> 

---

## 📌 2. NumPy — 직접 그래프는 없음

- NumPy는 **데이터 생성, 수치 계산용** 모듈로, 그래프를 직접 그리지는 않음
- 그러나 `matplotlib`이나 `plotly`에 넘겨줄 **데이터를 생성**하는 데 자주 사용됨

```python
import numpy as np
x = np.linspace(-10, 10, 100)
y = np.sin(x)

```

---

## 📌 3. Pandas — 통계형 그래프 내장

| 그래프 종류 | 메서드 | 특징 | 사용 예 |
| --- | --- | --- | --- |
| 선 그래프 | `plot.line()` 또는 `plot()` | 기본 그래프, 시계열에 많이 사용 | `df.plot()` |
| 막대그래프 | `plot.bar()` | 범주형 데이터 비교 | `df.plot.bar()` |
| 수직 막대그래프 | `plot.barh()` | 가로 방향 | `df.plot.barh()` |
| 히스토그램 | `plot.hist()` | 데이터 분포 보기 | `df.plot.hist()` |
| 박스플롯 | `plot.box()` | 이상치·분포 확인 | `df.plot.box()` |
| 산점도 | `plot.scatter()` | 두 변수 관계 | `df.plot.scatter(x="a", y="b")` |
| 파이 차트 | `plot.pie()` | 비율 표시 | `df['col'].plot.pie()` |

> ✔ matplotlib 기반
> 
> 
> ✔ 데이터프레임 기반이라 **빠르게 탐색적 분석(EDA)** 가능
> 

---

## 📌 4. SciPy — 통계/신호 그래프

| 그래프 종류 | 메서드 | 사용 예 |
| --- | --- | --- |
| 정규분포 / 이항분포 등 확률밀도 함수 | `scipy.stats.norm.pdf()` 등 | 분포 시각화 (`plt.plot(x, norm.pdf(x))`) |
| 누적분포 함수 | `cdf()` | 확률 누적 시각화 |
| 분위수 함수 | `ppf()` | 역분포 시각화 |
| 푸리에 변환 | `fft` 결과 시각화 | 주파수 분석 (신호 처리) |
| 적분된 함수 | `integrate.quad` 결과 그래프 | 면적 계산 확인용 |

> ✔ 자체적으로 그래프는 생성하지 않으며 matplotlib 또는 plotly와 함께 사용
> 
> 
> ✔ **통계적 분포와 수치해석 시각화**에 적합
> 

---

## 📌 5. Plotly — 고급 시각화 (대화형)

| 그래프 종류 | 함수명 (`px.` 기준) | 특징 | 사용 예 |
| --- | --- | --- | --- |
| 선 그래프 | `px.line()` | 연속 데이터 / 시계열 | 가격, 온도 |
| 산점도 | `px.scatter()` | 변수 관계 시각화 | 클러스터링 |
| 막대그래프 | `px.bar()` | 범주형 비교 | 판매량 |
| 박스플롯 | `px.box()` | 분포와 이상치 확인 | 시험점수 |
| 바이올린플롯 | `px.violin()` | 분포 밀도 + 중위값 | 밀도 비교 |
| 히스토그램 | `px.histogram()` | 데이터 분포 | 나이 분포 |
| 파이차트 | `px.pie()` | 비율 시각화 | 시장 점유율 |
| 선버스트/트리맵 | `px.sunburst()`, `px.treemap()` | 계층 구조 | 파일 시스템 구조 |
| 히트맵 | `px.density_heatmap()` | 2D 분포 시각화 | 상관관계 |
| 3D 그래프 | `px.scatter_3d()`, `px.line_3d()` | 3차원 관계 | 공간 분석 |
| 지도 기반 그래프 | `px.scatter_geo()`, `px.scatter_mapbox()` | 위도/경도 기반 | 위치 분석 |

> ✔ 내부적으로 D3.js 기반
> 
> 
> ✔ **대화형, 고해상도, 웹 공유 가능**
> 
> ✔ EDA, 프레젠테이션, 리포트 시각화에 적합
> 

---

## ✅ 총정리 비교표

| 모듈 | 그래프 생성 가능 여부 | 주요 그래프 | 특징 |
| --- | --- | --- | --- |
| **SymPy** | ✅ (기초 그래프) | 함수 그래프, 암시적, 3D | 수식 기반, 수학적 검증 |
| **NumPy** | ❌ (직접 생성 없음) | — | 데이터 생성용 |
| **Pandas** | ✅ (기본 그래프) | 선, 막대, 산점도, 박스 | EDA 중심, 간편 |
| **SciPy** | ❌ (직접 생성 없음) | 확률분포 시각화 등 | 통계·수치 계산용, matplotlib 연동 |
| **Plotly** | ✅ (고급 대화형) | 거의 모든 그래프 | 발표용, 웹 기반 시각화 강점 |