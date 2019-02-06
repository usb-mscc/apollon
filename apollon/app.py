import json
import logging
import os


from flask import Flask, jsonify, render_template, request

from apollon.reports.prostate import create as prostate_create
from apollon.reports.mama import create as mama_create

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("apollon.default_config")
app.config.from_pyfile("config.cfg", silent=True)
version = app.config["VERSION"] = "0.0.1"


@app.route("/")
def main():
    return render_template("index.html", form=None)


@app.route("/report")
def r():
    type = request.args.get("type")
    template = type + ".html"
    return render_template(template, form=None)


@app.route("/generate", methods=["POST", "GET"])
def generate():
    form = request.form
    report_type = form["report_type"]
    if report_type == "mamma":
        s1, s2 = create(request.form)
    elif report_type == "prostate"
        s1, s2 = create(request.form)
    else report_type == "colon"
        s1, s2 = create(request.form)
    return render_template("prostate.html", form=form, s1=s1, s2=s2)
