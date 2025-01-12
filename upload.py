import docx2txt
import streamlit as st
import pandas as pd
from PIL import Image
import pdfplumber


def handle_file_upload(file_label, file_types):
    uploaded_file = st.file_uploader(f"Upload a {file_label}", type=file_types)
    if uploaded_file is not None:
        file_details = {
            "file_name": uploaded_file.name,
            "file_type": uploaded_file.type,
            "file_size": uploaded_file.size
        }
        st.write(file_details)
    return uploaded_file

@st.cache_data
def load_image(image_file):
        return Image.open(image_file)

def main():
    st.title("File Upload Tutorial")

    menu = ["Home", "Dataset", "Document File", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        image_file = handle_file_upload("image", ["jpg", "jpeg", "png"])
        if st.button("Show image"):
            st.image(load_image(image_file), width=500)

    elif choice == "Dataset":
        st.subheader("Dataset")
        data = handle_file_upload("csv", ["csv"])
        if st.button("Show table"):
            df = pd.read_csv(data)
            st.dataframe(df)

    elif choice == "Document File":
        st.subheader("Document File")
        document = handle_file_upload("document", ["txt", "pdf", "docx"])
        if st.button("Process"):
            if document.type == "text/plain":
                #Read as byte
                st.text(str(document.read(), encoding="utf-8"))

            elif document.type == "application/pdf":
                try:
                    with pdfplumber.open(document) as pdf:
                        pages = pdf.pages[0]
                        st.write(pages.extract_text())
                except:
                    st.write("Could not extract text.")
            else:
                st.write(docx2txt.process(document))


    else:
        st.subheader("About")

if __name__ == "__main__":
    main()
