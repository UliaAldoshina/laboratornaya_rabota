from protocol import encode_message, decode_message


def test_encode_decode_message():
    command = "calculate"
    data = {"expression": "2 + 2"}

    encoded = encode_message(command, data)
    assert isinstance(encoded, bytes)
    assert encoded.endswith(b"\n")

    decoded = decode_message(encoded)
    assert decoded["command"] == command
    assert decoded["data"] == data