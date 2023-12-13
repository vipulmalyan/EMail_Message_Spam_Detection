# Email/SMS Spam Classifier

![Email/SMS Spam Classifier](https://wallpapers.com/images/hd/email-background-t0cbknt4ahfsy4rc.jpg)

## Overview

This Streamlit application serves as an Email/SMS Spam Classifier. It employs a pre-trained Random Forest model and CountVectorizer to predict whether a given text is spam or ham (not spam).

### Features

- **Classification of Emails/SMS**: Users can input email or SMS text and classify it as spam or not.
- **User-Friendly Interface**: Simple text input area with a classify button for easy interaction.

## Usage

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/vipulmalyan/spam-classifier-app.git
    cd spam-classifier-app
    ```

2. **Install Dependencies:**
    Ensure you have Streamlit and other necessary dependencies installed:
    ```bash
    pip install streamlit pandas scikit-learn joblib
    ```

3. **Run the Streamlit App:**
    ```bash
    streamlit run app.py
    ```

4. **Using the Application**:
    - Enter the text of the email or SMS in the text area.
    - Click the "Classify" button to get the prediction.

## Application Interface

![Application Screenshot](<screenshot_image_url>)

## Model Details

The application uses a pre-trained Random Forest model and CountVectorizer for text classification.

## Acknowledgments

The application was built using Streamlit and scikit-learn library for machine learning.

## License

This project is licensed under the [MIT License](LICENSE).
