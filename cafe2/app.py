import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 

if st.checkbox('당신은 로봇입니까?') :
        st.text('당신은 로봇이 아닙니다.')



st.title(
    """
    강원랜드 인공지능 AI 빅데이터 기반
    """
    )


st.header("""
강원랜드_호텔 인공지능 무인카페 이용현황
""")

def main():
    df = pd.read_csv('./cafe2/data.csv', encoding='cp949')
    two = df.iloc[4588:5129]

    if st.button('데이터 보기'):
        st.dataframe(two)

if __name__ == '__main__' :
    main()





# ice = two.loc[two['상품명'] != 'hot']
# st.write(ice) 


df = pd.read_csv('./cafe2/data.csv', encoding='cp949')
three = df.iloc[5000:5020]
two = df.iloc[4588:5129]

#st.write(df['영업일자'])

first = df.iloc[:627]
second = df.iloc[627:1976]
third = df.iloc[1976:3518]
forth = df.iloc[3518:]



# fig = px.histogram(two, x="상품명")

# total_sum1 = first['판매수량'].sum()
# st.subheader(f"1분기 총 판매량 {total_sum1}잔 팔았습니다.")
# total_sum2 = second['판매수량'].sum()
# st.subheader(f"2분기 총 판매량 {total_sum2}잔 팔았습니다.")
# total_sum3 = third['판매수량'].sum()
# st.subheader(f"3분기 총 판매량 {total_sum3}잔 팔았습니다.")
# total_sum4 = forth['판매수량'].sum()
# st.subheader(f"4분기 총 판매량 {total_sum4}잔 팔았습니다.")


st.sidebar.header('Menu')
name = st.sidebar.selectbox('분기별 판매량', ['종류를 선택해주세요','1분기','2분기','3분기','4분기','전체'])

if name == '1분기':
    total_sum1 = first['판매수량'].sum()
    st.subheader(f"1분기 총 판매량 {total_sum1}잔 입니다!!")
    st.write(" ## 하루에 100잔 가량 팔립니다!! 놀라워요!")
    fig_first = px.histogram(first, x="상품명", y='판매수량',title='강원랜드의 한 무인 카페의 1분기 음료 판매량' )

    st.plotly_chart(fig_first)

    sample1 = first[first['상품명'].str.contains('아메리카노')]

    st.write("## HOT vs ICE")
    st.write("### 1분기의 승자는 HOT 입니다.")
    fug1 = px.histogram(sample1, x="상품명", y='판매수량')
    st.plotly_chart(fug1)


    st.write("## BEST 3")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("1.아메리카노 HOT 995잔")
        st.image("https://health.chosun.com/site/data/img_dir/2022/05/11/2022051101651_0.jpg")

    with col2:
        st.subheader("2.아메리카노 ICE 753잔")
        st.image("data:image/jpeg;base64,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")

    with col3:
	    st.subheader("3.카페라떼 HOT 204잔")
	    st.image("https://www.the-cup.co.kr/data/editor/1902/thumb-687c8d0c78d329e0c637df3050b1fd20_1550129060_1108_920x843.jpg")


    st.write("## WORST 3")
    st.write("### 쓰다!! ")
    col4, col5, col6 = st.columns(3)
    with col4:
        st.subheader("1.그린티라떼 ICE 19잔")
        st.image("https://health.chosun.com/site/data/img_dir/2022/05/11/2022051101651_0.jpg")

    with col5:
        st.subheader("2.그린티라떼 HOT 23잔")
        st.image("data:image/jpeg;base64,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")

    with col6:
	    st.subheader("3.흑당라떼 HOT 28잔")
	    st.image("https://www.the-cup.co.kr/data/editor/1902/thumb-687c8d0c78d329e0c637df3050b1fd20_1550129060_1108_920x843.jpg")


elif name == '2분기':

    total_sum2 = second['판매수량'].sum()
    st.subheader(f"2분기 총 판매량 {total_sum2}잔 팔았습니다.")

    fig_second = px.histogram(second, x="상품명", y='판매수량',title='강원랜드의 한 무인 카페의 2분기 음료 판매량' )

    st.plotly_chart(fig_second)

elif name == '3분기':

    total_sum3 = third['판매수량'].sum()
    st.subheader(f"3분기 총 판매량 {total_sum3}잔 팔았습니다.") 

    fig_third = px.histogram(third, x="상품명", y='판매수량',title='강원랜드의 한 무인 카페의 3분기 음료 판매량' )

    st.plotly_chart(fig_third)
    
