import streamlit as st
from ocr import *
# Define your app layout
# from quiz import *
st.set_page_config(page_title="Learn Anything", page_icon=":books:", layout="wide")
st.title("Welcome to My Learning Platform")
st.write("What do you want to learn today?")    
load_dotenv() # Load secrets

print(os.getenv("OPENAI_API_KEY"))
gpt_3 = GPT_3(os.getenv('OPENAI_API_KEY'))

if "page" not in st.session_state:
    st.session_state.page = "search"

inp_val =""

if st.session_state.page == "search":

    # Add a field to select the type of input
    input_type = st.selectbox("Select input type:", ("Text", "Image",  "Audio", "Video"))

    # If the user selects "Text" as input type
    if input_type == "Text":
        user_input = st.text_input("Enter a topic:")

    with st.form("search_results"):
        # Add a search button
        search_button = st.form_submit_button("Search")

        if search_button:
            # Call your API with the search query and display the results
            # Replace this with your actual API call
            results = gpt_3.teach(user_input)
            inp_val = results
            # results = ["Result 1", "Result 2", "Result 3"]
            st.write("Here are your search results:")
            st.write(results)

    # Write the logic for your app
    # if st.button("Search"):
    #     # Call your API and display the results
    #     # Replace this with your actual API call
    #     results = gpt_3.teach(user_input)
    #     # results = ["Result 1", "Result 2", "Result 3"]
    #     st.write("Here are your search results:")
    #     st.write(results)

            # Add buttons for learning more and taking a quiz
if st.button("Learn more"):
            # Display additional resources for learning about the topic
    st.header("Additional resources:")
    res = gpt_3.resources(user_input)
    # res = gpt_3.resources(results)
    st.write("Here are some additional resources to help you learn more about this topic:")
    st.write(res)

            # Replace this with actual links or resources
if st.button("Quiz me"):
        
        quiz_questions = gpt_3.QuizMe(inp_val)

        # st.header(quiz_questions)
        # quiz_qs = eval(quiz_questions)
        # st.header("quiz")
        # st,write("quiz_questions")
        # []
            # {
            #     "question": "Question 1",
            #     "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            #     "correct_answer": "Option 1"
            # },
            # {
            #     "question": "Question 2",
            #     "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            #     "correct_answer": "Option 2"
            # },
            # {
            #     "question": "Question 3",
            #     "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            #     "correct_answer": "Option 3"
            # },
            # {
            #     "question": "Question 4",
            #     "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            #     "correct_answer": "Option 4"
            # },
            # {
            #     "question": "Question 5",
            #     "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            #     "correct_answer": "Option 1"
            # },
        # ]

        # st.session_state.page = "quiz"
        
        st.write(quiz_questions)
        # st.header("used eval then")
        # st.write(quiz_qs)

        # score = app(quiz_qs)
        # st.write(f"Your score is {score}/5")

# elif st.session_state.page == "quiz":
#     app()


#     if st.button("Back to Search"):
#         st.session_state.page = "search"

            # Display a quiz or some other interactive component for testing the user's knowledge of the topic
    # st.header("Test your knowledge:")
    # quiz = gpt_3.QuizMe(user_input)
    # st.write("Take this quiz to test your knowledge of this topic:")
    # st.write(quiz)
        # for result in results:
        #     st.write(result)
            # Add a block for getting more resources to learn about the topic
        # st.header("Additional resources:")
        # st.write("Here are some additional resources to help you learn more about this topic:")

        # # Add a block for quizzing the user on their knowledge of the topic
        # st.header("Test your knowledge:")
        # st.write("Take this quiz to test your knowledge of this topic:")

# # If the user selects "Image" as input type
# elif input_type == "Image":
#     image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

#     image_path = image_file.name
#     textIm = read_img(image_path)


#     # Write the logic for your app
#     if st.button("Submit"):
#         # Call your API with the uploaded image and display the results
#         # Replace this with your actual API call
#         results = ["Result 1", "Result 2", "Result 3"]
#         st.write("Here are your search results:")
#         for result in results:
#             st.write(result)

# # If the user selects "Audio" as input type
# elif input_type == "Audio":
#     audio_file = st.file_uploader("Upload an audio file", type=["mp3"])

#     # Write the logic for your app
#     if st.button("Submit"):
#         # Call your API with the uploaded audio file and display the results
#         # Replace this with your actual API call
#         results = ["Result 1", "Result 2", "Result 3"]
#         st.write("Here are your search results:")
#         for result in results:
#             st.write(result)

# # If the user selects "Video" as input type
# elif input_type == "Video":
#     video_url = st.text_input("Enter a video URL:")

#     # Write the logic for your app
#     if st.button("Submit"):
#         # Call your API with the video URL and display the results
#         # Replace this with your actual API call
#         results = ["Result 1", "Result 2", "Result 3"]
#         st.write("Here are your search results:")
#         for result in results:
#             st.write(result)


