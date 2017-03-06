# 8marta
ladies_bar

Вдохновившись идеей https://habrahabr.ru/post/172243/ Бара желаний,
сделали аналогичный проект на работе.
Проект полностью рабочий и законченный.

-- Развертка на ubuntu
```bash
sudo apt-get install virtualenv
virtualenv --no-site-packages --python=python3 --prompt='[8m]' env
source env/bin/activate
pip install -r 'requirements.txt'
```

-- Создайте суперпользователя для редактирования базы
```bash
./manage.py createsuperuser --username admin
```

-- Разворачиваем структуру базы
```bash
./manage.py migrate
```

--- Запуск на тестовом вэб сервере
```bash
./manage.py runserver
```
