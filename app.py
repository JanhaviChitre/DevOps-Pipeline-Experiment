"""Simple Notes API - mini project for the DevOps pipeline experiment."""
from flask import Flask, jsonify, request

app = Flask(__name__)

notes = []
next_id = 1


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/notes", methods=["GET"])
def list_notes():
    return jsonify(notes), 200


@app.route("/notes", methods=["POST"])
def add_note():
    global next_id
    data = request.get_json(silent=True) or {}
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "text is required"}), 400
    note = {"id": next_id, "text": text}
    next_id += 1
    notes.append(note)
    return jsonify(note), 201


@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            return jsonify({"message": "deleted"}), 200
    return jsonify({"error": "not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
