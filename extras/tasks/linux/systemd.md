# Часть 1
1) Установить на ВМ php
2) В директории /opt создать папку rot13
3) В директории /opt/rot13 создать файл с именем rot13-server.php с кодом
```php
<?php
$sock = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP);
socket_bind($sock, '0.0.0.0', 10000);
for (;;) {
  socket_recvfrom($sock, $message, 1024, 0, $ip, $port);
  $reply = str_rot13($message);
  socket_sendto($sock, $reply, strlen($reply), 0, $ip, $port);
}
```
4) Запустить сервер командой php rot13-server.php и проверить что сервер работает: выполнить nc -u 127.0.0.1 10000 и ввести Hello World
5) Написать юнит-файл для запуска rot13-server.php как сервиса
6) Установить nginx, если он еще не установлен
7) Посмотреть статус демона nginx
8) Остановить nginx
9) Запустить nginx
10) Убрать nginx из автозагрузки
11) Вернуть nginx в автозагрузку
12) "Замаскировать" nginx, попробовать перезапустить/остановить/запустить nginx; снять с nginx "маскировку"
13) Установить redis ([install-redis-on-linux](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-linux/)) - ссылка доступна под VPN
14) Посмотреть статус демона redis
15) Запустить второй экземпляр демона redis, написав systemd unit

# Часть 2
Развернуть Python-веб-сервер, настроить управление через systemd, организовать логирование; проверка `curl http://localhost:8000`

Код сервера
```python
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

os.chdir("/srv/webapp/content")
server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
```

#### Требования
1) Сервер запущен как systemd демон с правами пользователя `webadmin`
2) Пользователь `webadmin` не имеет shell-доступпа и является членом группы `webgroup`
3) Код сервера расположен в директории `/opt/srv/webapp`; в той же диреткории лежит `content/index.html` с содержимым
```html
<!DOCTYPE html>
<html>
<head>
    <title>Приветствие</title>
    <style>
        .greeting {
            border: 5px solid orange; 
            padding: 20px; 
            font-size: 48px;
            text-align: center; 
            margin: 50px auto; 
            width: fit-content;
            border-radius: 15px;
            background-color: #fff8f0; 
            font-family: Arial, sans-serif;
            box-shadow: 0 0 15px rgba(255, 165, 0, 0.3); 
        }
    </style>
</head>
<body>
    <div class="greeting">Hello, DOS-31-ONL! You are amazing!</div>
</body>
</html>
```
4) Настроено логрование в syslog/rsyslog