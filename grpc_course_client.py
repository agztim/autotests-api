import grpc # Импорт библиотеки gRPC

import course_service_pb2  # Сгенерированные классы для работы с gRPC-сообщениями
import course_service_pb2_grpc  # Сгенерированный класс для работы с сервисом

def run():
    # Устанавливаем соединение с сервером
    channel = grpc.insecure_channel('localhost:50051')
    stub = course_service_pb2_grpc.CourseServiceStub(channel)

    # Формируем и отправляем запрос
    request = course_service_pb2.GetCourseRequest(course_id="api-course")
    response = stub.GetCourse(request)

    # Выводим полный ответ
    print("Получен ответ от сервера:")
    print(f"course_id: {response.course_id}")
    print(f"title: {response.title}")
    print(f"description: {response.description}")

if __name__ == "__main__":
    run()