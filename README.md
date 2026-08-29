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
├─ requirements.txt
├─ README.md
├─ .gitignore
└─ .gitattributes
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
  - 공개용으로 익명화한 LAT. GASTRO %MVC 분석 데이터
  - 분석에 필요한 최소 컬럼만 포함

- `requirements.txt`
  - 분석 실행에 필요한 Python 패키지 목록

  ## Dataset

공개용 데이터셋은 318개의 trial과 23명의 피험자로 구성되어 있습니다.

Repeated Measures ANOVA에서는 세 조건(83cm, 93cm, 103cm)의
조건 평균이 모두 존재하는 피험자만 complete-case로 포함하였으며,
최종 분석에는 22명의 피험자가 사용되었습니다.

공개 CSV는 분석에 필요한 핵심 변수와 연구 맥락을 위한 최소 메타데이터만 포함되어있습니다.

- `subject`: 익명화된 피험자 ID (`S001` ~ `S023`)
- `group`: 연령 집단 (`older`, `young`)
- `condition`: 손잡이 높이 조건 (`83cm`, `93cm`, `103cm`)
- `repeat`: 조건별 반복 trial 번호
- `lat_gastro_percent_mvc`: LAT. GASTRO 근활성도 (%MVC)

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
```

## Reproducibility

분석 대상 변수는 Notebook 상단의 `value_col`에서 지정하며,
동일한 데이터 구조를 가진 다른 분석 변수에도
`analysis_pipeline.py`의 함수를 재사용할 수 있도록 구성하였다.
