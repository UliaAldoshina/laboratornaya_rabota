import socket
import logging
from concurrent.futures import ThreadPoolExecutor
from repository import CalculationRepository
from service import CalculationService
from protocol import decode_message, encode_message, ProtocolError

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

repo = CalculationRepository()
service = CalculationService(repo)


def handle_client(conn, addr):
    logging.info(f"Client connected: {addr}")
    conn.settimeout(30)  # Таймаут соединения
    buffer = b""
    try:
        while True:
            chunk = conn.recv(1024)
            if not chunk:
                break
            buffer += chunk
            while b"\n" in buffer:
                line, buffer = buffer.split(b"\n", 1)
                if not line.strip():
                    continue

                response_data = process_request(line)
                conn.sendall(response_data)
    except socket.timeout:
        logging.warning(f"Connection timeout for {addr}")
    except Exception as e:
        logging.error(f"Error handling client {addr}: {e}")
    finally:
        conn.close()
        logging.info(f"Client disconnected: {addr}")


def process_request(raw_line: bytes) -> bytes:
    try:
        req = decode_message(raw_line)
        command = req.get("command")
        data = req.get("data", {})
        logging.info(f"Command received: {command}")

        if command == "calculate":
            expr = data.get("expression")
            calc = service.calculate(expr)
            return encode_message("ok", calc.to_dict())
        elif command == "list":
            items = service.get_all()
            return encode_message("ok", {"items": items})
        elif command == "get":
            calc_id = int(data.get("id"))
            item = service.get_by_id(calc_id)
            return encode_message("ok", item)
        elif command == "delete":
            calc_id = int(data.get("id"))
            res = service.delete(calc_id)
            return encode_message("ok", res)
        else:
            return encode_message("error", {"error": f"Unknown command: {command}"})
    except Exception as e:
        return encode_message("error", {"error": str(e)})


def run_server(host="127.0.0.1", port=5000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    logging.info(f"Server started on {host}:{port}")

    executor = ThreadPoolExecutor(max_workers=10)
    try:
        while True:
            conn, addr = server.accept()
            executor.submit(handle_client, conn, addr)
    except KeyboardInterrupt:
        logging.info("Server shutting down")
    finally:
        server.close()


if __name__ == "__main__":
    run_server()