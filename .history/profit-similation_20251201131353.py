import streamlit as st
import math
import pandas as pd
import altair as alt

pre_cost = 2000*1.0E+4
fix_cost = 1000*1.0E+4
cost = pre_cost + fix_cost

def calc_earning(pre_cost):
    earning = 2.87E+07 * math.log(pre_cost) - 4.44E+08
    return int(earning)

def calc_profit(earning, cost):
  profit = earning - cost
  return int(profit)

earning = calc_earning(pre_cost)
profit = calc_profit(earning, cost)
profit_ratio = int(profit / cost * 100)

data_ad_cost = list(range(1000,9001))
data_earning = [calc_earning(ad_cost*1.0E+4) for ad_cost in data_ad_cost]
data_profit = [calc_profit(earning, ad_cost*1.0e+4 + fix_cost) for earning, ad_cost in zip(data_earning, data_ad_cost)]

# plt.plot(data_ad_cost, data_earning, color='blue')
# plt.plot(data_ad_cost, data_profit, color='green')
# plt.show()

max_profit = max(data_profit)
best_ad_cost = data_ad_cost[data_profit.index(max_profit)] * 1.0E+4

st.title("WEBアプリ開発")

st.write('こちらは通常のテキストだよ!')

# st.write('''Markdown
#   -リスト１
#   -リスト２
#   -リスト３
# ''')

st.write('#折れ線グラフ')
a = [1, 5, 2, 4, 10]
st.line_chart(a)

st.sidebar.write("## 入力フォーム")

ad_cost = st.sidebar.slider('広告費（万円）', 1000, 9000)*1.0E+04
fix_cost = 1000*1.0E+4
cost = ad_cost + fix_cost

st.write(f'広告宣伝費: {ad_cost}')

st.title('利益予想シミュレーション')


col1, col2, col3 = st.columns(3)
col1.metric('費用', f'{int(cost/1.0E+4)}万円')
col1.metric('最適な広告投下費用', f'{best_ad_cost} 万円')
col2.metric('予想売上', f'{int(earning/1.0E+04)} 万円')
col3.metric('予想利益', f'{int(profit/1.0E+04)} 万円', f'{profit_ratio} %')
col3.metric('予想最大利益', f'{int(max_profit/1.0E+04)} 万円')


df_earning = pd.DataFrame()
df_earning['ad_cost'] = data_ad_cost
df_earning['value'] = data