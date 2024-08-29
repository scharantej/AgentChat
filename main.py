
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define agents and their actions/responses
agents = {
    "agent1": {
        "actions": {
            "hello": "Hi there! How can I help you today?",
            "goodbye": "Goodbye! Have a nice day."
        },
        "inputs": {
            "name": "What is your name?"
        }
    },
    "agent2": {
        "actions": {
            "weather": "What's the weather like today?",
            "news": "What's the latest news?"
        },
        "inputs": {
            "location": "Where are you located?"
        }
    }
}

# Home page route
@app.route('/')
def index():
    return render_template('index.html', agents=agents)

# Chat page route
@app.route('/chat/<agent_name>')
def chat(agent_name):
    agent = agents.get(agent_name)
    return render_template('chat.html', agent=agent)

# Action handling route
@app.route('/action/<agent_name>', methods=['POST'])
def action(agent_name):
    agent = agents.get(agent_name)
    action = request.form.get('action')
    response = agent['actions'].get(action)
    return response

# Response handling route
@app.route('/response/<agent_name>', methods=['POST'])
def response(agent_name):
    agent = agents.get(agent_name)
    input_value = request.form.get('input')
    response = "Got it. {}".format(input_value)
    return response

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
