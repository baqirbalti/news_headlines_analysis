# 📰 News Headlines Sentiment Analysis

This project is a machine learning-based web app that classifies **news headlines** into **positive** or **negative** sentiments. It uses traditional NLP techniques such as TF-IDF and Logistic Regression, and provides a simple user interface via **Streamlit** for real-time predictions.

---

## 📌 Project Features

- Analyze the sentiment of any news headline
- Pre-trained model using Logistic Regression
- TF-IDF-based feature extraction
- Simple and interactive **Streamlit** web UI
- Easy to deploy and test via web browser

---

## 📁 Project Structure

news_headlines_analysis/
│
├── sentiment_model.pkl          # Trained sentiment classifier
├── tfidf_vectorizer.pkl         # TF-IDF vectorizer
├── news.csv                     # News headlines dataset
├── streamlit_app.py             # Streamlit app for UI
├── requirements.txt             # Project dependencies
└── README.md                    # Project description


---

## ⚙️ How It Works

1. A dataset of news headlines is cleaned and labeled with sentiment (positive/negative).
2. Text data is vectorized using **TF-IDF**.
3. A **Logistic Regression** model is trained to classify sentiments.
4. The model and vectorizer are saved using **joblib**.
5. The Streamlit UI lets users input a headline and see predicted sentiment in real time.

---

## 🚀 Try the App

You can run the app locally or use the live version (if hosted on Streamlit Cloud):

### ▶️ Run Locally


git clone https://github.com/yourusername/news_headlines_analysis.git
cd news_headlines_analysis
pip install -r requirements.txt
streamlit run streamlit_app.py


Requirements:
All necessary libraries are listed in requirements.txt:
streamlit
pandas
scikit-learn
joblib

Install them using:
pip install -r requirements.txt
