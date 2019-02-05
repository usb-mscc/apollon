import json
import logging
import os


from flask import Flask, jsonify, render_template, request

from apollon.reports.prostate import create


app = Flask(__name__, instance_relative_config=True)
app.config.from_object("apollon.default_config")
app.config.from_pyfile("config.cfg", silent=True)
version = app.config["VERSION"] = "0.0.1"


@app.route("/")
def main():
    return render_template("index.html", form=None)


@app.route("/generate", methods=["POST", "GET"])
def generate():
    form = request.form
    s1, s2 = create(request.form)
    return render_template("index.html", form=form, s1=s1, s2=s2)
