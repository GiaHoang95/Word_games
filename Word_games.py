import streamlit as st

from PIL import Image

image = Image.open('211125_SANOFI_LOGO_RGB.png')

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
  st.image(image)

tabs_font_css = """
<style>

div[class*="stTextInput"] label p {
  font-size: 1rem;
  color: black;
}

[data-testid="column"] {
    width: calc((100/15)%-1rem) !important;
    flex: 1 1 calc((100/15)%-1rem) !important;
    min-width: calc((100/15)%-1rem) !important;
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
    max-width: 1000px;
    position: relative;
}

div[class*="st-emotion-cache-5rimss e1nzilvr5"] {
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

div[class*="st-emotion-cache-1cwt8z2 e1f1d6gn1"] {
    height: 40px;
    min-width: auto;
}

div[class*="st-emotion-cache-1r6slb0 e1f1d6gn1"] {
    min-width: auto;
}

</style>
"""

st.write(tabs_font_css, unsafe_allow_html=True)

def header_stt(url):
    st.markdown(f'<div style="width:100%;height:40px;display:flex;justify-content:center;align-items:center;font-size:20px;border-radius:0%;">{url}</div>', unsafe_allow_html=True)

def header_space(url):
    st.markdown(f'<div style="opacity:0;width:100%;height:18px;display:flex;justify-content:center;align-items:center;background-color:#ffffff;color:#33ff33;border: 0px solid #ffffff;border-radius:0%;">{url}</div>', unsafe_allow_html=True)
  
def header(url):
    st.markdown(f'<div style="width:100%;height:40px;display:flex;justify-content:center;align-items:center;background-color:#767AD3;color:#ffffff;border: 0px solid #ffffff;font-size:20px;border-radius:0%;">{url}</div>', unsafe_allow_html=True)

def header0(url):
    st.markdown(f'<div style="opacity:0;width:100%;height:40px;display:flex;justify-content:center;align-items:center;background-color:#C2C4EC;color:#33ff33;border: 0px solid #ffffff;font-size:20px;border-radius:0%;">{url}</div>', unsafe_allow_html=True)

def headerkm(url):
    st.markdown(f'<div style="width:100%;height:40px;display:flex;justify-content:center;align-items:center;background-color:#7A01E6;color:#ffffff;border: 0px solid #ffffff;font-size:20px;border-radius:0%;">{url}</div>', unsafe_allow_html=True)

def head(url):
    st.markdown(f'<div style="display:flex;justify-content:center;align-items:center;background-color:inherit;color:#7A01E6;font-weight:bold;font-size:50px;border-radius:0%;">{url}</div>', unsafe_allow_html=True)
  
def head_up(url):
    st.markdown(f'<div style="display:flex;justify-content:center;align-items:center;background-color:inherit;color:black;font-weight:bold;font-size:1rem;border-radius:0%;">{url}</div>', unsafe_allow_html=True)

