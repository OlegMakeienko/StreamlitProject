import streamlit as st

#import Exploratory Data Analysis
import pandas as pd
import numpy as np

#
import plotly.express as px

def main():
    st.title("Plotly")
    df = pd.read_csv("./data/prog_languages_data.csv")
    #st.dataframe(df)

    figure_pie = px.pie(df, values="Sum", names="lang", title="Pie chart of Languages")
    st.plotly_chart(figure_pie)

    figure_bar = px.bar(df, x="lang", y="Sum", title="Bar Chart of Languages")
    st.plotly_chart(figure_bar)

if __name__ == "__main__":
    main()