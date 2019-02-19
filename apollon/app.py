import json
import logging
import os


from flask import Flask, jsonify, render_template, request

from apollon.reports.mamma import create as mamma_create
from apollon.reports.colon import create as colon_create
from apollon.reports.MRProstate import create as MRProstate_create
from apollon.reports.PathoProstate import create as PathoProstate_create

app = Flask(__name__, instance_relative_config=True, static_url_path='/static')
app.config.from_object("apollon.default_config")
app.config.from_pyfile("config.cfg", silent=True)
version = app.config["VERSION"] = "0.0.1"
app.config['DEBUG'] = True


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
    print(form)
    report_type = form["report_type"]
    if report_type == "mamma":
        s1, s2 = mamma_create(request.form)
    elif report_type == "MRProstate":
        s1, s2 = MRProstate_create(request.form)
    elif report_type == "PathoProstate":
        s1, s2 = MRProstate_create(request.form)
    elif report_type == "colon":
        s1, s2 = colon_create(request.form)
    template = report_type + ".html"
    return render_template(template, form=form, s1=s1, s2=s2)
