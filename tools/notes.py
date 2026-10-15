import json
from datetime import datetime
from pathlib import Path
from uuid import uuid4


NOTES_FILE = Path(__file__).resolve().parent.parent / "data" / "notes.json"

def read_notes():
    if not NOTES_FILE.exists():
        return []
    return json.loads(NOTES_FILE.read_text(encoding="utf-8"))

def save_note(text):
    notes = read_notes()

    note = {
        "id": str(uuid4()),
        "text": text,
        "created_at": datetime.now().astimezone().isoformat(),
    }
    notes.append(note)

    NOTES_FILE.parent.mkdir(parents=True, exist_ok=True)
    NOTES_FILE.write_text(
        json.dumps(notes, indent=2),
        encoding="utf-8",
    )
    return f"Saved note {note['id']}."

def read_notes_tool():
    return json.dumps(read_notes(), indent=2)
