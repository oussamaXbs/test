from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

# Database configuration
db_config = {
    "host": "mychatappservice-server.mysql.database.azure.com",
    "user": "rxalspiqjj",
    "password": "96$WOUAb4Z9dWVtV",
    "database": "mychatappservice-database",
    "ssl": {"ca": "/path/to/BaltimoreCyberTrustRoot.crt.pem"}  # Add the correct path to SSL cert
}

@app.route('/')
def home():
    try:
        # Connect to the database
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            cursor.execute("SELECT NOW();")  # Test query to fetch current time
            result = cursor.fetchone()
        connection.close()
        return jsonify({"message": "Connection successful!", "current_time": result[0]})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
