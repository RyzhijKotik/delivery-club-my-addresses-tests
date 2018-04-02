# delivery-club-my-addresses-tests

Задача:
Покрыть необходимыми тестами блок "Мои адреса" в профиле пользователя по адресу https://www.delivery-club.ru/profile/.
Использовать Python версии 3.5+ и стандратный биндинг для Selenium - https://pypi.python.org/pypi/selenium.
В качестве тестраннера желательно использовать pytest - https://docs.pytest.org/en/latest/.

requirements:
python > 3.5
selenium
pytest
pytest-selenium

Запускаем pytest'ом, при запуске передаём ключ --driver:
pytest .\tests --driver Chrome

Структура проекта:

test_my_address.py -- тесты;

conftest.py -- вспомогательные фикстуры (залогиниться, перейти в профиль, передать список данных для поля адресов);

common_data.py -- логин, пароль для аккаунта, данные для заполнения поля;

page_object -- xpath'ы элементов используемых в тестах страниц;


Два теста будут фейлиться.
1) test_add_and_delete_address
Этот тест будет падать, потому что добавленный адрес не удаляется.
    1) добавляем любой адрес, который добавится (с номером дома)
    2) жмем конпку удалить, подтверждаем удаление
    3) жмем f5
    результат: адрес остался на месте
Скринкаст: https://cloud.mail.ru/public/9osa/JLdJPNSDA

2) test_submit_unprecise_address_from_list -- будет работать только, пока в профиле нет такого адреса
    При наличии уже добавленного адреса я не могу добавить ещё один,
    если он начинается на те же буквы, что и добавленный.
    Представим, что список адресов у нас изначально пустой.
    1) Вводим в поле адреса "заг"
    2) Добавляем любой адрес из списка на "заг": например Санкт-Петербург, Загребский проезд, 9
    3) Снова вводим в поле адреса "заг"
    Результат: список адресов на "заг" мне больше не выдаётся
Скринкаст: https://cloud.mail.ru/public/Dpuk/DKEZTAfE1

3) Тест добавления на карту дефолтного адреса -- алерт-подсказка то есть, то нет.
    1) в поле ввода адреса кликаем на иконку карты
    2) ждём, пока нас автоматом перекинет на дефолтный адрес (местоположение или центр Москвы)
    Результат: иногда возникает алерт-подсказка, а иногда -- сразу кнопка "Адрес верный", без всякого алерта

Вот скринкаст двух последовательноых абсолютно одинаковых запусков. На первом подсказка есть, на втором нет:
https://cloud.mail.ru/public/5mnj/zB4dxBBHm
(я это смотрела руками и ждала пару минут -- не не успевает появиться, действительно нет)
