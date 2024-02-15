import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 데이터 로드
# 전국 65세 이상 인구 수 및 비율
df1 = pd.read_csv("./Nationwide_population.csv")
# 전국 경로당 수
df2 = pd.read_csv("./Nationwide_welfare.csv")
# 대전 65세 이상 인구 수 및 비율
df3 = pd.read_csv("./Daejeon_population.csv")
# 대전 경로당 수
df4 = pd.read_csv("./Daejeon_welfare.csv")

df1 = df1.astype('float')
df2 = df2.astype('float')
df3 = df3.astype('float')
df4 = df4.astype('float')

# 전국 노인 인구 비율 증가율
df5 = df1.copy()
base = df5.iloc[1][0].copy()
for i in range(1, 10):
    df5.iloc[1][i] = round((df5.iloc[1][i] - base) / base * 100, 2)
df5.iloc[1][0] = 0

# 대전 노인 인구 비율 증가율
df6 = df3.copy()
base = df6.iloc[1][0].copy()
# print(base)
for i in range(1, 10):
    # print(base, end=" ")
    # print(df6.iloc[1][i])
    df6.iloc[1][i] = round((df6.iloc[1][i] - base) / base * 100, 2)
df6.iloc[1][0] = 0

# 전국 경로당 증가율
df7 = df2.copy()
base = df7.iloc[1][0].copy()
for i in range(1, 10):
    df7.iloc[1][i] = round((df7.iloc[1][i] - base) / base * 100, 2)
df7.iloc[1][0] = 0


# 대전 경로당 증가율
df8 = df4.copy()
base = df8.iloc[1][0].copy()
for i in range(1, 10):
    df8.iloc[1][i] = round((df8.iloc[1][i] - base) / base * 100, 2)
df8.iloc[1][0] = 0


# 전국, 대전 경로당 1개 당 노인 수
df9 = df1.copy()
df10 = df1.copy()
for i in range(0, 10):
    df9.iloc[1][i] = round((df1.iloc[2][i] / df2.iloc[1][i]), 2)
    df10.iloc[1][i] = round((df3.iloc[2][i] / df4.iloc[1][i]), 2)

# MAIN
st.title('노인 인구 및 여가복지시설 현황 비교')

tab1, tab2, tab3 = st.tabs(["전국", "대전", "비교"])

with tab1:
    # 전국 65세 이상 인구 변화 시각화
    st.subheader('전국 노인 인구 추이')
    fig1 = px.line(x=df1.iloc[0], y=df1.iloc[1], title='전국 노인 인구 비율 변화', markers=True)
    fig1.update_traces(mode='lines+markers+text', text=df1.iloc[1], textposition='top center',line=dict(color='pink'))
    fig1.update_layout(
        xaxis_title='연도',
        yaxis_title='65세 이상 인구 비율(퍼센트)',
    )
    st.plotly_chart(fig1)
    # 전국 여가복지시설 현황 시각화
    st.subheader('전국 여가복지시설(경로당) 현황')
    fig2 = px.line(x=df2.iloc[0], y=df2.iloc[1], title='연도별 여가복지시설(경로당) 총계', markers=True)
    fig2.update_traces(mode='lines+markers+text', text=df2.iloc[1], textposition='top center',line=dict(color='purple'))
    fig2.update_layout(
        xaxis_title='연도',
        yaxis_title='전국 경로당 수'
    )
    st.plotly_chart(fig2)

    st.text("전국 노인 인구는 계속해서 증가하며, 이에따라 여가복지시설도 증가하는 추세를 보임.")

