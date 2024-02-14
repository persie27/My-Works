import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt):
    model = genai.GenerativeModel('gemini-pro') # I am converting pdf to text , so using gemini-pro instead of vision
    response = model.generate_content(input_prompt)
    return response.text

def pdf_to_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

input_prompt = """
Act like you are an experienced ATS(Application tracking System) with deep understanding of Technical fields like Data Science,
Software Engineering, Data Engineering. Your task is to evaluate the resume based on job description.
Considering the job market being very competitive, you must provide best assistance for improving the resume. 
Assign the matching percentage with job description and the key words missing with high accuracy 
jd :{jd}
resume:{text}

I want the response in the following format
{{"JD is matching":"%" , "Missing Keywords": "[]", "Profile summary" : ""}}
"""

st.title("ATS using GenAI")
st.text("Improve your Resume")
jd = st.text_area("Job description goes here...")
uploaded_file = st.file_uploader("Upload your resume", type="pdf")

submit = st.button("Track Resume")

if submit:
    if uploaded_file is not None:
        text = pdf_to_text(uploaded_file)
        response = get_gemini_response(input_prompt)
        st.markdown(response)