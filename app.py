wimport streamlit as st
import pandas as pd
import plotly.express as px

# Test dashboard without Firebase
st.title("🚀 WORKING Dashboard")
data = pd.DataFrame({
    "x": [1, 2, 3],
    "y": [4, 5, 6]
})
st.plotly_chart(px.line(data, x="x", y="y"))