from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h2>Hello, Udacity! This is Oluseyi Akerele's Capstone project. <h2>"

# Run on port 80
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True) 