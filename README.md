
Простой проект для практики, в нём будет

Django
React (хотя там и typescript проскальзывает)

в Django будет
- одна вьюшка, может две, подумаю
- один сокет какой-нибудь, может чат полноценный сделаю
- авторизация скорее всего

В React будет чат на сокетах
- история сообщений
- непрочитанные сообщения
- уведомления
- ещё подумаю что сделать

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

В данное время нахожусь на этапе автоматического деплоя на сервер, 
уже почти сделано, остались последние две строчки,
потому что пуш идёт, а куда именно образы ложатся - хз
работаю крч

после думаю займусь кастомизацией и статик файлы заведу

----------------------------------------------------------

- Запуск очень прост

`docker compose up -d build`

или

`docker compose -f docker-compose.yml -f docker-compose.override.yml up -d build`

- Вырубить всё также просто

`docker compose down`

или

`docker compose -f docker-compose.yml -f docker-compose.override.yml down -v`

- Запуск для прода

`docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d build`

выключение в проде

`docker compose -f docker-compose.yml -f docker-compose.prod.yml down`
