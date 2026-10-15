from .clock import get_current_time
from .notes import read_notes_tool, save_note


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "save_note",
            "description": "Save a note when the user asks you to remember something.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "The information to remember.",
                    },
                },
                "required": ["text"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_notes",
            "description": "Read previously saved notes about the user.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current local date and time.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        },
    }
]


TOOL_FUNCTIONS = {
    "get_current_time": get_current_time,
    "save_note": save_note,
    "read_notes": read_notes_tool,
}
