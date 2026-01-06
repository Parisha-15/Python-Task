import streamlit as st
import numpy as np
from numpy import random
st.sidebar.title("Std info")
name=st.sidebar.text_input("Enter your Name: ")
st.write(name)
btn=st.button("random no:")
if btn:
    s=random.randint(100)
    st.write(s)
    if s>50:
        bt1=st.button("generate img")
        st.image(r"c:\Users\LJENG\Desktop\Parisha_T4_FSD\T4_Lec-4\a.jpg")
    else:
        st.audio("a.mp3")