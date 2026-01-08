import streamlit as st
st.sidebar.title("Std info")
b=st.sidebar.selectbox("Select Batch",["B1","B2","B3","B4"])
ge=st.sidebar.radio("Select Gender",["Male","Female"])
x=st.sidebar.selectbox("Select Subject",["FSD","Python"])
tab1,tab2=st.tab("Python","FSD")
if tab1==x[0]:
    if x=="Python":
        st.write("Welcome to Python")
        name=st.sidebar.text_input("Enter your Name: ")
        en=st.sidebar.number_input("Enter your enrollement number: ")
        project_title=st.sidebar.text_input("ENter title:")
        project_desc=st.sidebar.text_area("Enter description")
else:
        st.write("welcome to FSD")
        name=st.sidebar.text_input("Enter your Name: ")
        en=st.sidebar.number_input("Enter your enrollement number: ")
        project_title=st.sidebar.text_input("ENter title:")
        project_desc=st.sidebar.text_area("Enter description")
btn=st.sidebar.button("Submit")
if btn==True:
    st.write(name)
    st.write(en)
    st.write(b)
    st.write(ge)
    st.write(x)
    st.write(project_title)
    st.write(project_desc)

st.markdown("",unsafe_allow_html=True)
