from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import *
import re
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])

def process_data():
    # Get data from request body
    data = request.get_json()  # Nếu dữ liệu là JSON
    review = str(data['review'])
    # Convert text to lowercase
    review = review.lower()
    # Removing punctuation
    review = re.sub(r'[^\w\s]', '', review)
    # remove word not in world list
    review = remove_words_not_in_list(review)
    # correct spelling and tokenize
    review = correct_spelling(review)
    # Dealing with emojis and emoticon
    review = remove_emojis(review)
    return jsonify({
        "result": review
    })

if __name__ == '__main__':
    # Run the app in debug mode
    app.run(debug=True)

