def test_add_item(json_storage, vacancy_data):
    json_storage.add_item(vacancy_data)
    assert len(json_storage.get_items()) == 1


def test_add_duplicate_item(json_storage, vacancy_data):
    json_storage.add_item(vacancy_data)  # Добавляем элемент первый раз
    json_storage.add_item(vacancy_data)  # Добавляем тот же элемент второй раз
    assert len(json_storage.get_items()) == 1  # Дубликаты не должны добавляться


def test_get_items(json_storage, vacancy_data):
    json_storage.add_item(vacancy_data)
    items = json_storage.get_items(title="Python Developer")
    assert len(items) == 1


def test_delete_item(json_storage, vacancy_data):
    json_storage.add_item(vacancy_data)
    json_storage.delete_item(vacancy_data.url)  # Удаляем элемент по URL
    assert len(json_storage.get_items()) == 0  # Проверяем, что список пуст