def ex(ans, x):
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15 = st.columns(15)

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
        
    if x == 1:
        with col1:
            header_stt('1')
        with col2:
            header0('')
        with col3:
            header0('')
        with col4:
            header0('')
        with col5:
            header(ans.upper()[0])
        with col6:
            header(ans.upper()[1])
        with col7:
            header(ans.upper()[2])
        with col8:
            header(ans.upper()[3])
        with col9:
            headerkm(ans.upper()[4])
        with col10:
            header(ans.upper()[5])
        with col11:
            header(ans.upper()[6])
        with col12:
            header(ans.upper()[7])
        with col13:
            header0('')
        with col14:
            header0('')
        with col15:
            header0('')
        
    elif x == 2:
        with col1:
            header_stt('2')
        with col2:
            header0('')
        with col3:
            header0('')
        with col4:
            header(ans.upper()[0])
        with col5:
            header(ans.upper()[1])
        with col6:
            header(ans.upper()[2])
        with col7:
            header(ans.upper()[3])
        with col8:
            header(ans.upper()[4])
        with col9:
            headerkm(ans.upper()[5])
        with col10:
            header(ans.upper()[6])
        with col11:
            header(ans.upper()[7])
        with col12:
            header(ans.upper()[8])
        with col13:
            header(ans.upper()[9])
        with col14:
            header(ans.upper()[10])
        with col15:
            header(ans.upper()[11])
        
    elif x == 3:
        with col1:
            header_stt('3')
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
            header(ans.upper()[0])
        with col8:
            header(ans.upper()[1])
        with col9:
            headerkm(ans.upper()[2])
        with col10:
            header(ans.upper()[3])
        with col11:
            header(ans.upper()[4])
        with col12:
            header(ans.upper()[5])
        with col13:
            header0('')
        with col14:
            header0('')
        with col15:
            header0('')
        
    elif x == 4:
        with col1:
            header_stt('4')
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
            header(ans.upper()[0])
        with col8:
            header(ans.upper()[1])
        with col9:
            headerkm(ans.upper()[2])
        with col10:
            header(ans.upper()[3])
        with col11:
            header(ans.upper()[4])
        with col12:
            header(ans.upper()[5])
        with col13:
            header0('')
        with col14:
            header0('')
        with col15:
            header0('')
        
    elif x == 5:
        with col1:
            header_stt('5')
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
            headerkm(ans.upper()[0])
        with col10:
            header(ans.upper()[1])
        with col11:
            header(ans.upper()[2])
        with col12:
            header(ans.upper()[3])
        with col13:
            header(ans.upper()[4])
        with col14:
            header(ans.upper()[5])
        with col15:
            header(ans.upper()[6])
        
    elif x == 6:
        with col1:
            header_stt('6')
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
            header(ans.upper()[0])
        with col8:
            header(ans.upper()[1])
        with col9:
            headerkm(ans.upper()[2])
        with col10:
            header(ans.upper()[3])
        with col11:
            header0('')
        with col12:
            header0('')
        with col13:
            header0('')
        with col14:
            header0('')
        with col15:
            header0('')
        
    elif x == 7:
        with col1:
            header_stt('7')
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
            headerkm(ans.upper()[0])
        with col10:
            header(ans.upper()[1])
        with col11:
            header(ans.upper()[2])
        with col12:
            header0('')
        with col13:
            header0('')
        with col14:
            header0('')
        with col15:
            header0('')
        
    elif x == 8:
        with col1:
            header_stt('8')
        with col2:
            header0('')
        with col3:
            header0('')
        with col4:
            header0('')
        with col5:
            header0('')
        with col6:
            header(ans.upper()[0])
        with col7:
            header(ans.upper()[1])
        with col8:
            header(ans.upper()[2])
        with col9:
            headerkm(ans.upper()[3])
        with col10:
            header(ans.upper()[4])
        with col11:
            header(ans.upper()[5])
        with col12:
            header0('')
        with col13:
            header0('')
        with col14:
            header0('')
        with col15:
            header0('')
        
    elif x == 9:
        with col1:
            header_stt('9')
        with col2:
            header(ans.upper()[0])
        with col3:
            header(ans.upper()[1])
        with col4:
            header(ans.upper()[2])
        with col5:
            header(ans.upper()[3])
        with col6:
            header(ans.upper()[4])
        with col7:
            header(ans.upper()[5])
        with col8:
            header(ans.upper()[6])
        with col9:
            headerkm(ans.upper()[7])
        with col10:
            header(ans.upper()[8])
        with col11:
            header(ans.upper()[9])
        with col12:
            header(ans.upper()[10])
        with col13:
            header(ans.upper()[11])
        with col14:
            header(ans.upper()[12])
        with col15:
            header0('')
        
    elif x == 10:
        with col1:
            header_stt('10')
        with col2:
            header0('')
        with col3:
            header(ans.upper()[0])
        with col4:
            header(ans.upper()[1])
        with col5:
            header(ans.upper()[2])
        with col6:
            header(ans.upper()[3])
        with col7:
            header(ans.upper()[4])
        with col8:
            header(ans.upper()[5])
        with col9:
            headerkm(ans.upper()[6])
        with col10:
            header(ans.upper()[7])
        with col11:
            header0('')
        with col12:
            header0('')
        with col13:
            header0('')
        with col14:
            header0('')
        with col15:
            header0('')
        
    elif x == 11:
        with col1:
            header_stt('11')
        with col2:
            header0('')
        with col3:
            header0('')
        with col4:
            header0('')
        with col5:
            header(ans.upper()[0])
        with col6:
            header(ans.upper()[1])
        with col7:
            header(ans.upper()[2])
        with col8:
            header(ans.upper()[3])
        with col9:
            headerkm(ans.upper()[4])
        with col10:
            header(ans.upper()[5])
        with col11:
            header(ans.upper()[6])
        with col12:
            header(ans.upper()[7])
        with col13:
            header0('')
        with col14:
            header0('')
        with col15:
            header0('')
        
    elif x == 12:
        with col1:
            header_stt('12')
        with col2:
            header0('')
        with col3:
            header0('')
        with col4:
            header0('')
        with col5:
            header(ans.upper()[0])
        with col6:
            header(ans.upper()[1])
        with col7:
            header(ans.upper()[2])
        with col8:
            header(ans.upper()[3])
        with col9:
            headerkm(ans.upper()[4])
        with col10:
            header(ans.upper()[5])
        with col11:
            header0('')
        with col12:
            header0('')
        with col13:
            header0('')
        with col14:
            header0('')
        with col15:
            header0('')
        
    elif x == 13:
        with col1:
            header_stt('13')
        with col2:
            header0('')
        with col3:
            header0('')
        with col4:
            header0('')
        with col5:
            header0('')
        with col6:
            header(ans.upper()[0])
        with col7:
            header(ans.upper()[1])
        with col8:
            header(ans.upper()[2])
        with col9:
            headerkm(ans.upper()[3])
        with col10:
            header(ans.upper()[4])
        with col11:
            header0('')
        with col12:
            header0('')
        with col13:
            header0('')
        with col14:
            header0('')
        with col15:
            header0('')
        
    elif x == 14:
        with col1:
            header_stt('14')
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
            header(ans.upper()[0])
        with col8:
            header(ans.upper()[1])
        with col9:
            headerkm(ans.upper()[2])
        with col10:
            header(ans.upper()[3])
        with col11:
            header(ans.upper()[4])
        with col12:
            header(ans.upper()[5])
        with col13:
            header(ans.upper()[6])
        with col14:
            header0('')
        with col15:
            header0('')

