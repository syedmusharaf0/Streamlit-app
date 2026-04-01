import streamlit as st

# Title
st.title("Hello, I'm Musharaf 👋")

# Subtitle
st.subheader("Welcome to my first Streamlit App 🚀")

# Text
st.write("This is my beginner DevOps + Streamlit project.")

# Input box
name = st.text_input("Enter your name:")

# Button
if st.button("Say Hello"):
    if name:
        st.success(f"Hello {name}! 👋 Welcome to Musharaf's app.")
    else:
        st.warning("Please enter your name.")

# Sidebar
st.sidebar.title("About Me")
st.sidebar.write("Hi, I'm Musharaf — Learning DevOps & Data Science 🚀")
st.sidebar.write("MY EAGER TO CONTRIBUTE TO DEVOPS")
st.sidebar.write("hello learning devops")
st.sidebar.write("CI/CD")