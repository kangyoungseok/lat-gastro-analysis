# LAT. GASTRO %MVC Analysis

승강식 피난기 손잡이 높이 조건(83cm, 93cm, 103cm)에 따른
LAT. GASTRO %MVC 변화를 분석한 프로젝트입니다.

반복 측정 데이터를 피험자 단위로 정리한 뒤,
조건별 기술통계, 시각화, Repeated Measures ANOVA,
paired t-test 및 Bonferroni correction을 수행했습니다.

반복적으로 사용하는 데이터 처리 및 통계 과정은
`analysis_pipeline.py`로 모듈화하여 재사용할 수 있도록 구성했습니다.

## Project Structure

```text
.
├─ lat_gastro_public.csv
├─ lat_gastro_analysis.ipynb
├─ analysis_pipeline.py
└─ README.md
```

## Files

- `lat_gastro_analysis.ipynb`
  - 데이터 구조 및 결측 확인
  - 피험자별·조건별 trial coverage 확인
  - 피험자별 조건 평균 계산
  - 조건별 기술통계
  - 개인별 반응 및 평균 ± SD 시각화
  - Repeated Measures ANOVA
  - paired t-test 및 Bonferroni 보정
  - 최종 결과 해석

- `analysis_pipeline.py`
  - 반복적으로 사용하는 데이터 처리 및 통계 함수를 모듈화
  - 분석 대상 변수는 `value_col`로 전달
  - 동일한 데이터 구조를 가진 다른 변수에도 재사용 가능

- `lat_gastro_public.csv`
  - 본 분석에 사용한 LAT. GASTRO %MVC 데이터

## Analysis Workflow

```text
CSV data
   ↓
Basic QC & trial coverage
   ↓
Subject × condition mean
   ↓
Descriptive statistics
   ↓
Visualization
   ↓
Complete-case preparation
   ↓
Repeated Measures ANOVA
   ↓
Paired post-hoc tests
   ↓
Bonferroni correction
```

## Main Results

Repeated Measures ANOVA 결과,
손잡이 높이 조건에 따른 LAT. GASTRO %MVC 차이가 통계적으로 유의하였다.

- RM-ANOVA: F(2, 42) = 4.986, p = 0.011
- Bonferroni 보정 후 93cm와 103cm 조건 간 차이만 유의
- 83cm-93cm, 83cm-103cm 비교는 보정 후 유의하지 않음

본 결과는 LAT. GASTRO 단일 근육의 분석 결과이며,
특정 손잡이 높이를 최적 조건으로 단정하기 위한 결과로 해석하지 않았다.

## Tools

- Python
- pandas
- matplotlib
- SciPy
- statsmodels
- Jupyter Notebook

## Installation

필요한 Python 패키지는 다음 명령으로 설치할 수 있습니다.

```bash
pip install -r requirements.txt

## Reproducibility

분석은 Jupyter Notebook에서 위에서 아래 순서대로 실행되도록 구성하였다.

분석 대상 변수는 Notebook 상단에서 다음과 같이 지정한다.

```python
value_col = "lat_gastro_percent_mvc"
```

`analysis_pipeline.py`의 함수들은 `value_col`을 입력받도록 구성하여,
동일한 데이터 구조를 가진 다른 분석 변수에도 재사용할 수 있도록 하였다.

분석 재현 시 Notebook 커널을 재시작한 뒤
`Run All`을 실행하면 동일한 분석 흐름을 재현할 수 있다.