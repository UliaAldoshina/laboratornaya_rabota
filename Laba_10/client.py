import requests

BASE_URL = "http://127.0.0.1:5000"


def main():
    while True:
        print("\n=========================")
        print("    REST CLIENT (LAB 10)")
        print("=========================")
        print("1. Получить список всех книг")
        print("2. Получить книгу по ID")
        print("3. Создать новую книгу")
        print("4. Изменить книгу полностью (PUT)")
        print("5. Частично изменить книгу (PATCH)")
        print("6. Удалить книгу (DELETE)")
        print("7. Фильтрация книг (по жанру/автору)")
        print("8. Сортировка (по цене/году)")
        print("9. Специализированный поиск по автору")
        print("0. Выход")
        print("=========================")

        choice = input("Выберите действие: ").strip()

        try:
            if choice == "1":
                resp = requests.get(f"{BASE_URL}/books")
                print(f"\nКод ответа: {resp.status_code}")
                print(resp.json())

            elif choice == "2":
                b_id = input("Введите ID книги: ")
                resp = requests.get(f"{BASE_URL}/books/{b_id}")
                print(f"\nКод ответа: {resp.status_code}")
                print(resp.json())

            elif choice == "3":
                title = input("Название: ")
                author = input("Автор: ")
                year = int(input("Год: "))
                genre = input("Жанр: ")
                price = float(input("Цена: "))

                payload = {"title": title, "author": author, "year": year, "genre": genre, "price": price}
                resp = requests.post(f"{BASE_URL}/books", json=payload)
                print(f"\nКод ответа: {resp.status_code}")
                print(resp.json())

            elif choice == "4":
                b_id = input("ID книги для замены: ")
                title = input("Новое название: ")
                author = input("Новый автор: ")
                year = int(input("Новый год: "))
                genre = input("Новый жанр: ")
                price = float(input("Новая цена: "))

                payload = {"title": title, "author": author, "year": year, "genre": genre, "price": price}
                resp = requests.put(f"{BASE_URL}/books/{b_id}", json=payload)
                print(f"\nКод ответа: {resp.status_code}")
                print(resp.json())

            elif choice == "5":
                b_id = input("ID книги для изменения: ")
                price = input("Новая цена (оставьте пустым для пропуска): ")
                payload = {}
                if price:
                    payload["price"] = float(price)

                resp = requests.patch(f"{BASE_URL}/books/{b_id}", json=payload)
                print(f"\nКод ответа: {resp.status_code}")
                print(resp.json())

            elif choice == "6":
                b_id = input("ID книги для удаления: ")
                resp = requests.delete(f"{BASE_URL}/books/{b_id}")
                print(f"\nКод ответа: {resp.status_code}")
                if resp.status_code == 204:
                    print("Успешно удалено (204 No Content)")
                else:
                    print(resp.json())

            elif choice == "7":
                genre = input("Введите жанр для фильтрации: ")
                resp = requests.get(f"{BASE_URL}/books", params={"genre": genre})
                print(f"\nКод ответа: {resp.status_code}")
                print(resp.json())

            elif choice == "8":
                sort_field = input("Сортировать по (price/year): ")
                order = input("Порядок (asc/desc): ")
                resp = requests.get(f"{BASE_URL}/books", params={"sort": sort_field, "order": order})
                print(f"\nКод ответа: {resp.status_code}")
                print(resp.json())

            elif choice == "9":
                author = input("Введите имя автора для поиска: ")
                resp = requests.get(f"{BASE_URL}/books/by-author", params={"name": author})
                print(f"\nКод ответа: {resp.status_code}")
                print(resp.json())

            elif choice == "0":
                print("Завершение работы клиента.")
                break
        except Exception as e:
            print(f"Ошибка запроса: {e}")


if __name__ == "__main__":
    main()