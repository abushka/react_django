Простой проект для практики, в нём будет

Django
React (хотя там и typescript проскальзывает)

в Django будет
- одна вьюшка, может две, подумаю
- один сокет какой-нибудь, может чат полноценный сделаю

БД - postgresql

Всё это дело в docker compose естественно

Локально React должен использовать npm start, а Django runserver
Для прода React должен использовать pm2 или serve, в Django gunicorn

Статические файлы Django будет где угодно, но не в джанге

Для прода подключить Nginx - будет адресовать на три точки
- Django
- React
- Статические файлы

На гитхабе настрою пайплайны
Автоматический деплой на сервере
В композе добавить таск на генерацию сертификата для Nginx