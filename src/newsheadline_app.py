import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load the trained model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Streamlit UI
st.title("📰 News Sentiment Classifier")
st.write("Enter a news sentence to predict its sentiment.")

user_input = st.text_area("Enter news headline or content here:", "")

if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        transformed = vectorizer.transform([user_input])
        prediction = model.predict(transformed)[0]
        st.success(f"Predicted Sentiment: **{prediction}**")


import joblib

# Save model and vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("Model and Vectorizer saved!")
