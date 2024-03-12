from flask import Flask, render_template, request
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the pre-trained model and vectorizer
model = joblib.load('models/model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

# Home route
@app.route('/', methods=['GET', 'POST'])
def home():
    sentiment = None
    input_text = None

    if request.method == 'POST':
        # Get the input text from the form
        input_text = request.form['text']
        
        # Preprocess the input text using the vectorizer
        input_text_tfidf = vectorizer.transform([input_text])
        
        # Make prediction using the model
        prediction = model.predict(input_text_tfidf)[0]
        
        # Determine the sentiment label
        sentiment = "Positive" if prediction == 1 else "Negative"
        
    return render_template('index.html', sentiment=sentiment, input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)
