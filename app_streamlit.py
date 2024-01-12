import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd


st.header('Dashboard - Amazon EC2 ')

x = np.arange(0,1000,1)
y = np.random.normal(loc = 10, scale = 2, size = 1000)


dic = {'x' : x,
       'y' : y}


df = pd.DataFrame.from_dict(dic)
 

fig = px.line(x = df['x'], y = df['y'])


st.plotly_chart(fig)