import requests
import streamlit as st
from  gptKaam import * 
load_dotenv()
gpt_3 = GPT_3(os.getenv('OPENAI_API_KEY'))



ELAI_API_ENDPOINT = 'https://apis.elai.io/api/v1/videos/generate/text'
ELAI_API_KEY = 'YOUR_API_KEY_HERE'

st.title('Elai Text to Video Converter')


text_input = st.text_input('Enter your text')
submit_button = st.button('Convert to Video')

processed_text = gpt_3.script(text_input)

if submit_button:
    payload = {
        'api_key': ELAI_API_KEY,
        'text': processed_text
    }
    response = requests.post(ELAI_API_ENDPOINT, json=payload)

    if response.ok:
        video_url = response.json()['url']
        st.video(video_url)
    else:
        st.error('Error converting text to video')

