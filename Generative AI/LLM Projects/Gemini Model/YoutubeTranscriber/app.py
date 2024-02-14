import streamlit as st
from dotenv import load_dotenv

load_dotenv() ## load all env variables

import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

prompt = """
You are a Youtube video Sumarizer who summarises youtube videos in crisp points. You will be taking transcript text and summarizing
the entire video and provide the key takeaways and conclusion in structured format from the video in points within 200 words. The transcript text will
be appended here :
"""

# summarizing yt video by giving text transcripts to gemini model
def get_gemini_content(text_transcript, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt+text_transcript)
    return response.text

# getting text transcripts from youtube video
def get_transcript_of_yt_video(video_url):
    # get video id from the url : https://www.youtube.com/watch?v=csG_qfOTvxw 
    # video id of this url is "csG_qfOTvxw"
    try:
        video_id = video_url.split("=")[1] #splilts url into list of 2 elements
        text_transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        
        # returns list of text transcript. we will append elements from the list.
        video_transcript = ""
        for i in text_transcript_list:
            video_transcript += " "+i["text"]

        return video_transcript
    except Exception as e:
        raise e
    
st.title("Clip Insight")
st.subheader("Unlock the Power of Brevity: Your YouTube Videos, Summarized!")

youtube_url = st.text_input("Youtube link goes here ...")

if youtube_url:
    video_id = youtube_url.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True) # for displaying thumbnail of the yt video

if st.button("Summarize video"):
    video_transcript = get_transcript_of_yt_video(youtube_url)

    if video_transcript:
        summary_response = get_gemini_content(video_transcript, prompt)
        st.subheader("Video Summary :")
        st.markdown(summary_response)