# 📊 Plotly 그래프를 만들 때 넣어야 하는 **입력 객체** 요약

## 1. plotly.express (px) ― “간단·빠른” 방식
| 특징 | 입력 형식 | 예시 코드 |
|------|-----------|-----------|
| **대부분의 px 함수** (`px.scatter`, `px.line`, `px.bar` …) | **`pandas.DataFrame`** + 열 이름 문자열 (`x="열"`, `y="열"`, `color="열"` …) | ```python<br>import plotly.express as px, pandas as pd<br>df = pd.DataFrame({"x":[1,2,3], "y":[3,1,2]})<br>fig = px.scatter(df, x="x", y="y")<br>fig.show()<br>``` |
| `px.imshow` | 2-D 배열 / 이미지 행렬 | `fig = px.imshow(img_array)` |
| 3-D·지도 함수 (`px.line_3d`, `px.scatter_mapbox` 등) | 위·경도, 3-D 좌표 컬럼 포함한 DataFrame | `fig = px.scatter_mapbox(df, lat="lat", lon="lon")` |

> **px 함수는 내부에서 자동으로 `go.Figure`를 만들어 반환**하므로, `fig.show()`만 호출하면 바로 시각화!

---

## 2. plotly.graph_objects (go) ― “정교·유연” 방식
| 구성 요소 | 역할 | 입력 형식 | 예시 |
|-----------|------|-----------|------|
| `go.<TraceType>`<br>(예: `go.Scatter`, `go.Bar`, `go.Surface`) | **데이터 시리즈(trace)** 생성 | 리스트, `np.array`, 파이썬 숫자 시퀀스 | `trace = go.Scatter(x=[1,2,3], y=[10,20,15])` |
| `go.Figure` | **그래프 전체 객체** | Trace(s) + 레이아웃(dict) | `fig = go.Figure(trace)` |
| `fig.show()` | 브라우저 / 노트북에 출력 | — | `fig.show()` |

> `go.Scatter` **단독**으로는 화면에 아무것도 안 뜸.  
> **항상 `go.Figure`에 담은 뒤 `.show()`** 해야 시각화된다.

---

## 3. Jupyter Notebook 특이사항
- 노트북 셀 마지막 줄이 `fig` 객체면 `fig.show()` 없이도 **자동 렌더**.
  ```python
  fig = px.line(x=[1,2,3], y=[2,4,1])
  fig    # 셀 실행 시 바로 그래프 표시
