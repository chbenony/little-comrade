import json
from urllib.request import Request, urlopen
from datetime import datetime
from time import perf_counter

messages = []

def get_current_time():
    return datetime.now().astimezone().strftime(
        "%Y-%m-%d %I:%M:%S %p %Z (UTC%z)"
    )

TOOLS = [
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

def ask_model(messages):
    payload = {
        "model": "gpt-oss:20b",
        "messages": messages,
        "stream": False,
        "tools": TOOLS,
    }
    
    request = Request(
        "http://localhost:11434/api/chat",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"} 
    )
    
    with urlopen(request, timeout=120) as response:
        return json.load(response)["message"]

TOOL_FUNCTIONS = {
    "get_current_time": get_current_time,
}


def chat():
    while True:
        text = input("You: ")
        if text.lower() in {"quit", "exit"}:
            break
        
        messages.append({"role": "user", "content": text})
        
        while True:
            started = perf_counter()
            reply =  ask_model(messages)
            print(f"[model: {perf_counter() - started: .2f}s]")
            messages.append(reply)
            
            tool_calls = reply.get("tool_calls", [])
            
            if not tool_calls:
                print(f"Comrade: {reply['content']}")
                break
            
            for call in tool_calls:
                name = call["function"]["name"]
                arguments = call["function"].get("arguments", {})
                
                function = TOOL_FUNCTIONS.get(name)
                
                if function is None:
                    tool_result = f"Unknown tool: {name}"
                else:
                    tool_result = function(**arguments)
                
                print(f"[tool: {name}] {tool_result}")
                
                messages.append({
                    "role": "tool",
                    "tool_name": "name",
                    "content": tool_result,
                })
