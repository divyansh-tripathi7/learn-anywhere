import whisper
# importing required modules
from PyPDF2 import PdfReader
from transformers import pipeline
from gptKaam import *
from gtts import gTTS
from io import BytesIO

import requests
# download the model in library 

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

#  can modify to get detail by page 
load_dotenv()
gpt_3 = GPT_3(os.getenv('OPENAI_API_KEY'))

total_content = ""

def getText(file_path , total_content):
    reader = PdfReader(file_path)
    # print(reader.numPages)
    val = len(reader.pages)
    for i in range(val):
        page = reader._get_page(i)
        page_content = page.extract_text()
        total_content += page_content

    return val , total_content



val , text = getText("know-india-booklet.pdf" , "")

print(val)
print(len(text))

summary = summarizer(text) # when we get transformer model
# summary = gpt_3.summarize2(text) ## gpt ki abhi itni aukat nhi hai

# print(summary)

# assume summary h tab kya karoge

def sumToAudio(summary):
    audio = gTTS(summary)
    af = BytesIO()
    audio.write_to_fp(af)
    return af




# text is very long for gpt sum
# mary gotta use library