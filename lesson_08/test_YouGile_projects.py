import pytest
from YouGileApi import YouGileApi

YouGile = YouGileApi("https://ru.yougile.com/api-v2")


# Получить список проектов
@pytest.mark.positive
def test_get_projects():
    list_projects = YouGile.get_projects_list()
    print(list_projects)
    print("ok")


# Создать проект - позитивный
@pytest.mark.positive
def test_positive_create_project():
    # количество проектов до создания
    list_projects = YouGile.get_projects_list()
    count_before = len(list_projects)

    my_title = "New 1"
    # my_users = {}
    # роли - "worker", "admin"
    my_payload = {"title": my_title}

    created_project = YouGile.create_project(my_payload)
    assert created_project.status_code == 201
    created_id = created_project.json()["id"]  # получаем ID созданного проекта
    assert len(created_id) is not None

    # количество проектов после создания
    list_projects = YouGile.get_projects_list()
    count_after = len(list_projects)
    assert count_after - count_before == 1

    # Проверяем название и id добавленного проекта:
    assert list_projects[-1]["title"] == my_title
    assert list_projects[-1]["id"] == created_id


# Изменить проект - позитивный
@pytest.mark.positive
def test_positive_update_project():
    my_title = "New 10_for Update"
    my_payload = {"title": my_title}

    created_project = YouGile.create_project(my_payload)
    created_id = created_project.json()["id"]  # получаем ID созданного проекта

    upd_title = f"Проект {my_title} измененный"
    upd_payload = {"title": upd_title}

    response = YouGile.update_project(created_id, upd_payload)
    assert response.status_code == 200
    # найдем измененный проект по id
    updated_project = YouGile.get_project_by_id(created_id)
    assert updated_project.json()["title"] == upd_title
    # проверим, что id проекта не изменился
    assert updated_project.json()["id"] == created_id


# Получить проект по ID - позитивный
@pytest.mark.positive
def test_positive_get_project_by_id():
    my_title = "New for GET"
    my_payload = {"title": my_title}

    created_project = YouGile.create_project(my_payload)
    created_id = created_project.json()["id"]  # получаем ID созданного проекта
    assert created_project.status_code == 201
    get_project = YouGile.get_project_by_id(created_id)
    assert get_project.json()["title"] == my_title
    # проверим, что id проекта не изменился
    assert get_project.json()["id"] == created_id


# Создать проект - негативный
@pytest.mark.negative
def test_negative_create_project():
    my_title = ""
    my_payload = {"title": my_title}

    created_project = YouGile.create_project(my_payload)
    assert created_project.status_code == 400


# Изменить проект - негативный
def test_negative_update_project():
    my_title = "New 10_for Update"
    my_payload = {"title": my_title}

    created_project = YouGile.create_project(my_payload)
    created_id = created_project.json()["id"]  # получаем ID созданного проекта
    response = YouGile.update_project(created_id, "")
    assert response.status_code == 400


# Получить проект по ID - негативный
@pytest.mark.negative
def test_negative_get_project_by_id():
    get_project = YouGile.get_project_by_id('123')
    assert get_project.status_code == 404
