# 安装 Streamlit 库
# 激活环境之后就是时候安装 streamlit 库了：
# pip install streamlit
from datetime import time, datetime

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.write('Hello, world!')

# 启动命令行终端
# 前往终端，敲入命令：
# streamlit run streamlit_app.py
# 然后应当弹出一个浏览器窗口，其中为你新创建的 Streamlit 应用。
# 恭喜你！ 你刚刚搭建了人生中第一个 Streamlit 应用！

# 应用的标题文字
st.header('st.button')

# 使用条件分支语句 if 和 else 来显示不同的消息
if st.button("Say hello"):  # st.button() 语句接收了一个值为 Say hello 的 label 参数，会作为显示在按钮上的文字
    st.write('Why hello there')  # st.write 命令被用作显示文字消息，取决于按钮是否按下，显示的要么是 Why hello there，要么是 Goodbye
else:
    st.write('Goodbye')

# st.write 能够在 Streamlit 应用中输出文字等内容。
# 除了能够输出文字，st.write() 命令还能够输出...
#
# 输出字符串，类似于 st.markdown()
# 输出 Python 的 dict 字典对象
# 输出 pandas DataFrame，将数据框显示为表格
# 输出用 matplotlib、plotly、altair、graphviz、bokeh 等库所作的图表
# https://docs.streamlit.io/library/api-reference/write-magic/st.write

# 应用的标题文字
st.header('st.write')

# st.write 的基本用法就是现实文字和使用 Markdown 语法的文本
st.write('Hello,*World!*:sunglasses:')

# st.write 还能够输出其他数据类型，比如数字
st.write(1234)

# 数据框也能够通过如下语句显示
df = pd.DataFrame({'first column': [1, 2, 3, 4], 'second column': [10, 20, 30, 40]})
st.write(df)

# 也能传入多个参数
st.write('Below is DataFrame:', df, 'Above is a dataframe.')

# 可以显示各种图表，只需传入图表对象即可
df2 = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

# 应用的标题文字
st.header('st.slider')

# 应用的子标题文字-基础滑条
st.subheader('Slider')

# st.slider() 命令被用作收集用户输入的年龄信息
# 第一个参数为 滑条 组件上方的标题文字，此处为询问用户年龄：'How old are you?'
# 三个整数 0, 130, 25 分别代表最小值、最大值和默认数值
age = st.slider('How old are you ?', 0, 130, 25)
st.write("I'm", age, 'years old')

# 范围滑条
st.subheader('Range slider')

values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# 时间范围滑条
st.subheader('Range time slider')

# 时间范围滑条允许同时输入一对下界与上界时间
appointment = st.slider("Schedule your appointment:", value=(time(11, 30), time(12, 45)))
st.write("You'r scheduled for:", appointment)

# 日期时间滑条
st.subheader('Datetime slider')

# 日期时间滑条允许输入一个日期时间。
# 第一个参数为 日期时间滑条 组件上方的标题文字，此处为询问开始时间：'When do you start?'。
# 这里日期时间的默认值通过 value 参数被设为 2020 年 1 月 1 日 9:30
start_time = st.slider("When do you start?", value=datetime(2020, 1, 1, 9, 30), format="MM/DD/YY-hh:mm")
st.write("Start time:", start_time)

# 探索与此相关的组件：
# st.select_slider https://docs.streamlit.io/library/api-reference/widgets/st.select_slider

# 折线图
st.header('Line chart')

# 用随机生成的数字新建一个三列的数据框
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
# st.line_chart() 创建一个折线图，以此前创建的数据框 chart_data 作为输入数据
st.line_chart(chart_data)

# st.selectbox 选择组件
st.header('st.selectbox')

# st.selectbox() 命令接收两个输入参数：
# 1.组件上方的标题文字，也就是这里的 'What is your favorite color?'
# 2.备选的数值，此处为 ('Blue', 'Red', 'Green')
option = st.selectbox('What is you favorite color?', ('Blue', 'Red', 'Green'))
st.write('Your favorite color is ', option)
