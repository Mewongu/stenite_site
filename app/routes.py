# SPDX-License-Identifer: MPL-2.0
# Copyright © 2020 Andreas Stenberg
from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")
