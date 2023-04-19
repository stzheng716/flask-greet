from flask import Flask

app = Flask(__name__)

@app.get("/welcome")
def welcome():
    
    html =  "<p>welcome</p>"
    return html

@app.get("/welcome/home")
def welcomehome():
    
    html =  "<p>welcome home</p>"
    return html

@app.get("/welcome/back")
def welcomeback():
    
    html =  "<p>welcome back</p>"
    return html