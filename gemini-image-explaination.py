import os
import streamlit as st
import google.generativeai as genai
from PIL import Image
from config import GOOGLE_API_KEY

os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

vision_model = genai.GenerativeModel('gemini-pro-vision')

def get_image_explanation(image):
    response = vision_model.generate_content(["Explain the picture?", image])
    if hasattr(response, 'content'):
        return response.content
    elif hasattr(response, 'text'):
        return response.text
    else:
        return "No explanation found."

st.title("Image Explanation App")
st.write("Upload an image to get an explanation of what's happening in the picture.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    

    st.image(image, caption="Uploaded Image", use_column_width=True)
    

    with st.spinner("Generating explanation..."):
        explanation = get_image_explanation(image)

    st.write("Explanation:")
    st.write(explanation)
