import pytest
from YougileApi import YougileApi

# Данные для подключения
BASE_URL = "https://ru.yougile.com/api-v2"
LOGIN = ""
PASSWORD = ""
COMPANY_ID = ""

api = YougileApi(BASE_URL)


# получение токена
def test_get_token():
    token = api.get_token(LOGIN, PASSWORD, COMPANY_ID)

    # проверка, что токен не пустой
    assert token is not None
    assert len(token) > 0
    print(f"Токен получен: {token[:20]}...")


# Тест: создание нового проекта
def test_create_project():
    token = api.get_token(LOGIN, PASSWORD, COMPANY_ID)
    project_title = "Тестовый проект Гульназ"
    result = api.create_project(project_title, token)
    assert "id" in result
    print(f"Создан проект с ID: {result['id']}")


# Тест: получение проекта по ID
def test_get_project_by_id():
    token = api.get_token(LOGIN, PASSWORD, COMPANY_ID)
    create_result = api.create_project("Проект для проверки получения", token)
    project_id = create_result["id"]
    print(f"Создан проект с ID: {project_id}")

    project = api.get_project(project_id, token)
    print(f"Проект получен: {project}")

    assert project["title"] == "Проект для проверки получения"
    print("Название совпадает")

    assert project["id"] == project_id
    print("ID совпадает")


# Тест: обновление названия проекта
def test_update_project():
    token = api.get_token(LOGIN, PASSWORD, COMPANY_ID)
    create_result = api.create_project("Проект для обновления", token)
    project_id = create_result["id"]
    print(f"Создан проект с ID: {project_id}, название: 'Проект для обновления'")

    new_title = "Обновленное название проекта"
    api.update_project(project_id, new_title, token)
    print("Отправлен запрос на обновление")

    updated_project = api.get_project(project_id, token)
    assert updated_project["title"] == new_title
    print(f"Название обновлено на: '{updated_project['title']}'")


# Негативный тест: создание проекта без названия
def test_create_project_negative_no_title():
    token = api.get_token(LOGIN, PASSWORD, COMPANY_ID)
    result = api.create_project("", token)
    print(f"Ответ сервера: {result}")

    assert "id" not in result
    print("Ошибка при создании без названия")


# Негативный тест: получение проекта с несуществующим ID
def test_get_project_negative_wrong_id():
    token = api.get_token(LOGIN, PASSWORD, COMPANY_ID)

    fake_id = "00000000-0000-0000-0000-000000000000"
    result = api.get_project(fake_id, token)
    print(f"Ответ сервера: {result}")

    assert "id" not in result
    print("Ошибка при получении несуществующего проекта")


# Негативный тест: обновление несуществующего проекта
def test_update_project_negative_wrong_id():
    token = api.get_token(LOGIN, PASSWORD, COMPANY_ID)

    fake_id = "00000000-0000-0000-0000-000000000000"
    result = api.update_project(fake_id, "Новое название", token)
    print(f"Ответ сервера: {result}")

    assert "id" not in result
    print("Ошибка при обновлении несуществующего проекта")
