import streamlit as st

st.set_page_config(page_title="Olegs page",
                   page_icon=" :) ",
                   layout="wide",
                   initial_sidebar_state="auto ")

def main():
    st.title("Page Settings")
    st.sidebar.success("Menu")

if __name__ == "__main__":
    main()