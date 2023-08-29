import streamlit as st

tabs_font_css = """
<style>

div[class*="stTextInput"] label p {
  font-size: 30px;
}

</style>
"""

st.write(tabs_font_css, unsafe_allow_html=True)

def header(url):
     st.markdown(f'<div style="width:40px;height:40px;display:flex;justify-content:center;align-items:center;background-color:#ffffff;color:#33ff33;border:solid #ff0000;font-size:24px;border-radius:0%;">{url}</div>', unsafe_allow_html=True)

def header0(url):
     st.markdown(f'<div style="width:40px;height:40px;display:flex;justify-content:center;align-items:center;background-color:#ffffff;color:#33ff33;border:solid #ffffff;font-size:24px;border-radius:0%;">{url}</div>', unsafe_allow_html=True)

def headerkm(url):
     st.markdown(f'<div style="width:40px;height:40px;display:flex;justify-content:center;align-items:center;background-color:#008000;color:#33ff33;border:solid #ff0000;font-size:24px;border-radius:0%;">{url}</div>', unsafe_allow_html=True)

def ex(ans, x):
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

    if x == 0:
        with col1:
            header0('')
        with col2:
            header0('')
        with col3:
            header0('')
        with col4:
            header0('')
        with col5:
            header0('')
        with col6:
            header0('')
        with col7:
            header0('')
        with col8:
            header0('')
        with col9:
            header0('')
        with col10:
            header0('')

    if x == 1:
        with col1:
            header0('')
        with col2:
            header0('')
        with col3:
            header0('')
        with col4:
            header(ans.upper()[0])
        with col5:
            header(ans.upper()[1])
        with col6:
            headerkm(ans.upper()[2])
        with col7:
            header(ans.upper()[3])
        with col8:
            header(ans.upper()[4])
        with col9:
            header0('')
        with col10:
            header0('')
    
    elif x == 2:
        with col1:
            header0('')
        with col2:
            header(ans.upper()[0])
        with col3:
            header(ans.upper()[1])
        with col4:
            header(ans.upper()[2])
        with col5:
            header(ans.upper()[3])
        with col6:
            headerkm(ans.upper()[4])
        with col7:
            header(ans.upper()[5])
        with col8:
            header(ans.upper()[6])
        with col9:
            header(ans.upper()[7])
        with col10:
            header0('')

    elif x == 3:
        with col1:
            header(ans.upper()[0])
        with col2:
            header(ans.upper()[1])
        with col3:
            header(ans.upper()[2])
        with col4:
            header(ans.upper()[3])
        with col5:
            header(ans.upper()[4])
        with col6:
            headerkm(ans.upper()[5])
        with col7:
            header(ans.upper()[6])
        with col8:
            header(ans.upper()[7])
        with col9:
            header(ans.upper()[8])
        with col10:
            header(ans.upper()[9])

    elif x == 4:
        with col1:
            header0('')
        with col2:
            header0('')
        with col3:
            header(ans.upper()[0])
        with col4:
            header(ans.upper()[1])
        with col5:
            header(ans.upper()[2])
        with col6:
            headerkm(ans.upper()[3])
        with col7:
            header(ans.upper()[4])
        with col8:
            header0('')
        with col9:
            header0('')
        with col10:
            header0('')

ans1 = st.text_input('Xin chào trong tiếng anh là gì? (hello)')
ans2 = st.text_input('Chúc mừng trong tiếng anh là gì? (congrats)')    
ans3 = st.text_input('Kỳ diệu trong tiếng anh là gì? (fantastics)')    
ans4 = st.text_input('May mắn trong tiếng anh là gì? (lucky)')

if len(ans1) < 5:
    ex('     ', 1)
else:
    ex(ans1, 1)

ex('           ', 0)

if len(ans2) < 8:
    ex('        ', 2)
else:
    ex(ans2, 2)

ex('           ', 0)

if len(ans3) < 10:
    ex('          ', 3)
else:
    ex(ans3, 3)

ex('           ', 0)

if len(ans4) < 5:
    ex('     ', 4)
else:
    ex(ans4, 4)
