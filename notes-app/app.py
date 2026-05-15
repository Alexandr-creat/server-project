from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
NOTES_FILE = "/data/notes.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE) as f:
        return json.load(f)

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f)

@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(load_notes())

@app.route("/notes", methods=["POST"])
def add_note():
    note = request.json
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
