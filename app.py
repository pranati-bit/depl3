from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        sapid = request.form["sapid"]
        rollno = request.form["rollno"]
        name = request.form["name"]
        div = request.form["div"]
        cgpa = request.form["cgpa"]

        return f"""
        <h2>Student Details</h2>
        SAP ID: {sapid}<br>
        Roll No: {rollno}<br>
        Name: {name}<br>
        Division: {div}<br>
        CGPA: {cgpa}
        """

    return """
    <h2>Enter Student Details</h2>
    <form method="post">
        SAP ID: <input type="text" name="sapid"><br><br>
        Roll No: <input type="text" name="rollno"><br><br>
        Name: <input type="text" name="name"><br><br>
        Division: <input type="text" name="div"><br><br>
        CGPA: <input type="text" name="cgpa"><br><br>
        <input type="submit">
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)