from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to home"

import controller.user_controller as user_controller


