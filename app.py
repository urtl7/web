import streamlit as st

#from src.summary import summarize
#from src.bert2 import get_summary
#from src.mbart import predictions
from src.bert3 import predictions


if __name__ == '__main__':

    st.header("Text Summarization using BERT")
    st.subheader("This app will summarize the long piece of input text in a few sentences")

    st.subheader("Paste your long text below:")
    text = st.text_area(label="Input text")
    if st.button("Summarize"):
        if text:
            summary_result = predictions(text)
            st.success(summary_result)
            

        else:
            st.error("Please paste or write(!) some text")


