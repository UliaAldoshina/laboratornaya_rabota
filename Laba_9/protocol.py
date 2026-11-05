import json

class ProtocolError(Exception):
    pass

def encode_message(command: str, data: dict) -> bytes:
    message = {
        "command": command,
        "data": data
    }
    return (json.dumps(message) + "\n").encode("utf-8")

def decode_message(raw_data: bytes) -> dict:
    try:
        text = raw_data.decode("utf-8").strip()
        if not text:
            return {}
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise ProtocolError(f"Некорректный JSON: {e}")