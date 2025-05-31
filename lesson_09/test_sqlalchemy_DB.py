from Subject_Page import Subjects

db_connection_string = "postgresql://postgres:lqs@localhost:5432/postgres"
db_subj = Subjects(db_connection_string)


def test_get_list_subjects():
    # получить список предметов из БД:
    subjects = db_subj.get_list_subjects()
    print(subjects)


def test_add_subject():
    test_subject = "Statistics_add"
    # количество записей до добавления
    count_before = db_subj.count_subjects()
    # создаем предмет
    db_subj.insert_subject(test_subject)
    # количество записей после добавления
    count_after = db_subj.count_subjects()
    # получаем предмет из базы по наименованию
    result = db_subj.get_subject(test_subject).fetchone()
    print(result)
    # Удаляем за собой тестовые данные
    db_subj.delete_subject(test_subject)
    # Проверяем, что добавился предмет
    assert count_after == count_before + 1
    assert result is not None


def test_update_title():
    test_subject = 'Statistics_upd'
    # добавляем тестовый предмет
    db_subj.insert_subject(test_subject)
    # Меняем описание:
    new_title = 'Updated_Statistics'
    db_subj.update_subject(test_subject, new_title)
    result = db_subj.get_subject(new_title).fetchone()
    db_subj.delete_subject(new_title)
    print(result)
    # Проверяем, что изменения внесли
    assert result is not None
    assert result._data[1] == new_title


def test_delete_subject():
    test_subject = "Statistics_del"
    # добавляем тестовый предмет
    db_subj.insert_subject(test_subject)
    db_subj.delete_subject(test_subject)
    result = db_subj.get_subject(test_subject).fetchone()
    print(result)
    assert result is None
