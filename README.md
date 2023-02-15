Основной код в ветке prod

Простой чат на websockets, 
- с авторизацией (в будущем)
- с уведомлениями о новых сообщениях (вроде бы работают, надо проверить)
- видимость того, что пользователь печатает
- прокрутка чата и загрузка истории чата (paginator)
- сообщения прочитаны (надо проверить)

Используются такие технологии как
- Django
- React (хотя там typescript)
- Postgresql
- Docker, docker compose
- Nginx
- Shell
- Gunicorn
- Redis
- Github pipelines (мелкий CI/CD)
- любовь

Локально React должен использовать npm start, а Django runserver
Для прода React должен использовать pm2 или serve, а Django gunicorn

Статические файлы Django будут где угодно, но не в джанге

Для прода Nginx адресат в три точки
- Django
- React
- Статические файлы

На гитхабе пайплайны
Автоматический деплой на сервере
В композе добавить таск на генерацию сертификата для Nginx (намного легче руками конечно 
сделать, но подумаю и об автоматизации)

Осталось сделать регистрацию, баги пофиксить, существуещее проверить нормально,
дизайн получше придумать


----------------------------------------------------------

- Запуск очень прост

`docker compose up -d build`

или

`docker compose -f docker-compose.yml -f docker-compose.override.yml up -d build`

Вырубить всё также просто

`docker compose down`

или

`docker compose -f docker-compose.yml -f docker-compose.override.yml down -v`

- Запуск для прода

`docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d build`

Вырубить в проде

`docker compose -f docker-compose.yml -f docker-compose.prod.yml down`
