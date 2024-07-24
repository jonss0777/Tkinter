from flask import Flask, request

# Variable rules:
# Request Object: 
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Home</p>"

@app.route("/register")
def register():
    return "<p>register</p>"

@app.route("/login")
def login():
    return "<p>login</p>"

@app.route("/create_user")
def create_user():
    return "<p>create</p>"

@app.route("/update_user")
def update_user():
    return "<p>update</p>"

@app.route("/delete_user")
def deleteUser():
    return "<p>delete</p>"