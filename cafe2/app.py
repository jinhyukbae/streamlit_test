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
    강원랜드 인공지능 AI 빅데이터 기반 Data Analysis & Data Visualization Project
    """
    )

st.write('&nbsp;')
st.write('&nbsp;')
st.write('&nbsp;')
st.write('&nbsp;')
st.write('&nbsp;')


st.subheader("""
강원랜드_호텔 인공지능 무인카페 이용현황
""")

def main():
    df = pd.read_csv('./cafe2/data.csv', encoding='cp949')

    if st.button('데이터 보기'):
        st.dataframe(df)

if __name__ == '__main__' :
    main()


df = pd.read_csv('./cafe2/data.csv', encoding='cp949')


# a1 = df[df['상품명'].str.contains('아메리카노')] # 1
# a2 = df[df['상품명'].str.contains('카페라떼')] # 2
# a3 = df[df['상품명'].str.contains('초코라떼')] # 5
# a4 = df[df['상품명'].str.contains('흑당라떼')] # 8
# a5 = df[df['상품명'].str.contains('자몽')] # 6
# a6 = df[df['상품명'].str.contains('바닐라')] # 3
# a7 = df[df['상품명'].str.contains('아이스티')] # 9
# a8 = df[df['상품명'].str.contains('자두')] # 10
# a9 = df[df['상품명'].str.contains('청포도')] # 4
# a10 = df[df['상품명'].str.contains('카페모카')] # 7
# a11 = df[df['상품명'].str.contains('카푸치노')] # 11


# st.write(a1.sum())
# st.write(a2.sum())
# st.write(a3.sum())
# st.write(a4.sum())
# st.write(a5.sum())
# st.write(a6.sum())
# st.write(a7.sum())
# st.write(a8.sum())
# st.write(a9.sum())
# st.write(a10.sum())
# st.write(a11.sum())




def main() :

    cof = ['CHOICE','아메리카노','카페라떼','흑당라떼','초코라떼','스위티자몽','바닐라라떼','아이스티','자두주스','청포도주스','카페모카','카푸치노','그린티라떼']
    choice = st.selectbox('귀하가 선호하는 카페 음료는 무엇입니까?', cof)

    if choice == cof[1] :
        st.balloons()
        st.write("# 당신이 고른 음료는 첫번째로 많이 팔렸어요 ")
    elif choice == cof[2] :
        st.balloons()
        st.write("# 당신이 고른 음료는 두번째로 많이 팔렸어요")
    elif choice == cof[3] :
        st.snow()
        st.write("# 당신이 고른 음료는 여덟번째로 많이 팔렸어요.")
    elif choice == cof[4] :
        st.balloons()
        st.write("# 당신이 고른 음료는 다섯번째로 많이 팔렸어요.")
    elif choice == cof[5] :
        st.balloons()
        st.write("# 당신이 고른 음료는 여섯번째로 많이 팔렸어요.")
    elif choice == cof[6] :
        st.balloons()
        st.write("# 당신이 고른 음료는 세번째로 많이 팔렸어요.")
    elif choice == cof[7] :
        st.snow()
        st.write("# 당신이 고른 음료는 아홉번째로 많이 팔렸어요.")
    elif choice == cof[8] :
        st.snow()
        st.write("# 당신이 고른 음료는 열번째로 많이 팔렸어요.")
    elif choice == cof[9] :
        st.balloons()
        st.write("# 당신이 고른 음료는 네번째로 많이 팔렸어요.")  
    elif choice == cof[10] :
        st.snow()
        st.write("# 당신이 고른 음료는 일곱번째로 많이 팔렸어요.")
    elif choice == cof[11] :
        st.snow()
        st.write("# 당신이 고른 음료는 열한번째로 많이 팔렸어요.")
    elif choice == cof[-1] :
        st.snow()
        st.write("# 당신이 고른 음료는 열두번째로 많이 팔렸어요.")


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
        st.image("https://images.chosun.com/resizer/UWFdOvSfItpdtxI3bC5pdrK-5Xc=/544x393/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/FM2LW33USJAC7AENZB3WTXNYSA.JPG")

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
        st.image("data:image/jpeg;base64,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")





elif name == '2분기':

    total_sum2 = second['판매수량'].sum()
    st.subheader(f"2분기 총 판매량 {total_sum2}잔 팔았습니다.")

    fig_second = px.histogram(second, x="상품명", y='판매수량',title='강원랜드의 한 무인 카페의 2분기 음료 판매량' )

    st.plotly_chart(fig_second)

    sample2 = second[second['상품명'].str.contains('아메리카노')]

    st.write("## HOT vs ICE")
    st.write("### 2분기의 승자는 HOT 입니다.")
    fug2 = px.histogram(sample2, x="상품명", y='판매수량')
    st.plotly_chart(fug2)

    st.write("## BEST 3")
    col7, col8, col9 = st.columns(3)
    with col7:
        st.subheader("1.아메리카노 HOT 2020잔")
        st.image("data:image/jpeg;base64,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")

    with col8:
        st.subheader("2.아메리카노 ICE 1937잔")
        st.image("https://images.chosun.com/resizer/UWFdOvSfItpdtxI3bC5pdrK-5Xc=/544x393/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/FM2LW33USJAC7AENZB3WTXNYSA.JPG")
    with col9:
	    st.subheader("3.청포도주스 ICE 403잔")
	    st.image("https://www.the-cup.co.kr/data/editor/1902/thumb-687c8d0c78d329e0c637df3050b1fd20_1550129060_1108_920x843.jpg")
    
    st.write("## WORST 3")
    st.write("### 쓰다!! ")
    col10, col11, col12 = st.columns(3)
    with col10:
        st.subheader("1.그린티라떼 HOT 51잔")
        st.image("https://health.chosun.com/site/data/img_dir/2022/05/11/2022051101651_0.jpg")

    with col11:
        st.subheader("2.그린티라떼 ICE 57잔")
        st.image("data:image/jpeg;base64,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")

    with col12:
	    st.subheader("3.스위티자몽 HOT 63잔")
	    st.image("https://www.the-cup.co.kr/data/editor/1902/thumb-687c8d0c78d329e0c637df3050b1fd20_1550129060_1108_920x843.jpg")

elif name == '3분기':

    total_sum3 = third['판매수량'].sum()
    st.subheader(f"3분기 총 판매량 {total_sum3}잔 팔았습니다.") 
    
    fig_third = px.histogram(third, x="상품명", y='판매수량',title='강원랜드의 한 무인 카페의 3분기 음료 판매량' )

    st.plotly_chart(fig_third)

    sample3 = third[third['상품명'].str.contains('아메리카노')]

    st.write("## HOT vs ICE")
    st.write("### 3분기의 승자는 ICE 입니다.")
    st.write("### 여름이니까 아이스 커피~")
    fug3 = px.histogram(sample3, x="상품명", y='판매수량')
    st.plotly_chart(fug3)

    st.write("## BEST 3")
    col13, col14, col15 = st.columns(3)
    with col13:
        st.subheader("1.아메리카노 ICE 3433잔")
        st.image("https://images.chosun.com/resizer/UWFdOvSfItpdtxI3bC5pdrK-5Xc=/544x393/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/FM2LW33USJAC7AENZB3WTXNYSA.JPG")

    with col14:
        st.subheader("2.아메리카노 HOT 2290잔")
        st.image("data:image/jpeg;base64,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")

    with col15:
	    st.subheader("3.청포도주스 ICE 636잔")
	    st.image("https://www.the-cup.co.kr/data/editor/1902/thumb-687c8d0c78d329e0c637df3050b1fd20_1550129060_1108_920x843.jpg")
    
    st.write("## WORST 3")
    st.write("### 쓰다!! ")
    col16, col17, col18 = st.columns(3)
    with col16:
        st.subheader("1.그린티라떼 HOT 66잔")
        st.image("https://health.chosun.com/site/data/img_dir/2022/05/11/2022051101651_0.jpg")

    with col17:
        st.subheader("2.흑당라떼 HOT 104잔")
        st.image("https://t1.daumcdn.net/cfile/tistory/99F811365D172C5A01")
    with col18:
	    st.subheader("3.카푸치노 HOT 110잔")
	    st.image("https://www.the-cup.co.kr/data/editor/1902/thumb-687c8d0c78d329e0c637df3050b1fd20_1550129060_1108_920x843.jpg")
    
elif name == '4분기':

    total_sum4 = forth['판매수량'].sum()
    st.subheader(f"4분기 총 판매량 {total_sum4}잔 팔았습니다.")

    fig_forth = px.histogram(forth, x="상품명", y='판매수량',title='강원랜드의 한 무인 카페의 4분기 음료 판매량' )

    st.plotly_chart(fig_forth)  

    sample4 = forth[forth['상품명'].str.contains('아메리카노')]

    st.write("## HOT vs ICE")
    st.write("### 4분기의 승자는 HOT 입니다.")
    
    fug4 = px.histogram(sample4, x="상품명", y='판매수량')
    st.plotly_chart(fug4)

   

           


# if __name__ == "__main__" :
#     main()


    st.write("## BEST 3")
    col19, col20, col21 = st.columns(3)
    with col19:
        st.subheader("1.아메리카노 HOT 3772잔")
        st.image("https://health.chosun.com/site/data/img_dir/2022/05/11/2022051101651_0.jpg")

    with col20:
        st.subheader("2.아메리카노 ICE 3179잔")
        st.image("https://images.chosun.com/resizer/UWFdOvSfItpdtxI3bC5pdrK-5Xc=/544x393/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/FM2LW33USJAC7AENZB3WTXNYSA.JPG")

    with col21:
	    st.subheader("3.바닐라라떼 HOT 730잔")
	    st.image("https://www.the-cup.co.kr/data/editor/1902/thumb-687c8d0c78d329e0c637df3050b1fd20_1550129060_1108_920x843.jpg")
    
    st.write("## WORST 3")
    st.write("### 쓰다!! ")
    col22, col23, col24 = st.columns(3)
    with col22:
        st.subheader("1.그린티라떼 HOT 106잔")
        st.image("https://health.chosun.com/site/data/img_dir/2022/05/11/2022051101651_0.jpg")

    with col23:
        st.subheader("2.그린티라떼 ICE 106잔")
        st.image("data:image/jpeg;base64,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")

    with col24:
	    st.subheader("3.카페모카 ICE 139잔")
	    st.image("https://www.the-cup.co.kr/data/editor/1902/thumb-687c8d0c78d329e0c637df3050b1fd20_1550129060_1108_920x843.jpg")



elif name == '전체':
    total_sum5 = df['판매수량'].sum()
    st.subheader(f"21년 총 판매량 {total_sum5}잔 팔았습니다.")

    fig_all = px.histogram(df, x="상품명", y='판매수량',title='강원랜드의 한 무인 카페의 21년 총 음료 판매량' )

    st.plotly_chart(fig_all)




    
    
    





    sample5 = df[df['상품명'].str.contains('아메리카노')]

    st.write("## HOT vs ICE")
    st.write("### 21년의 승자는 ICE 입니다.")
    st.write("### 한국인은 아아의 민족 입니다.")


    fug5 = px.histogram(sample5, x="상품명", y='판매수량')
    st.plotly_chart(fug5)

    st.write("## BEST 3")
    col25, col26, col27 = st.columns(3)
    with col25:
        st.subheader("1.아메리카노 ICE 9302잔")
        st.image("https://images.chosun.com/resizer/UWFdOvSfItpdtxI3bC5pdrK-5Xc=/544x393/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/FM2LW33USJAC7AENZB3WTXNYSA.JPG")

    with col26:
        st.subheader("2.아메리카노 HOT 9077잔")
        st.image("data:image/jpeg;base64,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")

    with col27:
	    st.subheader("3.청포도주스 ICE 1886잔")
	    st.image("https://www.the-cup.co.kr/data/editor/1902/thumb-687c8d0c78d329e0c637df3050b1fd20_1550129060_1108_920x843.jpg")
    
    st.write("## WORST 3")
    st.write("### 쓰다!! ")
    col28, col29, col30 = st.columns(3)
    with col28:
        st.subheader("1.그린티라떼 HOT 246잔")
        st.image("https://health.chosun.com/site/data/img_dir/2022/05/11/2022051101651_0.jpg")

    with col29:
        st.subheader("2.그린티라떼 ICE 329잔")
        st.image("data:image/jpeg;base64,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")

    with col30:
	    st.subheader("3.흑당라떼 HOT 410잔")
        st.image("https://t1.daumcdn.net/cfile/tistory/99F811365D172C5A01")





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


   

           

#     if __name__ == "__main__" :
#         main()

  
#st.write(two)