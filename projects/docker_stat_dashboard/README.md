# dos-29-diplomas-projects
## Docker Dashboard
Веб-приложение для мониторинга и управления Docker контейнерами с возможностью генерации отчетов и отправки их через Telegram.

### Функционал
1) Аутентификация пользователей: регистрация и вход в систему
2) Просмотр Docker контейнеров: отображение всех контейнеров на хосте
3) Визуализация статусов: цветные индикаторы статусов контейнеров (запущен, остановлен, на паузе)
4) Детальная информация: просмотр подробных данных о каждом контейнере
5) Генерация отчетов: создание PDF-отчетов о контейнерах
6) Telegram интеграция: отправка отчетов через Telegram бота
7) Дашборд автоматически обновляется при изменении состояния контейнеров

### Технологический стек
- Backend: Golang
- Frontend: HTML, CSS, JavaScript
- База данных: PostgreSQL
- Очередь сообщений: RabbitMQ
- Интеграция: Telegram Bot API

#### Предварительные требования
1) Telegram бот (получить токен можно через @BotFather)
2) Telegram ID пользователя (можно получить через @userinfobot)

#### Структура таблицы users
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    telegram_id VARCHAR(50)
);
```
### API endpoints
- GET / - Главная страница
- GET /login - Страница входа
- POST /login - Аутентификация пользователя
- GET /register - Страница регистрации
- POST /register - Создание нового пользователя
- GET /dashboard - Дашборд с контейнерами
- GET /container/:id - Страница контейнера
- POST /report - Генерация отчета
- GET /events - Server-Sent Events для обновлений
- GET /logout - Выход из системы
