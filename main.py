import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px


st.title("[jwan코치_05팀] 2주차 미션")
st.divider()

st.write("### 개요")
st.write("""
**jwan코치_05팀**의 2주차 미션은 각자 제출한 코드를 조합하였습니다.

그리고 Streamlit으로 재구성하여 반응형 웹으로 구성하였습니다.
         
**[제출자 전체 내용 확인 링크]**
""")

user_info = {
    "제출자": [
        "김용진", "박기범", "Hani Bae", "김기훈", "강혜림", "양연희", "이지수", "박재홍"
    ],
    "제출링크": [
        "https://boostmission2-n2ovwylqxatx9vtmovooxf.streamlit.app/", 
        "박기범", 
        "https://drive.google.com/file/d/1lWwbjNIbFRlBQaZz1W4c-_P5LPe6S416/view?usp=sharing", 
        "김기훈", 
        "강혜림", 
        "https://colab.research.google.com/drive/1YUM9hvnnqWQSDG1datiHTmR4137_ZqTZ?usp=sharing", 
        "https://drive.google.com/file/d/1mE1oTVBKUyqIgx32541ktzmOdTiOPFQF/view?usp=sharing", 
        "https://drive.google.com/file/d/1nV5oimvmtbRSeJRrfECl1hwXiQVKNSwr/view?usp=sharing"    
    ]
}

user_df = pd.DataFrame(user_info)

st.table(user_df)

info, quiz1, quiz2, quiz3, quiz4 = st.tabs(["Info", "Quiz 1", "Quiz 2", "Quiz 3", "Quiz 4"])

with info :
    st.write("### 데이터 확인하기")

    col_num = st.slider("컬럼 수 조절하기", 0, 100, 10)

    df = pd.read_csv("medical_201909.csv", low_memory=False)
    st.dataframe(df.head(col_num))
    
with quiz1 :
    st.write("### Quiz 1")
    st.write("""
상권업종소분류명이 약국인 것을 찾아 빈도수를 구해주세요. 이 때, `value_counts`, `groupby`, `pivot_table` 등 다양한 집계 방법을 통해 구해볼 수 있습니다. 각자 구하기 편한 방법을 통해 빈도수를 구합니다.
다음의 결과가 나오도록 구합니다.
             """)
    
    st.write("""### **미션1. 풀이 (1)**""")

    with st.echo() : 
        st.dataframe(
            # 작성자 : 이지수 
            # Streamlit 적용 : 김용진
            # 시도별 약국수 빈도 확인

            df.loc[df["상권업종소분류명"] == "약국", "시도명"].value_counts(),
            use_container_width=True
        )

    st.write("""### **미션1. 풀이 (2)**""")

    with st.echo() :
        st.dataframe(
            # 작성자 : 배하니 
            # Streamlit 적용 : 김용진
            # 시도별 약국수 빈도 확인

            df[df['상권업종소분류명'] == '약국'].groupby(['시도명'])['상가업소번호'].count().sort_values(ascending = False),
            use_container_width=True
        )

with quiz2 :
    st.write("### Quiz 2")
    st.write("""
여러분은 반려동물과 관련된 사업을 하는 스타트업에 취업을 하여 상권분석을 해달라는 요청을 받았습니다. 병원이나 약국은 인구나 유동인구가 많은 지역에 주로 위치하고 있습니다. 그렇다면 동물병원도 병원이나 약국이 많은 곳에 더 많이 있을까요?
    """)

    st.write("""### **미션2. 풀이**""")

    with st.echo() : 
        st.dataframe(
            # 작성자 : 김용진

            df[df["상권업종소분류명"]=="동물병원"],
            use_container_width=True
        )

    animal_hospital = df[df["상권업종소분류명"]=="동물병원"]

    st.write("### 전국 동물병원 분포도")
    st.write("`animal_hospital`데이터에서 전국 동물병원의 수를 확인한 결과는 다음과 같음")
    st.code("""
            animal_hospital = df[df["상권업종소분류명"]=="동물병원"]
            """, language="python")

    with st.echo() :
        import plotly.express as px
        # matplotlib이 아닌 plotly 라이브러리 사용
        # 작성자 : 김용진 

        fig1 = px.bar(
            data_frame = animal_hospital["시도명"].value_counts(),
            x = "count",
            orientation='h'
        )
        st.plotly_chart(fig1, use_container_width=True)

    st.write("""
**[시각화 결과]**

* "경기도"의 비중이 가장 많은 것을 확인할 수 있음
* 미션1 에서 경기도에서 약국의 수가 가장 많은 것을 확인할 수 있었음
* 즉, 경기도는 "약국" 과 "동물병원"의 수가 가장 많음
""")


with quiz3 :
    st.write("### Quiz 3")
    st.write("강남지역에는 다른 지역에 비해 피부과나 성형외과가 많아 보입니다. 실제로 해당 지역에 피부과나 성형외과가 다른 지역에 비해 전체 병원 수 중에서 어느 정도의 비율을 차지하고 있는지 알아보겠습니다.")

    st.write("""### **미션3. 풀이(1)**""")

    with st.echo()  : 
        st.dataframe(
            # 작성자 : 김용진 

            df[(df["시도명"]=="서울특별시") & (df["상권업종중분류명"]=="병원")]
        )

    seoul_df = df[(df["시도명"]=="서울특별시") & (df["상권업종중분류명"]=="병원")]
    st.code(
        """
        seoul_df = df[(df["시도명"]=="서울특별시") & (df["상권업종중분류명"]=="병원")]
        """,
        language = "python"
    )

    with st.echo() : 
        st.dataframe(
            # 작성자 : 이지수 
            # 수정자 : 김용진

            seoul_df[seoul_df["상권업종소분류명"].str.contains("피부|성형")].value_counts("시군구명"),
            use_container_width=True
        )

    with st.echo() :
        st.dataframe(
            # 전체 병원 수에서 "피부", "성형"이 들어간 병워명을 나누는 코드
            # 작성자 : 이지수 
            # 수정자 : 김용진

            round(seoul_df[seoul_df["상권업종소분류명"].str.contains("피부|성형")].value_counts("시군구명")/seoul_df.value_counts("시군구명"), 2),
            use_container_width=True
        )
    
    st.write("""### **미션3. 풀이(2)**""")
    
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


with quiz4 :
    st.write("### Quiz 4")

    df.rename(columns={"위도":"lat", "경도":"lon"}, inplace=True)

    option = st.selectbox(
    "확인하고 싶은 상권업종소분류명을 선택해 주세요.",
    set(df["상권업종소분류명"].to_list())
    )

    filter_df = df[df["상권업종소분류명"] == option]
    st.dataframe(filter_df)

    st.map(filter_df[["lat", "lon"]])
