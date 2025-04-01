from flask import Flask, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    # Handle actual POST request
    data = request.json
    query = data.get('query', '')

    # Call the DeepSeek API
    response = client.chat.completions.create(
        model="deepseek-reasoner",
        messages=[
            {"role": "system", "content": "You are a helpful assistant to a fraud analyst. You are helping them investigate suspicious transactions. Upon receiving data to analyze, you will provide insights and recommendations to the analyst. You explain in logical, sequential steps how you arrived at your conclusions."},
            {"role": "user", "content": query}
        ]
    )

    # Return the response to the frontend
    return jsonify({"response": response.choices[0].message.content})

if __name__ == '__main__':
    app.run(debug=True, port=5000)