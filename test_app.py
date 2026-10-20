import app as notes_app
import pytest


@pytest.fixture(autouse=True)
def reset_store():
    notes_app.notes.clear()
    notes_app.next_id = 1
    yield
    notes_app.notes.clear()
    notes_app.next_id = 1


@pytest.fixture
def client():
    notes_app.app.config["TESTING"] = True
    return notes_app.app.test_client()


def test_health(client):
    assert client.get("/health").status_code == 200


def test_list_notes_empty(client):
    resp = client.get("/notes")
    assert resp.status_code == 200
    assert resp.get_json() == []


def test_add_note(client):
    resp = client.post("/notes", json={"text": "first note"})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["id"] == 1
    assert data["text"] == "first note"


def test_add_note_rejects_empty(client):
    resp = client.post("/notes", json={"text": "   "})
    assert resp.status_code == 400


def test_delete_note(client):
    client.post("/notes", json={"text": "to delete"})
    resp = client.delete("/notes/1")
    assert resp.status_code == 200
    assert client.get("/notes").get_json() == []


def test_delete_missing_note(client):
    assert client.delete("/notes/99").status_code == 404
