import socket
from protocol import encode_message, decode_message


def main():
    host = "127.0.0.1"
    port = 5000

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(10)

    try:
        client.connect((host, port))
        print("Подключено к серверу калькулятора.")
    except Exception as e:
        print(f"Не удалось подключиться к серверу: {e}")
        return

    try:
        while True:
            print("\n=== КАЛЬКУЛЯТОР КЛИЕНТ ===")
            print("1. Вычислить выражение (calculate)")
            print("2. Получить список всех вычислений (list)")
            print("3. Получить вычисление по ID (get)")
            print("4. Удалить вычисление (delete)")
            print("0. Выход")

            choice = input("Выберите команду: ").strip()
            if choice == "0":
                break

            command = None
            data = {}

            if choice == "1":
                command = "calculate"
                expr = input("Введите математическое выражение (например, 15 * 4 + 2): ")
                data = {"expression": expr}
            elif choice == "2":
                command = "list"
            elif choice == "3":
                command = "get"
                calc_id = input("Введите ID: ")
                data = {"id": int(calc_id)}
            elif choice == "4":
                command = "delete"
                calc_id = input("Введите ID для удаления: ")
                data = {"id": int(calc_id)}
            else:
                print("Неверный выбор.")
                continue

            # Отправка запроса
            req_bytes = encode_message(command, data)
            client.sendall(req_bytes)

            # Получение ответа
            response_bytes = client.recv(1024)
            response = decode_message(response_bytes)

            print("\nОтвет сервера:")
            print(response)

    except socket.timeout:
        print("Превышено время ожидания ответа от сервера (тайм-аут).")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        client.close()
        print("Соединение закрыто.")


if __name__ == "__main__":
    main()