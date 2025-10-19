from flask import Flask, jsonify, Response
import requests
import json
from datetime import datetime, timezone
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

name = os.getenv("USER_NAME")
email = os.getenv("USER_EMAIL")
cat_fact_url = os.getenv("CAT_FACT_URL")

tech_stack = "Python/Flask"

@app.route('/', methods=['GET'])
def home():
    return "Hii, go to /me to see the API response."

@app.route('/me', methods=['GET'])
def hng_task_0():
    try:
        response = requests.get(cat_fact_url)
        if response.status_code == 200:
            cat_fact = response.json().get('fact', 'No cat fact found')
            status = "success"
        else:
            response.raise_for_status()
    except requests.RequestException:
        return jsonify({'error': 'Failed to fetch cat fact'}), 503

    data = {
        "status": status,
        "user": {
            "email": email,
            "name": name,
            "stack": tech_stack
        },
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "fact": cat_fact
    }

   
    json_data = json.dumps(data, indent=2, ensure_ascii=False)
    return Response(json_data, mimetype='application/json')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

