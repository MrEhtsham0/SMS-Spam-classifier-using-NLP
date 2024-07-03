from flask import Flask, render_template, request
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from text_preprocess import text_preprocessing

app = Flask(__name__)

# Load model and vectorizer
with open('pkl_models/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('pkl_models/vectorizer.pkl', 'rb') as vectorizer_file:
    tfidf = pickle.load(vectorizer_file)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        email = request.form.get('message')
        try:
            print(f"Original message: {email}")
            processed_email = text_preprocessing(email)
            print(f"Processed message: {processed_email}")
            
            # Vectorize the processed email
            vectorized_email = tfidf.transform([' '.join(processed_email)])  # Ensure it's a list of strings
            print(f"Vectorized message: {vectorized_email}")
            
            result = model.predict(vectorized_email)
            print(f"Prediction: {result}")

            if result[0] == 1:
                result = "Your SMS is Spam"
            else:
                result = "Your SMS is Ham"
        except ValueError as e:
            print("Error in text preprocessing:", e)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
