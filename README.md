# Фреймворк Django (семинары)
## Итоговая аттестация

### Задание 1
Используя фреймворк Django создайте сайт, на котором пользователи смогут
добавлять свои рецепты блюд и просматривать рецепты других пользователей.
Готовый проект необходимо сдать в виде ссылки на рабочий сайт в сети интернет и
репозитория с исходным кодом проекта.

### Решение


Устанавливаем Django:

    pip install django

Создаем проект для работы:

    django-admin startproject Final_project

Переходим в папку проекта:

    cd .\Final_project\

Создаем новое приложение в проекте:

    python manage.py startapp recipesapp

Запускаем сервер проекта:

    python manage.py runserver

Редактируем файлы:
*********
- settings.py
- urls.py
- urls.py
- views.py

Создаем модель данных, в соответствие с заданием. 
Модель данных находится в файле: 

- models.py

Применяем миграции (Физически создаем объекты на сервере БД):

    python manage.py migrate

Так же были подготовлены шаблоны для отображения формы. Файлы с шаблонами

Для более эстетичного восприятия был добавлен [bootstrap](https://getbootstrap.com/)


Так же - создаем папку для хранения изображений, и указываем ее в настройках settins.py
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'website/media'

В файле *urls.py* указываем маршруты к новой форме редактирования рецепта, и к папке, в которой хранятся изображения 

Разрабатываем представление для формы создания/редактирования рецепта forms.py

Разрабатываем шаблон для отображения формы создания/редактирования рецепта: recipe_detail.html

В файле *views.py* описываем логику работы представления

Прописываем маршрут и класс для отображения формы в файле *urls.py*

Создаем пользователя - администратора нашего проекта

    python manage.py createsuperuser
    

    (venv) PS C:\Users\user\Downloads\Education\final_work\Final_project> python manage.py createsuperuser
    Имя пользователя: superadmin
    Адрес электронной почты: baranov.mihail@mail.ru
    Password:
    Password (again):
    Введённый пароль слишком широко распространён.
    Введённый пароль состоит только из цифр.
    Bypass password validation and create user anyway? [y/N]: y
    Superuser created successfully.

Делаем соответствующие настройки для панели администрирования в файле *admin.py*

Заходим в панель управления, вводим заданный ранее пароль.

Далее можно управлять данными, которые находятся у нас в безе.

#### Разворачивание приложения на сервере в интернете

Регистрируемся на площадке [https://www.pythonanywhere.com/](https://www.pythonanywhere.com/).

Создаем базу данных MySQL, устанавливаем кодировку в консоли mysql
    
    ALTER DATABASE zisson$default CHARACTER SET utf8 COLLATE utf8_general_ci;

После внесения настроек (удаление настроек, связанных с отладкой), загружаем готовую версию проекта на GitHub/

В консоли *pythonanywhere.com* клонируем проект

    git clone https://github.com/Baranovms/Final_project.git

Создаем виртуальное окружение

    mkvirtualenv --python=/usr/bin/python3.10 virtualenv

Устанавливаем необходимые пакеты:

    cd Final_project
    pip install -r requirements.txt

Делаем необходимые настройки в панели управления сайтом, делаем миграцию базы данных.

## Результат работы:

Проект сделан с возможностью авторизации пользователей. Причем неавторизованный пользователь может увидеть только
рецепты, а если пользователь авторизуется, то тогда он сможет добавлять, редактировать и удалять свои рецепты.
Администратор сайта может редактировать и удалять любые рецепты.


Сайт расположен по адресу: [https://zisson.pythonanywhere.com/](https://zisson.pythonanywhere.com/)