with tab2:
    # 대전 65세 이상 인구 변화 시각화
    st.subheader('대전 노인 인구 추이')
    fig3 = px.line(x=df3.iloc[0], y=df3.iloc[1], title='대전 노인 인구 비율 변화', markers=True)
    fig3.update_traces(mode='lines+markers+text', text=df3.iloc[1], textposition='top center',line=dict(color='aquamarine'))
    fig3.update_layout(
        xaxis_title='연도',
        yaxis_title='65세 이상 인구 비율(퍼센트)'
    )
    st.plotly_chart(fig3)

    # 대전 여가복지시설 현황 시각화
    st.subheader('대전 여가복지시설(경로당) 현황')
    fig4 = px.line(x=df4.iloc[0], y=df4.iloc[1], title='연도별 여가복지시설(경로당) 총계', markers=True)
    fig4.update_traces(mode='lines+markers+text', text=df4.iloc[1], textposition='top center')
    fig4.update_layout(
        xaxis_title='연도',
        yaxis_title='대전 경로당 수'
    )
    st.plotly_chart(fig4)
    st.text("대전 노인 인구 또한 계속해서 증가하며, 이에따라 여가복지시설도 증가하는 추세를 보임.")


with tab3:
    st.subheader('대전 노인 인구 증가비율 대비 경로당 수 증가 비율')
    fig5 = go.Figure()
    fig5.add_trace(go.Scatter(
        x = df5.iloc[0],
        y = df5.iloc[1],
        name='노인 인구 증가 비율',
        mode='lines+markers+text',
        text=df5.iloc[1],
        textposition='top center',
        line=dict(color='green')
    ))
    fig5.add_trace(go.Scatter(
        x = df7.iloc[0],
        y = df7.iloc[1],
        name='경로당 수 증가 비율',
        mode='lines+markers+text',
        text=df7.iloc[1],
        textposition='top center',
        line=dict(color='olive')
    ))
    fig5.update_layout(
        xaxis_title='연도',
        yaxis_title='비율',
        title='전국 노인 인구 증가비율 대비 경로당 수 증가 비율',
    )
    st.plotly_chart(fig5)


    fig6 = go.Figure()
    fig6.add_trace(go.Scatter(
        x = df6.iloc[0],
        y = df6.iloc[1],
        name='노인 인구 증가 비율',
        mode='lines+markers+text',
        text=df6.iloc[1],
        textposition='top center',
        line=dict(color='palevioletred')
    ))
    fig6.add_trace(go.Scatter(
        x = df8.iloc[0],
        y = df8.iloc[1],
        name='경로당 수 증가 비율',
        mode='lines+markers+text',
        text=df8.iloc[1],
        textposition='top center',
        line=dict(color='mistyrose')
    ))
    fig6.update_layout(
        xaxis_title='연도',
        yaxis_title='비율',
        title='대전 노인 인구 증가비율 대비 경로당 수 증가 비율',
    )
    st.plotly_chart(fig6)


    fig7 = go.Figure()
    fig7.add_trace(go.Scatter(
        x = df7.iloc[0],
        y = df7.iloc[1],
        name='전국 평균',
        mode='lines+markers+text',
        text=df7.iloc[1],
        textposition='top center',
        line=dict(color='yellowgreen')
    ))
    fig7.add_trace(go.Scatter(
        x = df8.iloc[0],
        y = df8.iloc[1],
        name='대전',
        mode='lines+markers+text',
        text=df8.iloc[1],
        textposition='top center',
        line=dict(color='lightgreen')
    ))

    fig7.update_layout(
        xaxis_title='연도',
        yaxis_title='비율',
        title='전국 평균과 대전의 경로당 수 증가 비율 비교',
    
    )
    st.plotly_chart(fig7)

    fig8 = go.Figure()
    fig8.add_trace(go.Scatter(
        x = df9.iloc[0],
        y = df9.iloc[1],
        name='전국 평균',
        mode='lines+markers+text',
        text=df9.iloc[1],
        textposition='top center',
        line=dict(color='violet')
        
    ))
    fig8.add_trace(go.Scatter(
        x = df10.iloc[0],
        y = df10.iloc[1],
        name='대전',
        mode='lines+markers+text',
        text=df10.iloc[1],
        textposition='top center',
        line=dict(color='darkviolet')
    ))

    fig8.update_layout(
        xaxis_title='연도',
        yaxis_title='비율',
        title='경로당 1개 당 65세 이상 노인 수',
    )
    st.plotly_chart(fig8)
    
    st.text("전국 평균에 비해 복지시설 수가 적으며, 노인 인구 증가량에 비해 복지시설 구축이 따라오지 못하고 있음.")
