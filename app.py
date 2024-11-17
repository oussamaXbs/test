from flask import Flask, jsonify
import pymysql
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Database configuration from environment variables
db_config = {
    "host": os.getenv("AZURE_MYSQL_HOST"),
    "user": os.getenv("AZURE_MYSQL_USER"),
    "password": os.getenv("AZURE_MYSQL_PASSWORD"),
    "database": os.getenv("AZURE_MYSQL_NAME"),
    "ssl": {"ca": "/path/to/BaltimoreCyberTrustRoot.crt.pem"}  # Update with your SSL path
}

@app.route('/')
def home():
    try:
        # Connect to the database
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            cursor.execute("SELECT NOW();")
            result = cursor.fetchone()
        connection.close()
        return jsonify({"message": "Connection successful!", "current_time": result[0]})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
