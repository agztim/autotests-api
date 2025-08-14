import socket


def run_server():
    # Создаем TCP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем сокет к адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Начинаем слушать подключения (максимум 10 в очереди)
    server_socket.listen(10)
    print("Сервер запущен и ожидает подключений на localhost:12345")

    # Список для хранения истории сообщений
    message_history = []

    while True:
        try:
            # Принимаем новое подключение
            client_socket, client_address = server_socket.accept()
            print(f"Пользователь с адресом: {client_address} подключился к серверу")

            # Получаем сообщение от клиента
            data = client_socket.recv(1024).decode()
            if data:
                print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")
                # Добавляем сообщение в историю
                message_history.append(data)

                # Отправляем клиенту всю историю сообщений
                response = '\n'.join(message_history)
                client_socket.send(response.encode())

            # Закрываем соединение с клиентом
            client_socket.close()

        except KeyboardInterrupt:
            print("Сервер остановлен")
            break
        except Exception as e:
            print(f"Ошибка: {e}")
            continue


if __name__ == '__main__':
    run_server()