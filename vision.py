from dotenv import load_dotenv
load_dotenv() ## load all env variables from .env file

import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini pro model and get responses

model = genai.GenerativeModel("gemini-1.5-pro")
def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

## initialize Streamlit app

st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")
input = st.text_input("Input prompt: ", key = "input")

uploaded_file = st.file_uploader("choose an image...", type = ["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Uploaded Image.", use_column_width = True)
    
submit = st.button("Tell me something about this image")

## if submit is clicked
if submit:
    response = get_gemini_response(input, image)
    st.subheader("The response is")
    st.write(response)
    st.write("**This is a demo of Gemini Image model. You can upload an image and ask the model to describe it or answer questions about it.")
    st.write("**The model can also generate images based on the input prompt. You can try it out by entering a prompt and clicking the button.")
    st.write("**Note: The model may take some time to respond depending on the complexity of the image and the input prompt.")
