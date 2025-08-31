import httpx    # Импортируем библиотеку HTTPX

# URL базовый для API
BASE_URL = "http://localhost:8000"

# JSON-данные, которые будем отправлять в API
payload = {
    "email": "agztim88@gmail.com",
    "password": "password"
}

# Выполняем POST-запрос к эндпоинту /api/v1/authentication/login
response = httpx.post(f"{BASE_URL}/api/v1/authentication/login", json=payload)

# Выводим JSON-ответ и статус-код
print(f"Статус код POST-запроса: {response.status_code}")
print("JSON-ответ с данными пользователя:")
print(response.json())

# Извлекаем accessToken из ответа
login_data = response.json()
access_token = login_data['token']['accessToken']

# Выполняем GET-запрос с использованием токена
headers = {"Authorization": f"Bearer {access_token}"}

# Выполняем GET-запрос к эндпоинту /api/v1/users/me
user_response = httpx.get(f"{BASE_URL}/api/v1/users/me", headers=headers)

# Выводим JSON-ответ и статус-код
print(f"Статус код GET-запроса: {user_response.status_code}")
print("JSON-ответ с данными пользователя:")
print(user_response.json())
