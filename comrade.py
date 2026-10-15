from time import perf_counter

from model import ask_model
from tools import TOOLS, TOOL_FUNCTIONS


def chat():
    messages = []

    while True:
        text = input("You: ")
        if text.lower() in {"quit", "exit"}:
            break

        messages.append({"role": "user", "content": text})

        while True:
            started = perf_counter()
            reply = ask_model(messages, TOOLS)
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
                    "tool_name": name,
                    "content": tool_result,
                })
