# SPDX-License-Identifer: MPL-2.0
# Copyright © 2020 Andreas Stenberg

from app import app


if __name__ == "__main__":
    app.run("0.0.0.0", port=80, debug=True)
