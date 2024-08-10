import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px

st.title("[jwan코치_05팀] 2주차 미션")
st.divider()

st.write("## 데이터 확인하기")

col_num = st.slider("컬럼 수 조절하기", 0, 100, 10)

df = pd.read_csv("medical_201909.csv", low_memory=False)
st.dataframe(df.head(col_num))

st.divider()

st.write("""
## Q1. 전국 시도별 약국수를 구해주세요!

* 상권업종소분류명이 약국인 것을 찾아 빈도수를 구해주세요. 이 때, `value_counts`, `groupby`, `pivot_table` 등 다양한 집계 방법을 통해 구해볼 수 있습니다. 각자 구하기 편한 방법을 통해 빈도수를 구합니다.
* 다음의 결과가 나오도록 구합니다.

```plain
경기도        4510
서울특별시      3579
부산광역시      1130
경상남도       1017
인천광역시      1002
경상북도        915
대구광역시       870
전라북도        862
충청남도        830
전라남도        811
강원도         729
광주광역시       691
충청북도        648
대전광역시       603
울산광역시       362
제주특별자치도     226
세종특별자치시      99

```
""")

st.write("""
## **미션1. 풀이 (1)**
**[풀이 의도]**

* 먼저, 데이터에 `상권업종소분류명`이 있는지 확인
* 해당 데이터에서 `상권업종소분류명`에서 **약국**이 있는지 확인
* "약국" 데이터에서 `시도명`컬럼을 기준으로 데이터를 count
""")

st.code("""
# 데이터에 상권업종소분류명이 있는지 확인하는 코드
"상권업종소분류명" in df.columns
        
# result : True
""", language="python"
)


st.code("""
# 전체 데이터에서 상권업종소분류명이 있으므로
# 해당 데이터에서 상권업종소분류명에서 "약국"이 있는지 확인
"약국" in df["상권업종소분류명"].tolist()
        
# result : True
""", language="python")

st.code("""
# 상권업종소분류명에서 "약국"인 데이터를 필터링한 결과
pharmacy = df[df["상권업종소분류명"]=="약국"]
""", language="python")

pharmacy = df[df["상권업종소분류명"]=="약국"]
st.dataframe(pharmacy.head(10))


st.code("""
# 상권업종소분류명에서 "약국"인 데이터를 필터링한 결과에서 "시도명"을 중심으로 데이터를 count
pharmacy["시도명"].value_counts()
""", language="python")

st.dataframe(pharmacy["시도명"].value_counts(), use_container_width=True)

st.divider()

st.write("""
## Q2. 여러분은 반려동물과 관련된 사업을 하는 스타트업에 취업을 하여 상권분석을 해달라는 요청을 받았습니다. 병원이나 약국은 인구나 유동인구가 많은 지역에 주로 위치하고 있습니다. 그렇다면 동물병원도 병원이나 약국이 많은 곳에 더 많이 있을까요?

* 빈도수를 구하고 시각화 하여 동물병원이 어느 지역에 많은지 분석해 주세요!
* 다음의 결과가 나오도록 구합니다.

```plain
경기도        992
서울특별시      557
인천광역시      193
경상북도       165
경상남도       161
부산광역시      153
충청남도       131
대구광역시      119
전라북도       111
강원도         85
대전광역시       77
전라남도        77
충청북도        75
광주광역시       71
울산광역시       61
제주특별자치도     46
세종특별자치시     13
Name: 시도명, dtype: int64
```
""")

st.write("""
## **미션2. 풀이**
**[풀이 의도]**

* 데이터에서 `상권업종소분류명`에서 **동물병원**이 있는지 확인
* 해당 데이터에서 `시도명`컬럼을 기준으로 데이터를 count
""")

animal_hospital = df[df["상권업종소분류명"]=="동물병원"]
st.code(
    'animal_hospital = df[df["상권업종소분류명"]=="동물병원"]',
    language="python"
)

st.write("### 전국 동물병원 분포도")
st.write("`animal_hospital`데이터에서 전국 동물병원의 수를 확인한 결과는 다음과 같음")


fig = px.bar(
    data_frame = animal_hospital["시도명"].value_counts(),
    x = "count",
    orientation='h'
)


st.plotly_chart(fig, use_container_width=True)

st.write("### 전국 동물병원 데이터")
st.dataframe(animal_hospital)

st.write("""
**[시각화 결과]**

* "경기도"의 비중이 32%로 가장 많은 것을 확인할 수 있음
* 미션1 에서 경기도에서 약국의 수가 가장 많은 것을 확인할 수 있었음
* 즉, 경기도는 "약국" 과 "동물병원"의 수가 가장 많음
         """)

st.write("""
## **미션2. 심화 : 풀이**
**[풀이 의도]**

* 전국 병원의 개수를 확인하여 전국에서 병원이 가장 많은 곳을 확인
""")

