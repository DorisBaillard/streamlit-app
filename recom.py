#imports

import streamlit as st
import pandas as pd
from PIL import Image
import pickle
from pathlib import Path
import requests
from streamlit_lottie import st_lottie






def main():
    st.set_page_config(layout="wide")
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    
    hide_menu = """
    <style>
    #MainMenu {
    visibility:visible;
    }

    footer{
        visibility:visible;
    }
    footer:after {
        content: 'Recom © 2022 - Doris BAILLARD';
        display: block;
        position: relative;
        color:blue;

    }
    </style>
    """

    hide_sidebar = """
    <style>
    .css-163ttbj {
    visibility:hidden;
    }

    </style>
    """

    st.markdown(hide_menu, unsafe_allow_html=True)
    st.markdown(hide_sidebar, unsafe_allow_html=True)


    def load_lottie(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie = load_lottie("https://assets2.lottiefiles.com/private_files/lf30_zSGy1w.json")
    st.image("images/logo-recom2.png")
    cols = st.columns((2,3))
    with cols[1]:

        st_lottie(lottie, height=400, key="coding")
    with cols[0]:
        st.markdown("<p style='font-size:160%'>Hello :)</p>", unsafe_allow_html=True)
        login = st.text_input("Username: ", 'admin')
        password = st.text_input("Password: ", "recom_demo")
        st.markdown('<a href="/Admin_dashboard" target="_self">LOGIN</a>', unsafe_allow_html=True)




if __name__ == '__main__':
    main()

