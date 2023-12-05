import streamlit as st
import base64

import sys
sys.path.insert(1, '')

import agent

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
st.set_page_config(
    page_icon="web/img/robot-1.1s-200px.png",
    layout="wide",
    page_title="React Agents Demo with Vertex AI (Google Cloud)",
    initial_sidebar_state="expanded",
)

st.markdown(
    f"<div class='header'><h3> React Agents Demo with Vertex AI</h3><h3>(Google Cloud) </h3></div>",
    unsafe_allow_html=True,
)
st.markdown(
    f'<div>Welcome to the ReAct! We are going to do a simple Google Search. You can use the following query: <b>What other movie has done the Director of Dune (2021)?</b></div>',
    unsafe_allow_html=True
)

query = st.text_input("Query to search")
verbose = False
temp = 0


generate = st.button("🤖Run Agent🤖")

if generate:
    with st.spinner("Agent running..."):
        result = agent.agent_start(query)
        st.success(result)
        st.balloons()

local_css("web/css/frontend.css")
remote_css("https://fonts.googleapis.com/icon?family=Material+Icons")
remote_css(
    "https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@300;400;500;600;700&display=swap"
)