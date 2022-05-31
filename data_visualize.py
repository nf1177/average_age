import altair as alt
import streamlit as st
from vega_datasets import data
import pandas as pd


# データの読みこみ
data = pd.read_csv("data.csv")

# ---- スライドバー ----
st.sidebar.write("""## 表示年度選択""")
s_year = st.sidebar.slider(
    '範囲を指定してください。',
    2020, 2021, (2021)
)


it_type = st.sidebar.selectbox(
    '試験を選択してください。',
    list(data["it_type"].unique().tolist())
)
# data = data[data["year"].isin(int(s_year))]
data = data[data["year"] == s_year]
data = data[data["it_type"] == it_type]

plot = alt.Chart(data).mark_circle(size=3000).encode(
    x=alt.X('level', scale=alt.Scale(domain=[0, 8])),
    y=alt.Y('受講平均年齢', scale=alt.Scale(domain=[20, 50])),
    color='kubun',
    tooltip=['受講平均年齢', '合格後のおすすめ試験']
)

text = plot.mark_text(
    align='center',
    baseline='middle',
    size=20,
).encode(
    text='shiken_name',
    color=alt.value('#eee')
)
st.markdown('みんなで試験を受講しよう')
st.altair_chart((plot+text).properties(
    width=1000,
    height=800,
    title="各試験の受講年齢")
    .configure_axis(
    grid=False
).configure_view(
    strokeOpacity=0)
    .interactive(), use_container_width=False)
