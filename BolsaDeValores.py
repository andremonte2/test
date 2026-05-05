import yfinance as yf
import pandas as pd
import streamlit as st
from datetime import datetime

st.header("Analisando empresas")
ticker = st.text_input("Ticker Code")

data = yf.Ticker(ticker)

data_news = pd.DataFrame(data.news)
data_news2 = data_news["content"]
#st.dataframe("content")

st.subheader(f"Ultimas noticias da {ticker}:")

for i in range (len(data.news)):

    title = data.news[i]["content"]["title"]
    url = data.news[i]["content"]["canonicalUrl"]["url"]
    print(f"Titulo: {title}  /// Url: {url}")
    st.markdown(f"Titulo: {title}")
    st.markdown(f"Link: {url}")
    st.markdown("-----------------------------------------------------")



data_hist = data.history(period= "max", start = "2019-03-16", interval = "5d")
data_hist = data_hist.reset_index()
ey = st.selectbox("Eixo y: ", data_hist.columns)
ex = st.selectbox("Eixo x: ", data_hist.columns)


st.subheader(f"Gráfico de {ey} x {ex}:")

st.line_chart(data_hist, x = ex, y = ey)

print(data_hist)
