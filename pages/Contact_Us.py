import streamlit as st
import pandas
from send_email import send_email

st.title("Contact Us")

df = pandas.read_csv("topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Enter your email address")
    topic = st.selectbox("What topic would you like to discuss?", df['topic'])
    text = st.text_area("Your message")
    message = f"""\
Subject: Message from Best Company Contact Us form
From: {user_email}
{topic}
{text}
"""

    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email has been sent successfully")
