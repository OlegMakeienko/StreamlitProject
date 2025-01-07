#Core Pkgs
import streamlit as st

city = "London"
name_one = "Oleg"
name_two = "Arja"

#Displaying Text
st.text("Hello, my name is {}".format(name_one))
st.text("And I live in {} :)".format(city))

#Header
st.header(city)

#Displaying colored text/bootstraps alert

st.success(name_one)
st.info(name_two)

#Help

st.write(dir(st))
st.help(str)
