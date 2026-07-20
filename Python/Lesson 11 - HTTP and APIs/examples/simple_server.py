from flask import Flask
from flask import request
import os
import json
import base64
import uuid

app = Flask(__name__)


@app.route("/", methods=["GET", "POST", "DELETE", "PATCH", "PUT"])
def hello_world():
    result = "<h1>Hello, world</h1>"
    if request.args:
        result += "\n- Server received: " + json.dumps(
            {key: val for key, val in request.args.items()}
        )
    return result


@app.route("/image", methods=["POST"])
def process_image():
    try:
        if request.content_type.lower() != "image/png":
            raise Exception('Content type must be "image/png"')
        path = os.path.join("./", str(uuid.uuid4()) + ".png")
        with open(path, "wb") as file:
            file.write(base64.b64decode(request.data))

        return f"Image saved to {path}"
    except Exception as e:
        return f"Error processing image {e}", 500


@app.route("/teapot")
def error_val():
    return "I'm a teapot", 418


@app.route("/requestType", methods=["GET", "POST", "DELETE", "PATCH", "PUT"])
def request_type():
    return f"Server received {request.method} HTTP request"


@app.route("/api")
def api():
    result = {}
    for file in os.listdir():
        if not os.path.isdir(file):
            result[file] = {
                "size": os.stat(file).st_size,
                "last_modified": os.stat(file).st_mtime,
                "created": os.stat(file).st_mtime,
                "ext": os.path.splitext(file)[1],
                "type": "file",
            }
        else:
            result[file] = {"type": "dir"}

    return json.dumps(result)


def run():
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    run()
