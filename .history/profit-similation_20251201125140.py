import streamlit as st

st.title("webアプリ開発")

st.write('こちらは通常のテキストだよ!')

st.write('''Markdown
  リスト１
  リスト２
  リスト３
''')

st.write('#折れ線グラフ')
a = [1, 5, 2, 4, 10]
st.line_chart(a)

st.sidebar.write("## 入力フォーム")

st.sidebar.slider('広告費')