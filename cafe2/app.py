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

st.write(df['영업일자'])

first = df.iloc[:627]
second = df.iloc[627:1976]
third = df.iloc[1976:3518]
forth = df.iloc[3518:]

# fig = px.histogram(two, x="상품명")

total_sum1 = first['판매수량'].sum()
st.subheader(f"1분기 총 판매량 {total_sum1}잔 팔았습니다.")
total_sum2 = second['판매수량'].sum()
st.subheader(f"2분기 총 판매량 {total_sum2}잔 팔았습니다.")
total_sum3 = three['판매수량'].sum()
st.subheader(f"3분기 총 판매량 {total_sum3}잔 팔았습니다.")
total_sum4 = forth['판매수량'].sum()
st.subheader(f"4분기 총 판매량 {total_sum4}잔 팔았습니다.")


st.sidebar.header('Menu')
name = st.sidebar.selectbox('Name', ['종류를 선택해주세요','따뜻한커피','차가운커피'])

if name == '따뜻한커피':
    st.image("https://i.pinimg.com/736x/0c/84/ab/0c84ab632174745bd69862f24fd21cc7.jpg")

elif name == '차가운커피':
    st.image("https://w.namu.la/s/58397a721e13604b779350324ba029e64b8c2a645ccc40bfc2188d61af804072fa7a18f5de18688f75662a46571480912b989c1e9b317d78d885918f0d15c933e45739bfdd551c28f9c22e8a56f6e480f579a75d8f8bd85fe86cec99bdbb84c333c12612db37e41fd4bfb653d120e28d")


  

# two['ice'] = (
#     two.apply(lambda x: x. if r.age >= 20 else 'child', axis=1) # 행을 기준으로 가져옴
# )
# titanic.tail()

fig1 = px.histogram(two, x="상품명", y='판매수량',title='강원랜드 12월 한달 커피 판매량' )

st.plotly_chart(fig1)

st.write("# BEST")

st.write("## 1.아메리카노 (HOT) 1215잔 ")
st.image("https://imagescdn.gettyimagesbank.com/500/201708/jv10960341.jpg")
st.write("## 2.아메리카노 (ICE) 888잔 ")
st.image("https://sitem.ssgcdn.com/29/96/11/item/1000329119629_i1_500.jpg")
st.write("## 3.바닐라라떼 (HOT) 264잔 ")
st.image("http://thumbnail.10x10.co.kr/webimage/image/basic600/352/B003520613.jpg?cmd=thumb&w=400&h=400&fit=true&ws=false")

st.write("# WORST")

st.write("## 1.그린티라떼 (HOT) 28잔 ")
st.image("https://t1.daumcdn.net/cfile/tistory/266ACC4A56C679952B")
st.write("## 2.그린티라떼 (ICE) 36잔 ")
st.image("https://imagecdn.dpon.gift/images/merchandises/ediya%EB%85%B9%EC%B0%A8%EB%9D%BC%EB%96%BCICE.jpg")
st.write("## 3.카페모카 (ICE) 38잔 ")
st.image("http://image.auction.co.kr/itemimage/19/a7/48/19a748d726.jpg")

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