col4, col5, col6 = st.columns([1, 1, 1])

col7, col8, col9 = st.columns([1, 1, 1])

with col5:
  head('ESSENTIAL')
  
with col8:
  head('MEDICINES')

ex('', 0)

ans1 = st.text_input('1\. Kiến nào không bao giờ ngủ?')
ans2 = st.text_input('2\. Chuỗi chương trình giáo dục cho bệnh nhân rất thành công mà SNF phối hợp thực hiện cùng BV ĐHYD TP.HCM?')
ans3 = st.text_input('3\. Cùng với Lovenox, đây là brand có thắng lợi lớn trong project Đàm phán giá trong năm 2023?')    
ans4 = st.text_input('4\. Con gì mà không có xương sống mà vẫn đứng được?')
ans5 = st.text_input('5\. Một trong 4 "Play to Win behavior" mang hàm ý chấp nhận thử thách mới?')    
ans6 = st.text_input('6\. Thức uống nào mà có chứa cả canxi và sắt?')
ans7 = st.text_input('7\. We are ... Sanofi')
ans8 = st.text_input('8\. Hình ảnh "Dòng thác" là hình ảnh quen thuộc của brand nào của EM?')
ans9 = st.text_input('9\. Resort tổ chức chương trình BU meeting của Essential Medicines tháng 10.23?')
ans10 = st.text_input('10\. Con trai có gì quý nhất?')    
ans11 = st.text_input('11\. Đồng gì mà đa số ai cũng thích?')
ans12 = st.text_input('12\. Trong chanh chứa chủ yếu Acid nào?')    
ans13 = st.text_input('13\. Trong truyện cổ tích Lọ Lem, con vật nào được biến thành ngựa kéo cỗ xe đưa Lọ Lem đến dự tiệc?')
ans14 = st.text_input('14\. Bông gì không mọc từ cây?')    

ex('', 0)

if len(ans1) != 8:
    ex('        ', 1)
else:
    ex(ans1, 1)

if len(ans2) != 12:
    ex('            ', 2)
else:
    ex(ans2, 2)

if len(ans3) != 6:
    ex('      ', 3)
else:
    ex(ans3, 3)

if len(ans4) != 6:
    ex('      ', 4)
else:
    ex(ans4, 4)

if len(ans5) != 7:
    ex('       ', 5)
else:
    ex(ans5, 5)

if len(ans6) != 4:
    ex('    ', 6)
else:
    ex(ans6, 6)

if len(ans7) != 3:
    ex('   ', 7)
else:
    ex(ans7, 7)

if len(ans8) != 6:
    ex('      ', 8)
else:
    ex(ans8, 8)

if len(ans9) != 13:
    ex('             ', 9)
else:
    ex(ans9, 9)

if len(ans10) != 8:
    ex('        ', 10)
else:
    ex(ans10, 10)

if len(ans11) != 8:
    ex('        ', 11)
else:
    ex(ans11, 11)

if len(ans12) != 6:
    ex('      ', 12)
else:
    ex(ans12, 12)

if len(ans13) != 5:
    ex('     ', 13)
else:
    ex(ans13, 13)

if len(ans14) != 7:
    ex('       ', 14)
else:
    ex(ans14, 14)

ex('', 0)

submit_form = """
<form action="https://formsubmit.co/giahoangduy@gmail.com" method="POST" enctype="multipart/form-data">
    <input type="text" placeholder="Key message" name="Key message" style="width: 100%;padding: 12px;border: 1px solid #ccc;border-radius: 6px; box-sizing: border-box;margin-top: 0px; margin-bottom: 16px;resize: vertical" required>
    <input type="text" placeholder="Team's name" name="District Manager's name" style="width: 100%;padding: 12px;border: 1px solid #cccccc;border-radius: 6px; box-sizing: border-box;margin-top: 6px; margin-bottom: 16px;resize: vertical" required>
    <input type="file" name="attachment" accept="image/png, image/jpeg" style="background-color: #ffffff;width: 100%;padding: 12px;border: 1px solid #cccccc;border-radius: 6px; box-sizing: border-box;margin-top: 6px; margin-bottom: 16px;resize: vertical">
    <button type="submit" style="background-color: #04AA6D;color: white;padding: 12px 20px;border: none;border-radius: 6px;cursor: pointer;">Send</button>
</form>
"""
st.markdown(submit_form, unsafe_allow_html=True)

ex('', 0)

head_up('Lưu ý: Upload ảnh chụp màn hình phần ô chữ bên trên')
