## Hey I want to create a web app that will allow you to chat with agents that you have been granted access to. Each agent has its unique actions and inputs.

### HTML Files

1. **index.html:** The main page of the application. It will include a list of available agents and their descriptions.
2. **chat.html:** The page where users can chat with a selected agent.

### Routes

1. **`/`:** Renders the index.html page, displaying the list of agents.
2. **`/chat/<agent_name>`:** Renders the chat.html page with the specified agent.
3. **`/action/<agent_name>`:** Handles user input and executes the appropriate action for the specified agent.
4. **`/response/<agent_name>`:** Returns the response from the specified agent.