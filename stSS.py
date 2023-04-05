import streamlit as st
from streamlit.hashing import _CodeHasher
from streamlit.report_thread import get_report_ctx
from streamlit.server.server import Server
import streamlit as st
from ytPlus import * 
from gptKaam import * 
import pytube, whisper, openai

def get_session_id():
    session_id = get_report_ctx().session_id
    if session_id is None:
        session_id = _CodeHasher().to_bytes([0])
    return session_id

class SessionState:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.session_id = get_session_id()

    def __call__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            self.kwargs[key] = value

    def __getitem__(self, key):
        return self.kwargs.get(key, None)

    def __repr__(self):
        return str(self.kwargs)

def ytplus():
    session_state = SessionState(user_input="", task_option="Transcript")

    st.title("ytPlus")
    st.write("This is the ytPlus page")

    session_state.user_input = ytBasic()

    if st.button("Let's GOOO"):
        session_state.audio, session_state.text = urlToText(session_state.user_input)

    session_state.task_option = st.selectbox(
        'What task is to be performed on the video?',
        options=['Transcript', 'Summarize', 'Translate'],
        index=['Transcript', 'Summarize', 'Translate'].index(session_state.task_option)
    )

    if session_state.task_option == "Transcript":
        st.markdown(session_state.text)
    elif session_state.task_option == "Summarize":
        summary = getSummary(session_state.text)
        st.markdown(summary)
    elif session_state.task_option == "Translate":
        st.write("Translate kro bhai")

