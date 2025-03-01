from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, my name is <span style='color:green;'>Sharoon</span> and Rafay, and this is my app!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
