import streamlit as st
import math
ad_cost = 2000*1.0E+4
fix_cost = 1000*1.0E+4
cost = ad_cost + fix_cost
def calc_earnings(ad_cost):
  earnings = 2.87E+07 * math.log(ad_cost) - 4.44E+08
return int(earnings)
def calc_profit(earnings, cost):
profit = earnings - cost
return int(profit)
earnings = calc_earnings(ad_cost)
profit = calc_profit(earnings, cost)
profit_ratio = int(profit / earnings * 100)
data_ad_cost = list(range(1000, 9001, 1))
data_earnings = [calc_earnings(ad_cost*1.0E+04) for ad_cost in data_ad_cost]
data_profit = [calc_profit(earnings, ad_cost*1.0E+04 + fix_cost) for
earnings, ad_cost in zip(data_earnings, data_ad_cost)]
max_profit = max(data_profit)
best_ad_cost = data_ad_cost[data_profit.index(max_profit)]

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


col1, col2, col3 = st.columns
col1.metric('費用', f'int(cost/1.0E+4)万円')
col1.metric('最適な広告投下費用', f'{best_ad_cost} 万円')
col2.metric('予想売上', f'{int(earnings/1.0E+04)} 万円')
col3.metric('予想利益', f'{int(profit/1.0E+04)} 万円', f'{profit_ratio} %')
col3.metric('予想最大利益', f'{int(max_profit/1.0E+04)} 万円')