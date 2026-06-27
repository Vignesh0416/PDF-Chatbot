import streamlit as st
import sys

st.write(sys.version)

try:
    import langchain_community
    st.success("langchain-community installed")
except Exception as e:
    st.error(e)