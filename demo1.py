import streamlit as st
from ytPlus import * 
from gptKaam import * 
from bookBuddy import *
import pytube, whisper, openai

load_dotenv() # Load secrets
print(os.getenv("OPENAI_API_KEY"))
reader = Reader(is_cuda=is_available())
gpt_3 = GPT_3(os.getenv('OPENAI_API_KEY'))

# Set page title
st.set_page_config(page_title="My Studying Platform")

# Define the function for the Home page
def home():
    st.title("Welcome to My Platform")
    st.write("This is the Home page")

# Define the function for the Assignment Assist page
def assignment_assist():
    st.title("Assignment Assist")
    st.write("This is the Assignment Assist page")


# Define the function for the ytPlus page
# https://www.youtube.com/watch?v=8-GavXeFlEA
def ytplus():
    st.title("ytPlus")
    st.write("This is the ytPlus page")

    user_input = ytBasic()
    if st.button("Lets GOOO"):
        audio , text , option = perform_video_task(user_input)
        if option == 'Transcript':
                st.markdown(text)
                # result = transcript
        elif option == 'Summarize':
                summy = gpt_3.summarize(text)
                st.markdown(summy)
        elif option == 'Translate':
                st.write("translate kro bhai")


def perform_video_task(user_input):
    # if st.button("Let's start"):
        st.write("You searched for:", user_input)
        with st.spinner('Processing the given url'):
            # audio_bytes , valuable = urlToText(user_input)
            audio , trans = urlToText(user_input)
            st.success("processed")

            # Get user input for the task to perform on the video
            option = st.selectbox(
                'What task is to be performed on the video?',
                options = [ 'Translate','Summarize','Transcript']
            )

            st.write('You selected:', option)

            return audio, trans , option








# Define the function for the Book Buddy page
def bookbuddy():
    st.title("Book Buddy")
    st.write("This is the Book Buddy page")
    pdf = st.file_uploader("Upload the pdf", type = ['pdf'])
    st.write("thanks for the pdf now leave it to us")
    if pdf is not None:
        st.write("getting text from pdf")
        _ , text = getText(pdf, "")
        st.markdown(text)
        if text is not None:
            st.write("text to audio")
            audio_file = sumToAudio(text)
            st.audio(audio_file.getvalue(), format='audio/mp3', start_time=0)
            st.download_button("Download Audio", data=audio_file.getvalue(), file_name="audio.mp3", mime="audio/mp3")

    # summary kro 
    #  give audio book and summary too 






# Create a dictionary of page names and functions
pages = {
    "Home": home,
    "Assignment Assist": assignment_assist,
    "ytPlus": ytplus,
    "Book Buddy": bookbuddy,
}

# Define the sidebar for navigation
st.sidebar.title("Navigation")
# selection = st.sidebar.radio("Go to", list(pages.keys()))
selection = st.sidebar.selectbox("Go to", list(pages.keys()))
# Call the function based on the user's selection
page = pages[selection]
page()
