# SPDX-License-Identifer: MPL-2.0
# Copyright © 2020 Andreas Stenberg

from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello world"