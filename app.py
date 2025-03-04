from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, my name is Zeeshan and <span style='color:blue;'>Hamza</span> and this is my app!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
