from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = mysql.connector.connect(
            host='db',
            user='root',
            password='KAUSTUBH010',
            database='testdb',
            port=3306
        )
        return "Connected to MySQL!"
    except Exception as e:
        return f"Error : {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
