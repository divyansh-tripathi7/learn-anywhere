import streamlit as st

# Set page title
st.set_page_config(page_title="My Studying Platform")

# Set page header
st.title("Welcome to My Studying Platform")

# Add a brief description of the platform
st.write("This platform is designed to help you study smarter and more efficiently. With our tools and resources, you'll be able to stay organized, manage your time effectively, and ace your exams!")

# Add a menu to select options
option = st.sidebar.selectbox("Choose an option", ("Home", "Study Resources", "Time Management", "Exam Prep"))

# Create different sections for each option
if option == "Home":
    st.write("Welcome to the Home page!")
    st.write("Here, you can access all the features and resources available on our platform.")
    
elif option == "Study Resources":
    st.write("Looking for study materials or resources? You've come to the right place!")
    st.write("Browse our collection of textbooks, tutorials, and other study aids to help you ace your exams!")
    
elif option == "Time Management":
    st.write("Struggling to manage your time effectively? We've got you covered!")
    st.write("Our time management tools and tips will help you stay on track and make the most of your study sessions.")
    
elif option == "Exam Prep":
    st.write("Getting ready for an exam? Don't stress!")
    st.write("Our exam preparation resources and practice tests will help you feel confident and well-prepared on exam day.")
