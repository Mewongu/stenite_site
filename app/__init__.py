# SPDX-License-Identifer: MPL-2.0
# Copyright © 2020 Andreas Stenberg

from flask import Flask


app = Flask(__name__)

from app import routes, errors
