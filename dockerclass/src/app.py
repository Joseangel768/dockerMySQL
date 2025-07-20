from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    try:
        conn = mysql.connector.connect(
            host=os.environ.get("MYSQL_HOST", "db"),
            user=os.environ.get("MYSQL_USER", "user"),
            password=os.environ.get("MYSQL_PASSWORD", "password"),
            database=os.environ.get("MYSQL_DATABASE", "appdb")
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'Conexión exitosa a MySQL!'")
        result = cursor.fetchone()
        return f"Hola Mundo! {result[0]}"
    except Exception as e:
        return f"Error al conectar a MySQL: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
