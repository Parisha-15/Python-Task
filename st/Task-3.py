import streamlit as st
st.header("This is Task-3")
x=st.file_uploader("Upload Photo",type=["pdf"])
# if st.button("Upload File"):
#     st.image(x)
st.success("s")
st.warning('w')
st.info("i")
st.error("e")
if st.button("submit"):
    x=st.progress(0)
    with st.spinner("loading..."):
        for i in range(100):
            import time
            time.sleep(0.1)
            x.progress(i+1)
    st.success("Submitted sucessfully")

import pandas as pd
data={"name":["A","B","C"],"age":[1,2,3]}
df=pd.DataFrame(data)
st.header('DataFrame')
st.dataframe(df)

st.header("Table")
st.table(data)
import matplotlib.pyplot as plt
x=["A","B","C","D"]
y=[20,10,15,25]
plt.bar(x,y,width=0.4)
st.pyplot(plt)
plt.clf()
plt.scatter(x,y)
st.pyplot(plt)
import numpy as np
a=np.arange(1,11)
b=np.random.randint(1,100,10)
z=np.column_stack((a,b))
st.line_chart(z)
st.bar_chart(z)
st.markdown("*Std*")
st.markdown("**Std**")
st.markdown("~~Std~~")
