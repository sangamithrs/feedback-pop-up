import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

vectorizer = CountVectorizer()
model = MultinomialNB()

# Save empty model and vectorizer
joblib.dump(vectorizer, 'vectorizer.joblib')
joblib.dump(model, 'sentiment_model.joblib')