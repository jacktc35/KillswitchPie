from flask import send_from_directory


@app.route("/static/")
def serve_static(filename):
    return send_from_directory("static", filename)
