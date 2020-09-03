# SPDX-License-Identifer: MPL-2.0
# Copyright © 2020 Andreas Stenberg
from werkzeug.utils import redirect

from app import app


@app.errorhandler(404)
def four_oh_four(error):
    return redirect("/")
