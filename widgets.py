import streamlit as st

name = st.text_input("Enter you name", max_chars=10, type='password')
text = "Hello, {}!".format(name)

if st.button("Submit", key="text"):
    st.write(text)

if st.button("Submit", key="name"):
    st.write("Hej då, {}".format(name))

if st.checkbox("Show/Hide", key="checkbox"):
    st.write(text)

kids = ["Arja", "Mark", "Ragnhild", "Katja"]
choice = st.selectbox("Children", kids)
my_children = st.multiselect("my_children", kids)