elif name == '4분기':

    total_sum4 = forth['판매수량'].sum()
    st.subheader(f"4분기 총 판매량 {total_sum4}잔 팔았습니다.")

    fig_forth = px.histogram(forth, x="상품명", y='판매수량',title='강원랜드의 한 무인 카페의 4분기 음료 판매량' )

    st.plotly_chart(fig_forth)    

elif name == '전체':
    total_sum5 = df['판매수량'].sum()
    st.subheader(f"21년 총 판매량 {total_sum5}잔 팔았습니다.")



# fig_first = px.histogram(first, x="상품명", y='판매수량',title='강원랜드의 한 무인 카페의 1분기 음료 판매량' )

# st.plotly_chart(fig_first)
  
# fig_second = px.histogram(second, x="상품명", y='판매수량',title='강원랜드의 한 무인 카페의 2분기 음료 판매량' )

# st.plotly_chart(fig_second)

# fig_third = px.histogram(third, x="상품명", y='판매수량',title='강원랜드의 한 무인 카페의 3분기 음료 판매량' )

# st.plotly_chart(fig_third)

# fig_forth = px.histogram(forth, x="상품명", y='판매수량',title='강원랜드의 한 무인 카페의 4분기 음료 판매량' )

# st.plotly_chart(fig_forth)

# sample1 = first[first['상품명'].str.contains('아메리카노')]

# st.write("## HOT vs ICE")
# st.write("### 1분기의 승자는 HOT 입니다.")
# fug1 = px.histogram(sample1, x="상품명", y='판매수량')
# st.plotly_chart(fug1)

# two['ice'] = (
#     two.apply(lambda x: x. if r.age >= 20 else 'child', axis=1) # 행을 기준으로 가져옴
# )
# titanic.tail()

# fig1 = px.histogram(two, x="상품명", y='판매수량',title='강원랜드 12월 한달 커피 판매량' )

# st.plotly_chart(fig1)







# st.write("# BEST")

# st.write("## 1.아메리카노 (HOT) 1215잔 ")
# st.image("https://imagescdn.gettyimagesbank.com/500/201708/jv10960341.jpg")
# st.write("## 2.아메리카노 (ICE) 888잔 ")
# st.image("https://sitem.ssgcdn.com/29/96/11/item/1000329119629_i1_500.jpg")
# st.write("## 3.바닐라라떼 (HOT) 264잔 ")
# st.image("http://thumbnail.10x10.co.kr/webimage/image/basic600/352/B003520613.jpg?cmd=thumb&w=400&h=400&fit=true&ws=false")

# st.write("# WORST")

# st.write("## 1.그린티라떼 (HOT) 28잔 ")
# st.image("https://t1.daumcdn.net/cfile/tistory/266ACC4A56C679952B")
# st.write("## 2.그린티라떼 (ICE) 36잔 ")
# st.image("https://imagecdn.dpon.gift/images/merchandises/ediya%EB%85%B9%EC%B0%A8%EB%9D%BC%EB%96%BCICE.jpg")
# st.write("## 3.카페모카 (ICE) 38잔 ")
# st.image("http://image.auction.co.kr/itemimage/19/a7/48/19a748d726.jpg")

def main() :

    cof = ['CHOICE','자메이카블루마운틴','루왁커피','인헤르토커피','게이샤커피','블랙아이보리커피']
    choice = st.selectbox('상식퀴즈 : 세상에서 제일 비싼 커피는 무엇일까요?', cof)

    if choice == cof[1] :
        st.write("# 틀렸습니다.")
    elif choice == cof[2] :
        st.write("# 틀렸습니다.")
    elif choice == cof[3] :
        st.write("# 틀렸습니다.")
    elif choice == cof[4] :
        st.write("# 틀렸습니다.")
    elif choice == cof[5] :
        st.balloons()
        st.write("# 정답입니다!!!")
        st.write("""
        세계에서 가장 비싼 커피로 알려진 블랙 아이보리 커피는 바로 한번쯤은 들어보셨을 코끼리 똥 커피입니다.
        커피 생산 방식은 루왁이랑 비슷합니다. 차이점은 고양이 대신 코끼리가 만든다는 점 입니다.
        잔당 5만원 가량 한다고 합니다.
        """)

           


if __name__ == "__main__" :
    main()

  
#st.write(two)