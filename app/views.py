from distutils.log import error
import mimetypes
from re import template
from urllib import request
from app import app
import io
import os
from flask import render_template, request, send_file
from app.tts import synthesizer
import requests

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/call/martha", methods = ["POST"])
def call_martha():
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", data ={
        "secret" : os.environ.get("RECAPTCHA_SITE_SECRET"),
        "response": request.form["g-recaptcha-response"]
    })

    if(response.status_code == 200):
        data = response.json()
        if(data["success"]):
            if(request.form["text"]):
                text = request.form["text"]
                outputs = synthesizer.tts(text)
                out = io.BytesIO()
                synthesizer.save_wav(outputs, out)
                return send_file(out, mimetype="audio/wav")
            else:
                return {"error": "Please provide the text"}, 400 
    return {"error": "Please check the recaptcha"}, 400 
