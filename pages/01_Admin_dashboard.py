from tkinter import Y, OptionMenu
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import glob
import streamlit as st
import os
from PIL import Image
import numpy as np
import pickle
from sklearn.neighbors import NearestNeighbors
from numpy.linalg import norm
import requests
from streamlit_lottie import st_lottie





def main():

    st.set_page_config(layout="wide", initial_sidebar_state='expanded')
    st.image("images/logo-recom2.png", width=100)
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
   


    hide_menu = """
    <style>
    #MainMenu {
    visibility:hidden;
    }

    footer{
        visibility:visible;
    }
    footer:after {
        content: 'Recom © 2022  - Doris BAILLARD';
        display: block;
        position: relative;
        color:blue;

    }
    </style>
    """
    
    def load_lottie(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()



    hello = st.columns(6)
    with hello[2]:
        lottie_robot= load_lottie("https://assets3.lottiefiles.com/packages/lf20_3vbOcw.json")
        st_lottie(lottie_robot, height=100, key="robot")

    hello[1].markdown("<p style='color:darkblue;font-size:160%'>Welcome Admin !</p>",unsafe_allow_html=True)
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.markdown("<p style='color:#3498db;font-size:120%'>Key Metrics</p>",unsafe_allow_html=True)


    kpi= st.columns(3)
    kpi[0].metric("Weekly Visits", "35642","+45%")
    kpi[1].metric("Sales - 7 days", "5970", "+70%")
    kpi[2].metric("Conversions -7 days", "9538","+35%")

    st.markdown("<hr/>", unsafe_allow_html=True)

    ### second row 

    st.markdown("<p style='color:#3498db;font-size:120%'>Secondary Metrics</p>",unsafe_allow_html=True)

    first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.columns(6)


    with first_kpi:
        st.markdown("**First KPI**")
        number1 = 413486 
        st.markdown(f"<p style='color:#3498db;font-size:120%'>{number1}</p>", unsafe_allow_html=True)

    with second_kpi:
        st.markdown("**Second KPI**")
        number2 = 254869 
        st.markdown(f"<p style='color:#3498db;font-size:120%'>{number2}</p>", unsafe_allow_html=True)

    with third_kpi:
        st.markdown("**Third KPI**")
        number3 = 33657 
        st.markdown(f"<p style='color:#3498db;font-size:120%'>{number3}</p>", unsafe_allow_html=True)

    with fourth_kpi:
        st.markdown("**Fourth KPI**")
        number1 = 53478 
        st.markdown(f"<p style='color:#3498db;font-size:120%'>{number1}</p>", unsafe_allow_html=True)

    with fifth_kpi:
        st.markdown("**Fifth KPI**")
        number2 = 18690
        st.markdown(f"<p style='color:#3498db;font-size:120%'>{number2}</p>", unsafe_allow_html=True)

    with sixth_kpi:
        st.markdown("**Sixth KPI**")
        number3 = 333.597
        st.markdown(f"<p style='color:#3498db;font-size:120%'>{number3}</p>", unsafe_allow_html=True)

    st.markdown("<hr/>", unsafe_allow_html=True)


    st.markdown("<p style='color:#3498db;font-size:120%'>Important charts</p>",unsafe_allow_html=True)
    chart_data = pd.DataFrame(
        np.random.randn(14,3),
        columns = ['a','b','c'])

    charts = st.columns((2,0.3,2))
    charts[0].markdown("chart 1 ")
    charts[0].bar_chart(chart_data)
   

    df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
    
    df2 = pd.DataFrame(
     np.random.randn(450, 3),
     columns=['a', 'b', 'c'])
    charts[0].markdown("chart 3 ")
    charts[0].vega_lite_chart(df, {
        'mark': {'type': 'circle', 'tooltip': True},
        'encoding': {
            'x': {'field': 'a', 'type': 'quantitative'},
            'y': {'field': 'b', 'type': 'quantitative'},
            'size': {'field': 'c', 'type': 'quantitative'},
            'color': {'field': 'c', 'type': 'quantitative'},
        },
    })
    charts[2].markdown("chart 2 ")
    charts[2].vega_lite_chart(df2, {
        'mark': {'type': 'circle', 'tooltip': True},
        'encoding': {
            'x': {'field': 'a', 'type': 'quantitative'},
            'y': {'field': 'b', 'type': 'quantitative'},
            'size': {'field': 'c', 'type': 'quantitative'},
            'color': {'field': 'c', 'type': 'quantitative'},
        },
    })
    charts[2].markdown("chart 4 ")
    charts[2].line_chart(chart_data)




    st.markdown(hide_menu, unsafe_allow_html=True)

       
  
if __name__ == '__main__':
    main()