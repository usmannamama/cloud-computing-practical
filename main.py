from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head><title>Cloud Computing Practical</title></head>
        <body style="text-align:center; font-family:Arial;">
            <h1>Welcome to Our Cloud Computing Practical</h1>
            <h2>ITC4344</h2>
            <p>This Python application is deployed using Render.</p>
            <p>Our cloud application is running successfully!</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
