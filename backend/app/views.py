from flask import Flask
from app import app

@app.route('/')
def hello():
    return "Hello World!"

# app.route('/test')
# def test():
#     # put a form for taking in commands here