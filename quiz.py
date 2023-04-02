import random
import streamlit as st

# Define the questions and answers for the quiz
# Each question is a dictionary with 'question', 'options', and 'answer' keys
# 'options' is a list of four possible answer choices
questions = [
    {
        'question': 'What is the capital city of India?',
        'options': ['New Delhi', 'Mumbai', 'Chennai', 'Kolkata'],
        'answer': 'New Delhi'
    },
    {
        'question': 'Who is the author of "To Kill a Mockingbird"?',
        'options': ['Harper Lee', 'F. Scott Fitzgerald', 'Ernest Hemingway', 'John Steinbeck'],
        'answer': 'Harper Lee'
    },
    {
        'question': 'What is the highest mountain in the world?',
        'options': ['Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse'],
        'answer': 'Mount Everest'
    },
    {
        'question': 'What is the largest planet in our solar system?',
        'options': ['Jupiter', 'Saturn', 'Neptune', 'Uranus'],
        'answer': 'Jupiter'
    },
    {
        'question': 'Which country won the first FIFA World Cup in 1930?',
        'options': ['Uruguay', 'Brazil', 'Argentina', 'Spain'],
        'answer': 'Uruguay'
    }
]

# Define function to generate shuffled answer choices for a given question
def shuffle_options(options, answer):
    # Remove the correct answer from the list of options
    options.remove(answer)
    # Shuffle the remaining options
    random.shuffle(options)
    # Add the correct answer back to the beginning of the list
    options.insert(0, answer)
    return options

# Define Streamlit app function for quiz page
def app(questions):
    # Set page title
    st.title("Quiz Me!")
    
    # Display instructions
    st.write("Welcome to the quiz! Answer the following multiple-choice questions to test your knowledge.")
    
    # Shuffle the order of questions
    random.shuffle(questions)
    
    # Keep track of number of correct answers
    num_correct = 0
    
    # Loop through each question and display it
    for i, q in enumerate(questions):
        # Display the question number and text
        st.write(f"\n{i+1}. {q['question']}")
        
        # Shuffle the order of answer choices
        options = shuffle_options(q['options'], q['answer'])
        
        # Display each answer choice as a radio button
        selected_option = st.radio("", options)
        
        # Check if selected answer is correct
        if selected_option == q['answer']:
            st.write("Correct!")
            num_correct += 1
        else:
            st.write(f"Sorry, the correct answer is {q['answer']}.")
    
    # Display final score
    st.write(f"\nYou answered {num_correct} out of {len(questions)} questions correctly.")
