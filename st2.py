import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from quiz import app
from ocr import *
from quiz import *
import pytube
import whisper
from ytPlus import *
from gptKaam import *

st.set_page_config(page_title="Learn Anything", page_icon=":books:", layout="wide")

model = whisper.load_model("base")

load_dotenv() # Load secrets
print(os.getenv("OPENAI_API_KEY"))
reader = Reader(is_cuda=is_available())
gpt_3 = GPT_3(os.getenv('OPENAI_API_KEY'))

def display_text(bounds):
    text = []
    for x in bounds:
        t = x[1]
        text.append(t)
    text = ' '.join(text)
    return text 


st.title("Learn Anything")

# st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

st.caption("select video to get info about a youtube URL and Image for accessing your assignments and notes. Text is the default for basic info gathering!")

st.write("🌟 Welcome to my Streamlit WebPage! 🌟")
st.write("Choose from the following options:")
st.write("✨ Select a video to get information about a YouTube URL 🎥")
st.write("📝 Access an image to view your assignments and notes")
st.write("💬 Default text for basic information gathering")

input_type = st.selectbox("Select Type of Input", ["Text", "Image", "Video URL"])
# search_op = st.text_input("Enter what you want to learn today")
# user_input = image_file.name

if input_type == "Text":
    user_input = st.text_area("Enter Text Here")
elif input_type == "Image":
    
    image_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    # user_input = image_file.name
    if image_file is not None:
        image = Image.open(image_file)
        user_input = image_file.name
        st.image(image, caption="Uploaded Image", use_column_width=True)
else:
    user_input = st.text_input("Enter Video URL here")

if st.button("Search"):
    if input_type == "Text":
        st.write("You searched for:", user_input)
        results = gpt_3.teach(user_input)
        # inp_val = results
        # results = ["Result 1", "Result 2", "Result 3"]
        st.write("Here are your search results:")
        st.write(results)

        # code to get response for user_input from backend API
    elif input_type == "Image":

        st.write("You uploaded:", user_input)

        with st.spinner('Extracting Text from given Image'):
            eng_reader = easyocr.Reader(['en'])
            detected_text = eng_reader.readtext(image)
            st.subheader('Extracted text is ...')
            text = display_text(detected_text)
            
            st.write(text.lower())
            # st.write(text)
            results = gpt_3.teach(text)
            
            # inp_val = results
            # results = ["Result 1", "Result 2", "Result 3"]

            st.write("Here are your search results:")
            st.write(results)


        # code to get response for user_input from backend API
    else:
        st.write("You entered Video URL:", user_input)

        with st.spinner('Processing the given url'):
            audio_bytes , valuable = urlToText(user_input)

        option = st.selectbox(
        'What task is to be performed on the video?', options = ['Transcript', 'Summarize', 'Translate'])

        st.write('You selected:', option)

        number = st.slider("Summary length in words", 0, 300)

        # if number > 1:
        #     # with st.spinner('Processing the given url'):
                
        #     #     # audio_bytes , valuable = urlToText(user_input)
                
        #         results = gpt_3.summarize(valuable, number)
        #         st.write()
        #         st.write("audio file of the video: ")
        #         st.audio(audio_bytes)
        #         st.download_button("download audio", audio_bytes)
        #         st.write("Here is the summary of the video :")
        #         st.write(results)



        # code to get response for user_input from backend API

    if st.button("Learn More"):
        st.write("Additional resources to learn more about", user_input)
        # code to get additional resources for user_input from backend API
    
    if st.button("Quiz Me"):
        quiz_questions = [
            {
                "question": "Question 1",
                "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                "correct_answer": "Option 1"
            },
            {
                "question": "Question 2",
                "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                "correct_answer": "Option 2"
            },
            {
                "question": "Question 3",
                "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                "correct_answer": "Option 3"
            },
            {
                "question": "Question 4",
                "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                "correct_answer": "Option 4"
            },
            {
                "question": "Question 5",
                "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                "correct_answer": "Option 1"
            },
        ]
        score = app(quiz_questions)
        st.write(f"Your score is {score}/5")

