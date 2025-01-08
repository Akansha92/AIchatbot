import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = ''

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    
    # Request to GPT-3 API
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use other models like gpt-3.5-turbo as well
        prompt=user_message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Extract the response from GPT-3
    bot_message = response.choices[0].text.strip()

    # Return the response as JSON
    return jsonify({"response": bot_message})

if __name__ == '__main__':
    app.run(debug=True)
