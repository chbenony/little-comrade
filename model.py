import json
from urllib.request import Request, urlopen


def ask_model(messages, tools):
    payload = {
        "model": "gpt-oss:20b",
        "messages": messages,
        "stream": False,
        "tools": tools,
    }

    request = Request(
        "http://localhost:11434/api/chat",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    with urlopen(request, timeout=120) as response:
        return json.load(response)["message"]
