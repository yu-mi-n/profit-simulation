import streamlit as st
import math
import pandas as pd
import altair as alt

fix_cost = int(1000*1.0E+4)
ad_cost = st.sidebar.slider('広告費（万円）', 1000, 9000)*1.0E+04
cost = ad_cost + fix_cost

def calc_earning(ad_cost):
    earning = 2.87E+07 * math.log(ad_cost) - 4.44E+08
    return int(earning)

def calc_profit(earning, cost):
  profit = earning - cost
  return int(profit)

earning = calc_earning(ad_cost)
profit = calc_profit(earning, cost)
profit_ratio = int(profit / cost * 100)

data_ad_cost = list(range(1000,9001, 1))
data_earning = [calc_earning(ad_cost*1.0E+4) for ad_cost in data_ad_cost]
data_profit = [calc_profit(earning, ad_cost*1.0e+4 + fix_cost) for earning, ad_cost in zip(data_earning, data_ad_cost)]

# plt.plot(data_ad_cost, data_earning, color='blue')
# plt.plot(data_ad_cost, data_profit, color='green')
# plt.show()

max_profit = max(data_profit)
best_ad_cost = data_ad_cost[data_profit.index(max_profit)]

# st.title("WEBアプリ開発")

# st.write('こちらは通常のテキストだよ!')

# st.write('''Markdown
#   -リスト１
#   -リスト２
#   -リスト３
# ''')

# st.write('#折れ線グラフ')
# a = [1, 5, 2, 4, 10]
# st.line_chart(a)

st.title("予想収益趣シミュレーション")
st.sidebar.write("## 入力フォーム")

cost_col1, cost_col2 = st.columns([2,3])
with cost_col1:
  st.write(f'広告宣伝費: {"{:,}".format(int(ad_cost))}円')
with cost_col2:
  st.write(f'その他の固定費：{"{:,}".format(fix_cost)}円')

col1, col2, col3 = st.columns(3)
col1.metric('費用', f'{"{:,}".format(int(cost/1.0E+4))}万円', height='stretch')
col1.metric('最適な広告投下費用', f'{"{:,}".format(int(best_ad_cost))} 万円')
col2.metric('予想売上', f'{"{:,}".format(int(earning/1.0E+04))} 万円')
col3.metric('予想利益', f'{"{:,}".format(int(profit/1.0E+04))} 万円', f'{profit_ratio} %', height='stretch')
col3.metric('予想最大利益', f'{"{:,}".format(int(max_profit/1.0E+04))} 万円')


df_earning = pd.DataFrame()
df_earning['ad_cost'] = data_ad_cost
df_earning['value'] = data_earning
df_earning['indicator'] = '売上'

df_profit = pd.DataFrame()
df_profit['ad_cost'] = data_ad_cost
df_profit['value'] = data_profit
df_profit['indicator'] = '利益'

df = pd.concat([df_earning, df_profit])
df['value'] = df['value'] / 1.0E+4

xmax = int(ad_cost / 1.0E+4)
df_view = df[df["ad_cost"] <= xmax]

chart = alt.Chart(df_view).mark_line().encode(
alt.X('ad_cost', title='広告宣伝費 (万円)'),
alt.Y('value', title='売上 & 利益 (万円)'),
color='indicator'
).configure_axis(
labelFontSize=12,
titleFontSize=16,
).configure_legend(
titleFontSize=12,
labelFontSize=16,)

st.write('## 広告宣伝費に応じた予測売上・利益の推移')
st.altair_chart(chart, use_container_width=True)

st.warning("*本サイトはあくまでシミュレーションです")