import streamlit as st

tabs_font_css = """
<style>

div[class*="stTextInput"] label p {
  font-size: 1rem;
  color: black;
}

[data-testid="column"] {
    width: calc(10% - 1rem) !important;
    flex: 1 1 calc(10% - 1rem) !important;
    min-width: calc(10% - 1rem) !important;
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
  
</style>
"""

st.write(tabs_font_css, unsafe_allow_html=True)

def header_space(url):
    st.markdown(f'<div style="opacity:0;width:100%;height:0px;display:flex;justify-content:center;align-items:center;background-color:#ffffff;color:#33ff33;border:0px solid #ffffff;font-size:20px;border-radius:0%;">{url}</div>', unsafe_allow_html=True)
  
def header(url):
     st.markdown(f'<div style="width:100%;height:25px;display:flex;justify-content:center;align-items:center;background-color:#8A8FE8;color:#FFFFFF;border:0.5px solid #8A8FE8;font-size:20px;border-radius:0%;">{url}</div>', unsafe_allow_html=True)

def header0(url):
     st.markdown(f'<div style="opacity:0;width:100%;height:25px;display:flex;justify-content:center;align-items:center;background-color:#ffffff;color:#FFFFFF;border:0px solid #ffffff;font-size:20px;border-radius:0%;">{url}</div>', unsafe_allow_html=True)

def headerkm(url):
     st.markdown(f'<div style="width:100%;height:25px;display:flex;justify-content:center;align-items:center;background-color:#0F19D5;color:#FFFFFF;border:0.5px solid #0F19D5;font-size:20px;border-radius:0%;">{url}</div>', unsafe_allow_html=True)
  
def head(url):
    st.markdown(f'<div style="display:flex;justify-content:center;align-items:center;background-color:inherit;color:#7A01E6;font-weight:bold;font-size:40px;border-radius:0%;">{url}</div>', unsafe_allow_html=True)

def ex(ans, x):
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10, gap="small")

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
