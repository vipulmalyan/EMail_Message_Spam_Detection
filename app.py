import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the pre-trained model and vectorizer
model = joblib.load('/Users/vipul/Downloads/Projects/Email:Message Spam Detection/model.pkl')
vectorizer = joblib.load('/Users/vipul/Downloads/Projects/Email:Message Spam Detection/vectorizer.pkl')

# Function to classify emails
def classify_email(text):
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)
    return prediction[0]

# Streamlit app
def main():
    st.title("Email/SMS Spam Classifier")

    # Input text area for user to input email text
    user_input = st.text_area('Enter the text of the email:')
    if st.button('Classify'):
        if user_input:
            prediction = classify_email(user_input)
            if prediction == 1:
                st.error('This email is classified as SPAM.')
            else:
                st.success('This email is classified as HAM (NOT SPAM).')
        else:
            st.warning('Please enter some text.')

if __name__ == "__main__":
    main()





page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://wallpapers.com/images/hd/email-background-t0cbknt4ahfsy4rc.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

hide_st_style = '''
<style> footer {visibility: hidden;} 
</style>
'''
st.markdown(hide_st_style, unsafe_allow_html=True)

footer_html = """
<style>
.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    color: white; /* Text color */
    padding: 10px;
    text-align: center; /* Center the text */
    font-size: 18px; /* Adjust the font size */
}
</style>
<div class="footer">Made by Vipul Malyan</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)