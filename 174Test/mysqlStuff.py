from asyncore import write
from textwrap import wrap
import streamlit as st
import mysql.connector

# Initialize connection.
# Uses st.experimental_singleton to only run once.
st.write("hello")
