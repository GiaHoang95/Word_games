import streamlit as st
import os

lst = [0, 0, 0, 0]
co_ans1 = 'HELLO'
co_ans2 = 'CONGRATS'
co_ans3 = 'FANTASTICS'
co_ans4 = 'LUCKY'

ans1 = st.text_input('Nhập đáp án của hàng 1')
ans2 = st.text_input('Nhập đáp án của hàng 2')    
ans3 = st.text_input('Nhập đáp án của hàng 3')    
ans4 = st.text_input('Nhập đáp án của hàng 4')

if ans1.upper() == co_ans1:
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.image("/Users/hdg1995/Desktop/Picture1.png")
    with col3:
        st.write("")
else:
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.image("/Users/hdg1995/Desktop/Picture1_blank.png")
    with col3:
        st.write("")
if ans2.upper() == co_ans2:
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.image("/Users/hdg1995/Desktop/Picture2.png")
    with col3:
        st.write("")
else:
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.image("/Users/hdg1995/Desktop/Picture2_blank.png")
    with col3:
        st.write("")

if ans3.upper() == co_ans3:
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.image("/Users/hdg1995/Desktop/Picture3.png")
    with col3:
        st.write("")
else:
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.image("/Users/hdg1995/Desktop/Picture3_blank.png")
    with col3:
        st.write("")

if ans4.upper() == co_ans4:
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.image("/Users/hdg1995/Desktop/Picture4.png")
    with col3:
        st.write("")
else:
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.image("/Users/hdg1995/Desktop/Picture4_blank.png")
    with col3:
        st.write("")
