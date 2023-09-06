import streamlit as st

tabs_font_css = """
<style>

div[class*="stTextInput"] label p {
  font-size: 10px;
  padding: 10px
  margin-boder: 0px;
}

[data-testid="column"] {
    width: calc(10% - 1rem) !important;
    flex: 1 1 calc(10% - 1rem) !important;
    min-width: calc(10% - 1rem) !important;
}

div[class*="stApp stAppEmbeddingID-s0kgnzez595f css-fg4pbf erw9t6i1] {
    background: #e5e5f7;
}

</style>
"""
st.write(tabs_font_css, unsafe_allow_html=True)
