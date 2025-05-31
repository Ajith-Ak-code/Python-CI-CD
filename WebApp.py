from flask import Flask

app=Flask(__name__)

@app.route('/')
def homepage():
    return 'Welcome to this page'

if __name__=="__main__":
    app.run(debug=True)