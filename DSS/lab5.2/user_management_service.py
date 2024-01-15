from flask import Flask, request
import json
import os
from dapr.clients import DaprClient

app = Flask(__name__)
dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)

@app.route('/api/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    # Process user data and store it in the database
    # ...

    # Publish an event to notify other services about the new user
    with DaprClient() as d:
        d.publish_event("pubsub", "new-user", json.dumps(user_data))

    return "User created successfully", 201

if __name__ == '__main__':
    app.run(port=dapr_port)
