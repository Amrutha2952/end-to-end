import joblib

# Load the trained model
model = joblib.load('models/model.pkl')

# Load the TF-IDF vectorizer
vectorizer = joblib.load('models/vectorizer.pkl')

# Input text for prediction
input_text = 'happy bday!'

# Preprocess the input text using the TF-IDF vectorizer
input_text_tfidf = vectorizer.transform([input_text])

# Make predictions
prediction = model.predict(input_text_tfidf)[0]

# Print the predicted sentiment
print("Predicted sentiment:", prediction)
