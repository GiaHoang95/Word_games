import streamlit as st

tabs_font_css = """
<style>

div[class*="stTextInput"] label p {
  font-size: 1rem;
  color: black;
}

[data-testid="column"] {
    width: calc((100/16)% - 1rem) !important;
    flex: 1 1 calc((100/16)% - 1rem) !important;
    min-width: calc((100/16)% - 1rem) !important;
}

[data-testid="stAppViewContainer"] {
    background-color: #e5e5f7;
    opacity: 0.8;
    background-image:  radial-gradient(#444cf7 0.5px, transparent 0.5px), radial-gradient(#444cf7 0.5px, #e5e5f7 0.5px);
    background-size: 20px 20px;
    background-position: 0 0,10px 10px;
}

[data-testid="block-container"] {
    font-size: 16px;
    font-family: Helvetica, sans-serif;
    font-weight: 400;
    line-height: 1.6;
    text-size-adjust: 100%;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
    -webkit-font-smoothing: auto;
    color: rgb(49, 51, 63);
    box-sizing: border-box;
    width: 100%;
    padding: 3rem 1rem 10rem;
    max-width: 46rem;
    padding-left: 1rem;
    padding-right: 1rem;
    position: relative;
}

div[class*="css-5rimss e1nzilvr5"] {
    font-size: 16px;
    font-weight: 400;
    line-height: 1.6;
    text-size-adjust: 100%;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
    -webkit-font-smoothing: auto;
    color: rgb(49, 51, 63);
    box-sizing: border-box;
    font-family: "Source Sans Pro", sans-serif;
    margin-bottom: -1rem;
    display: flex;
    align-items: center;
    justify-content: center;
}

[data-testid="stVerticalBlock"] {
    gap: 1px;
}

[data-testid="stHorizontalBlock"] {
    gap: 1px;
}

div[class*="css-1k67eer e1f1d6gn1"] {
    height: 40px;
}

</style>
"""

st.write(tabs_font_css, unsafe_allow_html=True)

def header_stt(url):
    st.markdown(f'<div style="width:100%;height:40px;display:flex;justify-content:center;align-items:center;font-size:20px;border-radius:0%;">{url}</div>', unsafe_allow_html=True)

def header_space(url):
    st.markdown(f'<div style="opacity:0;width:100%;height:30px;display:flex;justify-content:center;align-items:center;background-color:#ffffff;color:#33ff33;border: 0px solid #ffffff;border-radius:0%;">{url}</div>', unsafe_allow_html=True)
  
def header(url):
    st.markdown(f'<div style="width:100%;height:40px;display:flex;justify-content:center;align-items:center;background-color:#C2C4EC;color:#ffffff;border: 0px solid #ffffff;font-size:20px;border-radius:0%;">{url}</div>', unsafe_allow_html=True)

def header0(url):
    st.markdown(f'<div style="opacity:0;width:100%;height:40px;display:flex;justify-content:center;align-items:center;background-color:#C2C4EC;color:#33ff33;border: 0px solid #ffffff;font-size:20px;border-radius:0%;">{url}</div>', unsafe_allow_html=True)

def headerkm(url):
    st.markdown(f'<div style="width:100%;height:40px;display:flex;justify-content:center;align-items:center;background-color:#3941E5;color:#ffffff;border: 0px solid #ffffff;font-size:20px;border-radius:0%;">{url}</div>', unsafe_allow_html=True)

def head(url):
    st.markdown(f'<div style="display:flex;justify-content:center;align-items:center;background-color:inherit;color:#7A01E6;font-weight:bold;font-size:40px;border-radius:0%;">{url}</div>', unsafe_allow_html=True)

def ex(ans, x):
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16 = st.columns(16)

    if x == 0:
        with col1:
            header_space('')
        with col2:
            header_space('')
        with col3:
            header_space('')
        with col4:
            header_space('')
        with col5:
            header_space('')
        with col6:
            header_space('')
        with col7:
            header_space('')
        with col8:
            header_space('')
        with col9:
            header_space('')
        with col10:
            header_space('')
        with col11:
            header_space('')
        with col12:
            header_space('')
        with col13:
            header_space('')
        with col14:
            header_space('')
        with col15:
            header_space('')
        with col16:
            header_space('')
          
    if x == 1:
        with col1:
            header_stt('1')
        with col2:
            header('')
        with col3:
            header('')
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
            header('')
        with col10:
            header('')
        with col11:
            header0('')
        with col12:
            header_space('')
        with col13:
            header_space('')
        with col14:
            header_space('')
        with col15:
            header_space('')
        with col16:
            header('')  
    elif x == 2:
        with col1:
            header_stt('2')
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
        with col11:
            header0('')
        with col12:
            header_space('')
        with col13:
            header_space('')
        with col14:
            header_space('')
        with col15:
            header_space('')
        with col16:
            header('')
    elif x == 3:
        with col1:
            header_stt('3')
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
        with col11:
            header0('')
        with col12:
            header_space('')
        with col13:
            header_space('')
        with col14:
            header_space('')
        with col15:
            header_space('')
        with col16:
            header('')

    elif x == 4:
        with col1:
            header_stt('4')
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
        with col11:
            header0('')
        with col12:
            header_space('')
        with col13:
            header_space('')
        with col14:
            header_space('')
        with col15:
            header_space('')
        with col16:
            header('')


head('Essential Medicines')

col1, col2 = st.columns([1, 1])
col3, col4 = st.columns([1, 1])

with col1:
    ans1 = st.text_input('Xin chào trong tiếng anh là gì?')
with col2:
    ans2 = st.text_input('Chúc mừng trong tiếng anh là gì?')
with col3: 
    ans3 = st.text_input('Kỳ diệu trong tiếng anh là gì?')    
with col4:
    ans4 = st.text_input('May mắn trong tiếng anh là gì?')
  
ex('', 0)

if len(ans1) < 5:
    ex('     ', 1)
else:
    ex(ans1, 1)

if len(ans2) < 8:
    ex('        ', 2)
else:
    ex(ans2, 2)

if len(ans3) < 10:
    ex('          ', 3)
else:
    ex(ans3, 3)

if len(ans4) < 5:
    ex('     ', 4)
else:
    ex(ans4, 4)
