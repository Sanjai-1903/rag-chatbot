from flask import Flask, render_template, request, jsonify
from app import chat


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_backend():
    data = request.json
    query=data['query']
    response = chat(query)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True,port=5000)