import streamlit as st
import pandas as pd
import numpy as np

st.title("Titulo Deisy")
num=st.slider("num", 0, 100, step=1)
st.write("el numero ingresado es {}".format(num))
