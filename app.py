from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL)

@app.route("/", methods=["GET","POST"])
def index():
    student = None
    
    if request.method == "POST":
        search = request.form["search"]
        
        conn = get_connection()
        cur = conn.cursor()
        
        cur.execute("""
        SELECT name, sap_id, course, roll_number, gpa
        FROM students
        WHERE name ILIKE %s OR sap_id ILIKE %s OR roll_number ILIKE %s
        """, (f"%{search}%",f"%{search}%",f"%{search}%"))
        
        student = cur.fetchone()
        
        cur.close()
        conn.close()
    
    return render_template("index.html", student=student)

if __name__ == "__main__":
    app.run()
