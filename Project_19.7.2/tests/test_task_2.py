from api import PetFriends
from settings import valid_email, not_valid_email, valid_password, test_password_1
import os

pf = PetFriends()

# Test 1
def test_add_new_pet_without_photo(name='Громопётр', animal_type='Котан', age='29'):
    """Проверяем что можно добавить питомца с корректными данными, но БЕЗ фото"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

# Test 2
def test_add_photo_for_pet(pet_photo='images/cat1.jpg'):
    """Проверяем что можно добавить или изменить фото первому в списке питомцу"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и меняем фото
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.add_photo_for_pet(auth_key, pet_id, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert 'jpg' in pet_photo

# Test 3
def test_add_new_pet_with_un_normal_name(name='WWWW@@@@@#####!??ЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯ___ЙЙЙЙЙ?????))))', animal_type='Котан',
                                         age='29', pet_photo='images/cat.jpg'):
    """Проверяем что можно добавить питомца с не корректным и чрезмерно длинным именем"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

# Test 4
def test_add_new_pet_with_un_normal_age(name='Petr', animal_type='Котан',
                                         age='399', pet_photo='images/cat.jpg'):
    """Проверяем что можно добавить питомца с не корректным возрастом"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['age'] == age

# Test 5
def test_add_new_pet_with_un_normal_animal_type(name='Spyke', animal_type='$#&!?',
                                         age='9', pet_photo='images/cat.jpg'):
    """Проверяем возможность добавления питомца с не корректным типом"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['age'] == age

# Test 6
def test_get_api_key_for_not_valid_user(email=not_valid_email, password=test_password_1):
    """ Проверяем возможность получения api ключа с not_valid_email и с not_valid_password"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status != 200
    assert 'key' not in result

# Test 7
def test_add_new_pet_with_photo_8k(name='Petr', animal_type='Shpik',
                                         age='19', pet_photo='images/cat_8k.jpg'):
    """Проверяем что можно добавить питомца с корректным длинными и фото в 8к"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert 'jpg' in pet_photo

# Test 8
def test_add_new_pet_with_space_in_param(name=' ', animal_type=' ', age=' '):
    """Проверяем что можно добавить питомца с пустыми полями и без фото"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

# Test 9
def test_change_correct_name_and_type_pet_to_empty_value(name=' ', animal_type=' ', age=11):
    """Проверяем возможность обновления имени и типа питомца на пробелы"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

# Test 10
def test_add_new_pet_with_str_in_age_instead_int(name='Зорька', animal_type='котя',
                                     age='десять', pet_photo='images/cat1.jpg'):
    """Проверяем возможность добавления типа данных str в параметр age"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['age'] == age
