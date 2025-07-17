from flask import Flask, jsonify, Response
from flask_cors import CORS
import os
import json
import requests

app = Flask(__name__)
CORS(app)


def load_updates():
    with open("updates.json", "r") as f:
        return json.load(f)


@app.route('/', methods=['GET'])
def index():
    url = 'https://raw.githubusercontent.com/eesazahed/sat-prep-app/refs/heads/main/public/index.html'
    r = requests.get(url)
    return Response(r.text, content_type='text/html')


@app.route('/updates', methods=['GET'])
def get_updates():
    try:
        updates = load_updates()
        return jsonify(updates)
    except FileNotFoundError:
        return jsonify([]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
