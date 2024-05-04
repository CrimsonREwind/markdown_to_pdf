import streamlit as st
import markdown
from xhtml2pdf import pisa
import io

stitle = st.sidebar.title("Markdown to PDF")
size_exp = st.sidebar.expander("Text Size", expanded=False)
name_exp = st.sidebar.expander("File Name", expanded=True)
with size_exp:
    size = st.text_input("Text Size", value="15", label_visibility="hidden", key="size")
with name_exp:
    name = st.text_input("File Name", value="markdown", label_visibility="hidden", key="file_name")

markdown_text = st.text_area('Enter your Markdown Text Here', height=700, label_visibility="hidden", key="markdown_text")

generate_btn = st.button('Generate PDF')
if generate_btn:
    html = markdown.markdown(markdown_text)
    html = '<style>body { font-size: 'f'{size}''px; }</style>' + html
    pdf = io.BytesIO()
    pisa.CreatePDF(io.StringIO(html), pdf)
    pdf.seek(0)
    st.sidebar.download_button("Download Markdown File", pdf, f'{name}.pdf')
