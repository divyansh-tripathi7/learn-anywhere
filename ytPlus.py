import pytube, whisper, openai, streamlit
import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from quiz import app
from ocr import *
from quiz import *
import pytube
import whisper
# import whisper_timestamped
from gptKaam import *

def urlToText(url):
    data = pytube.YouTube(url)
    audioF = data.streams.get_audio_only()
    name = audioF.download()
            
    model = whisper.load_model("base")

    # timeStamps = model.
    audio_file = open(name, 'rb')
    audio_bytes = audio_file.read()
    text = model.transcribe(name)
    valuable = text['text']

    return audio_bytes, valuable 

#  this gives us transcript 

def getSummary(valuable):
    summary = gpt_3.summarize(valuable)
    return summary

def translate(lang , valuable):
    print("hello")
    translated = gpt_3.translate(valuable, lang)
    return translated

def ytBasic():
    st.write("✨ Select a video to get information about a YouTube URL 🎥")
    user_input = st.text_input("Enter Video URL here")
    return user_input



