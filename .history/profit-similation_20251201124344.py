import streamlit as st

st.write('''Markdown
  リスト１
  リスト２
  リスト３
''')

st.write('#折れ線グラフ')
a = [1, 5, 2, 4, 10]
st.line_chart(a)z