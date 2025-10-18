# HNG TASK 0

This is a small Flask API that returns profile information and a dynamic cat fact from the Cat Facts API.

## Project overview
GET `/me` returns JSON in this exact format:
```json
{
  "status": "success",
  "user": {
    "email": "<your email>",
    "name": "<your full name>",
    "stack": "<your backend stack>"
  },
  "timestamp": "<UTC ISO 8601 timestamp>",
  "fact": "<random cat fact>"
}
```

## Tech stack
- Python 3.10+
- Flask
- requests
- python-dotenv

## Setup (local)
1. Clone repo

2. Create & activate virtualenv
   
3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file (example below) in the project root:
```
USER_NAME=Your Full Name
USER_EMAIL=youremail@example.com
USER_STACK=Python/Flask
CAT_FACT_URL=https://catfact.ninja/fact
```

5. Run locally:
```bash
python app.py
# or
flask run
```

