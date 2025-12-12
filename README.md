# MAP - Charting Student Math Misunderstandings

자연언어처리 수업 프로젝트(25-2)로 진행하는 **수학 문제에 대한 학생 오답/설명 기반 오개념(Misconception) 분류** 과제이다.  
학생이 선택한 객관식 정답(MC_Answer)과 그에 대한 자연어 설명(Student Explanation)을 보고,  
해당 설명이 어떤 유형의 오개념에 해당하는지 분류하는 것이 목표이다.

---

## Dataset

데이터는 `train.csv`, `test.csv`, `sample_submission.csv` 세 파일로 구성된다.

### train/test.csv 컬럼 설명

| Column             | 설명                                                                 |
|--------------------|----------------------------------------------------------------------|
| `QuestionId`       | 각 문항을 구분하는 고유 ID                                          |
| `QuestionText`     | 수학 문제의 실제 텍스트                                             |
| `MC_Answer`        | 학생이 선택한 객관식 보기(정답/오답 여부와 무관)                   |
| `Student Explanation` | 학생이 해당 보기를 선택한 이유를 서술한 자연어 설명                 |
| `Category` (train only) | MC_Answer와 Student Explanation 간 관계를 나타내는 분류 레이블 |
| `Misconception` (train only) | `Category`가 오개념을 포함하는 경우에만 지정되는 오개념 유형, 그 외에는 `NA` |

### Submission 형식 (`sample_submission.csv`)

제출 파일에는 다음과 같은 형식의 컬럼이 포함된다.

- **`Category:Misconception`**
  - `Category`와 `Misconception`을 `:`(콜론)으로 이어 붙인 문자열
  - 예시:
    - `Correct:NA`
    - `Misconception_Arithmetic:Carry_Misunderstanding`
    - `Misconception_Fraction:Denominator_Misunderstanding`

모델의 최종 출력은 각 샘플에 대해 `Category:Misconception` 문자열을 예측하는 형태이다.

---

## Task Objective

- 학생의 설명(자연어 텍스트)를 기반으로,
- 선택한 보기(`MC_Answer`)와의 관계(`Category`)와
- 해당 설명이 포함하는 오개념 유형(`Misconception`)을 함께 예측하는 NLP 분류 문제이다.

---

## Project Structure

```bash
MAP-NLP/
├─ data/
│  ├─ train.csv
│  ├─ test.csv
│  └─ sample_submission.csv
├─ notebooks/
│  ├─ 01_eda.ipynb
│  └─ 02_baseline_model.ipynb
├─ src/
│  ├─ data_loader.py
│  ├─ model.py
│  └─ utils.py
├── requirements.txt
├── README.md
└── .gitignore