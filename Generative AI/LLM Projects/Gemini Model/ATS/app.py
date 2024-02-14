from dotenv import load_dotenv

load_dotenv()

import streamlit as st 
import os
from PIL import Image
import io
import base64

import pdf2image 
import google.generativeai as genai 


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response =  model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # convert pdf to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        first_page = images[0]

        # convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type" : "image/jpeg",
                "data" : base64.b64encode(img_byte_arr).decode() # encode to base 64
            }
        ]
        return pdf_parts
    else:
        FileNotFoundError("Np file Uploaded")


# Streamlit App
st.set_page_config(page_title="ATS Resume Scanner")
st.header("ATS Tracker")
input_text = st.text_area("Job description: ", key ="input")
uploaded_file = st.file_uploader("Upload your resume(PDF)..", type = ["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Succesfully")

submit1 = st.button("Tell me about the resume")
# submit2 = st.button("How can I improve ?")
submit3 = st.button("Match percentage")

input_prompt1 = """
You are an experienced HR with Technical Experience in the field of Full Stack Development, Data Science, Web Development, Big data Engineering,
Data Analyst, Devops. Your task is review the provided resume against the job description for these profiles.
Please share your professional evaluation on whether the candidate's profile aligns with the job description.
Highlight the strengths and weaknesses of the applicant in relation to the specified job description.
"""

input_prompt3 = """
You are askilled ATS(Application Tracking System) scanner with deep understanding of Full Stack Development, Data Science, Web Development, Big data Engineering,
Data Analyst, Devops and deep ATS functionality.
Your task is to evaluate the resume against the job description. Give me the percentage of match if the resume matches the job description.
first the output should come as perentage and then keywords missing and last final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The response is  ")
        st.write(response)
    else:
        st.write("Please Upload file")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The response is  ")
        st.write(response)
    else:
        st.write("Please Upload file")