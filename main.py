from flask import Flask, render_template
import pandas as pd
import joblib
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

# Load the vectorizer and model
vectorizer = joblib.load('vectorizer.joblib')
model = joblib.load('sentiment_model.joblib')

# Sample data for generating graphs
feedback_data = {
    'sentiment': ['Positive', 'Neutral', 'Negative', 'Positive', 'Negative'],
    'keywords': ['AI', 'feedback', 'CV', 'AI', 'feedback'],
    'categorization': ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied'],
    'patterns': ['Pattern A', 'Pattern B', 'Pattern A', 'Pattern C', 'Pattern B'],
    'improvement': ['Yes', 'No', 'Yes', 'No', 'Yes']
}

def generate_graph(data, title):
    df = pd.DataFrame(data, columns=['value'])
    fig = px.bar(df, x='value', title=title)
    graph_json = pio.to_json(fig)
    return graph_json

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ai_parameters')
def ai_parameters():
    graphs = {
        'sentiment': generate_graph(feedback_data['sentiment'], 'Sentiment Analysis'),
        'keywords': generate_graph(feedback_data['keywords'], 'Keyword Analysis'),
        'categorization': generate_graph(feedback_data['categorization'], 'Feedback Categorization'),
        'patterns': generate_graph(feedback_data['patterns'], 'Pattern Identification'),
        'improvement': generate_graph(feedback_data['improvement'], 'Continuous Improvement')
    }
    return render_template('ai_parameters.html', graphs=json.dumps(graphs))

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    # Handle feedback submission
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)



