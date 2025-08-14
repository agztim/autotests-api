import socket


def run_client():
    # Создаем TCP сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Подключаемся к серверу
        server_address = ('localhost', 12345)
        client_socket.connect(server_address)

        # Отправляем сообщение серверу
        message = "Привет, сервер!"
        client_socket.send(message.encode())

        # Получаем ответ от сервера
        response = client_socket.recv(1024).decode()
        print("Ответ от сервера:")
        print(response)

    except ConnectionRefusedError:
        print("Не удалось подключиться к серверу. Убедитесь, что сервер запущен.")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        # Закрываем соединение
        client_socket.close()


if __name__ == '__main__':
    run_client()