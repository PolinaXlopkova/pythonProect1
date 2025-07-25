<div id="header" align="center">
  <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExenJmM2h2Mm82N2JxbDJ2YXdobzhpd3pkd3UyanVlNzZiZWI2dnYzZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2IudUHdI075HL02Pkk/giphy.gif" width="200"/>
</div>

## :woman_technologist: информация о проекте:
Данный проект был создан специально для изучения материала от курсов SkyPro, суть проекта: IT-отдел крупного банка хочет внедрить новую фичу для личного кабинета клиента. Фича будет отображать несколько успешных операция клиента.

---

###
<h1>
Установка
  <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWRlZTg4OGo2N3p5aGptZjkwYzVlb3U4ZTlobGE5OTQ3aXM3czVmNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XGsHjfmwF3VMCuNQA4/giphy.gif" width="70px"/>
</h1>

1. Скопируйте репозиторий:
```
https://github.com/PolinaXlopkova/pythonProect1.git
```

2. Установка зависимости:
```
poetry install
```

3. Создайте базу данных и выполните миграции:
```
python manage.py migrate
```

4. Запустите локальный сервер:
```
python manage.py runserver
```
##
<h1>
Использование:
  <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjIwbmQwOXdvMHJsM2IyMnJkZXc1bW1oeWN6a3Ztajg1d2FwcTk3ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/0weNDO7xfTye4oqkUr/giphy.gif"
width="70px"/>
</h1>  
1. Перейдите на страницу в вашем веб-браузере.
2. Создайте новую учетную запись или войдите существующей.
3. Создайте новую запись в блоге или оставьте комментарий к существующей.

---

###
<h1>
Пример использования функций:
</h1>

1. Функция get_mask_card_number:
```
 7000792289606361     # входной аргумент
 7000 79** **** 6361  # выход функции
```
                               
2. Функция get_mask_account:
```
73654108430135874305  # входной аргумент
**4305  # выход функции
```

3. Функция mask_account_card:
```
# Пример для карты
Visa Platinum 7000792289606361  # входной аргумент
Visa Platinum 7000 79** **** 6361  # выход функции
# Пример для счета
Счет 73654108430135874305  # входной аргумент
Счет **4305  # выход функции
```
4. Функция get_date:
```
print(get_date("2025-06-14T12:00:00"))  # Вывод: 14.06.2025
```
5. Функция filter_by_state:
```
# Выход функции со статусом по умолчанию 'EXECUTED'
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
# Выход функции, если вторым аргументов передано 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
6. Функция sort_by_date:
```
# Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
feature/homework_12_2
7. Функция filter_by_currency:
```
# Принимает на вход список словарей, представляющих транзакции.
```
8. Генератор transaction_descriptions:
```
* Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
```

 main
###
<h1>
Пример использования тестов:
</h1>

## Тестирование функций

В этом документе описаны функции, которые были протестированы, их назначение и результаты тестирования.

 feature/homework_12_2
### 1. mask_account_card

### 1. Функция mask_account_card
 main

*Описание:*  
Эта функция используется для маскировки номера банковской карты, заменяя все цифры, кроме последних четырех, на символы *.

*Тестовые случаи:*
- Вход: 1234567812345678  
  Ожидаемый результат: ************5678
  
- Вход: 4000123412345678  
  Ожидаемый результат: ************5678

 feature/homework_12_2
### 2. filter_by_date

### 2. Функция filter_by_date
 main

*Описание:*  
Функция фильтрует данные по заданному диапазону дат.

*Тестовые случаи:*
- Вход: data=[{'date': '2023-01-01'}, {'date': '2023-01-02'}], start_date='2023-01-01', end_date='2023-01-01'  
  Ожидаемый результат: {'date': '2023-01-01'}

- Вход: data=[{'date': '2023-01-01'}, {'date': '2023-01-02'}], start_date='2023-01-03', end_date='2023-01-04'  
  Ожидаемый результат: []

 feature/homework_12_2
### 3. get_mask_account=======
### 3. Функция get_mask_account
 main

*Описание:*  
Функция возвращает замаскированный номер счета.

*Тестовые случаи:*
- Вход: account_number='123456789'  
  Ожидаемый результат: *****6789

- Вход: account_number='987654321'  
  Ожидаемый результат: *****4321

 feature/homework_12_2
### 4. get_mask_cart_number

### 4. Функция get_mask_cart_number
 main

*Описание:*  
Функция возвращает замаскированный номер карты.

*Тестовые случаи:*
- Вход: cart_number='4111111111111111'  
  Ожидаемый результат: ************1111

- Вход: cart_number='5500000000000004'  
  Ожидаемый результат: ************0004
 feature/homework_12_2

### 5. filter_by_currency

*Описание:*
Функция предназначена для фильтрации транзакций по заданной валюте.

### 6. transaction_descriptions

*Описание:*
Функция возвращает описания для каждой транзакции.

 main