groub_df = df.groupby("시도명")["상권업종소분류명"].value_counts().unstack()
st.dataframe(groub_df)

fig2 = px.bar(
    x = groub_df.sum(axis=1).sort_values(ascending=False).values,
    y = groub_df.sum(axis=1).sort_values(ascending=False).index,
    orientation='h'
)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.write("""
## Q3. 강남지역에는 다른 지역에 비해 피부과나 성형외과가 많아 보입니다. 실제로 해당 지역에 피부과나 성형외과가 다른 지역에 비해 전체 병원 수 중에서 어느 정도의 비율을 차지하고 있는지 알아보겠습니다.
* 서울에 소재한 병원 중 상권업종소분류명에 "피부" 나 "성형"이 들어간 분류명을 찾아 구해주세요!
* 피부과 성형외과 수 / 전체병원 수 로 비율을 구해주세요!
* 비율이 높은 순서대로 정렬되게 구해주세요!
* 수업에서 사용한 같은 CSV 파일을 사용하며 다음의 결과가 나오도록 구합니다.
* 소숫점 두 번째짜리까지 출력하는 방법은 pandas round 로 검색해서 사용법을 알아보세요!

```plain
시군구명
강남구     0.24
서초구     0.17
마포구     0.09
영등포구    0.08
서대문구    0.08
강서구     0.07
강동구     0.07
중구      0.07
양천구     0.07
중랑구     0.07
성북구     0.06
송파구     0.06
구로구     0.06
은평구     0.06
광진구     0.06
노원구     0.05
성동구     0.05
금천구     0.05
용산구     0.05
강북구     0.05
동대문구    0.04
동작구     0.04
관악구     0.04
종로구     0.03
도봉구     0.02
```

""")

st.divider()

st.write("""
## **미션3. 풀이(1)**
**[풀이 의도]**
* `시도명`이 **서울특별시**인 곳에서 `상권업종소분류명`이 **병원**인 곳을 추출
* 상권업종소분류명에서 "피부", "성형"인 곳을 찾아 필터링
* 피부과 성형외과 수 / 전체병원 수 로 비율을 찾아 오름차순 정렬 (소숫점 두 번째짜리까지 출력)
""")

seoul_df = df[(df["시도명"]=="서울특별시") & (df["상권업종중분류명"]=="병원")]
st.code("""
seoul_df = df[(df["시도명"]=="서울특별시") & (df["상권업종중분류명"]=="병원")]
""")
st.dataframe(seoul_df)



target = [s for s in set(seoul_df["상권업종소분류명"].to_list()) if "피부" in s or "성형" in s]
st.code("""
target = [s for s in set(seoul_df["상권업종소분류명"].to_list()) if "피부" in s or "성형" in s]
print(target)
        
#result : ['피부과', '정형/성형외과']
""")


target_df = seoul_df[(seoul_df["상권업종소분류명"]==target[0])|(seoul_df["상권업종소분류명"]==target[1])]
st.code("""
# '피부과', '정형/성형외과' 인 곳을 추출
target_df = seoul_df[(seoul_df["상권업종소분류명"]==target[0])|(seoul_df["상권업종소분류명"]==target[1])]
""")
st.dataframe(target_df)

result2 = round(target_df["시군구명"].value_counts()/seoul_df["시군구명"].value_counts(),2)
result2 = result2.sort_values(ascending=False)
st.code("""
result2 = round(target_df["시군구명"].value_counts()/seoul_df["시군구명"].value_counts(),2)
result2.sort_values(ascending=False)
""")
st.dataframe(result2, use_container_width=True)

st.write("""
## **미션3. 풀이(2)**
**[풀이 의도]**
* `시도명`이 **서울특별시**인 곳에서 `상권업종소분류명`이 **병원**인 곳을 추출
* 각 구에서 파이차트로 시각화
""")

option = st.selectbox(
    "확인하고 싶은 지역을 선택해 주세요.",
    set(seoul_df["시군구명"].to_list()),
)

gu_count = seoul_df[seoul_df["시군구명"] == option].value_counts("상권업종소분류명")

fig2 = px.pie(
    values=gu_count.values, 
    names=gu_count.index
    )

fig2.update_traces(pull= [0.3 if "정형/성형외과" in s or "피부과" in s else 0 for s in gu_count.index])

skin = gu_count.loc['피부과']
plastic_surgery = gu_count.loc['정형/성형외과']

st.write(f"{option} 의 피부과 비율:", round(skin/gu_count.sum(), 3))
st.write(f"{option} 의 정형/성형외과 비율:", round(plastic_surgery/gu_count.sum(), 3))
st.write(f"{option} 의 피부과, 정형/성형외과 비율:", round((skin + plastic_surgery)/gu_count.sum(), 3))

st.plotly_chart(fig2, use_container_width=True)

st.divider()