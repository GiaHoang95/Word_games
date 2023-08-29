import streamlit as st
import os
from PIL import Image

lst = [0, 0, 0, 0]
co_ans1 = 'HELLO'
co_ans2 = 'CONGRATS'
co_ans3 = 'FANTASTICS'
co_ans4 = 'LUCKY'

image1 = Image.open('Word_games/blob/main/Picture1.png')
image1_blank = Image.open('./Word_games/Picture1_blank.png')
image2 = Image.open('./Word_games/Picture2.png')
image2_blank = Image.open('./Word_games/Picture2_blank.png')
image3 = Image.open('./Word_games/Picture3.png')
image3_blank = Image.open('./Word_games/Picture3_blank.png')
image4 = Image.open('./Word_games/Picture4.png')
image4_blank = Image.open('./Word_games/Picture4_blank.png')

ans1 = st.text_input('Nhập đáp án của hàng 1')
ans2 = st.text_input('Nhập đáp án của hàng 2')    
ans3 = st.text_input('Nhập đáp án của hàng 3')    
ans4 = st.text_input('Nhập đáp án của hàng 4')

if ans1.upper() == co_ans1:
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.image(image1)
    with col3:
        st.write("")
else:
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.image(image1_blank)
    with col3:
        st.write("")
if ans2.upper() == co_ans2:
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.image(image2)
    with col3:
        st.write("")
else:
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.image(image2_blank)
    with col3:
        st.write("")

if ans3.upper() == co_ans3:
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.image(image3)
    with col3:
        st.write("")
else:
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.image(image3_blank)
    with col3:
        st.write("")

if ans4.upper() == co_ans4:
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.image(image4)
    with col3:
        st.write("")
else:
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.image(image4_blank)
    with col3:
        st.write("")
