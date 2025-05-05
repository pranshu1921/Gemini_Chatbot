from dotenv import load_dotenv
load_dotenv() ## load all env variables from .env file

import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini pro model and get responses

model = genai.GenerativeModel("gemini-1.5-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

## initialize Streamlit app

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Application")
input = st.text_input("Input: ", key = "input")
submit = st.button("Submit")

## when submit is clicked

if submit:
    response = get_gemini_response(input)
    st.subheader("the Response is")
    st.write(response)
                          

    
    
    
    