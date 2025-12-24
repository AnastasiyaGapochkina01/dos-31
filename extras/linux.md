## 00 - Работа с git
минимальный минимум для тех, кто не юзал никогда: https://youtu.be/CLhJqZZswFo
## 01 - Введение
- общее устройство ОС семейства *Nix https://youtu.be/IyDs9ZgWcTo
- работа с командной строкой https://youtu.be/PnvG2DjFCRI
## 02 - Работа с файловой системой (beginner)
- работа с файлами https://youtu.be/IPSfoerrNig
- работа с директориями https://youtu.be/fqWjveB1Oyo
- простая обработка текста https://youtu.be/MN1vu7haaO8
- регулярные выражения https://www.youtube.com/watch?v=PBkJIRmWynM
---
[**Задания**](./tasks/linux/files.md)

## 03 - Пользователи и права доступа
- урок - https://youtu.be/cGE64MxCswo
---
[**Задания**](./tasks/linux/users.md)
## 04 - Установка ПО
- урок - https://youtu.be/2RrmMs0FP18
---
[**Задания**](./tasks/linux/soft.md)

## 05 - Процессы
- урок https://youtu.be/vWQ5KN9o70k
---
[**Задания**](./tasks/linux/processes.md)
## 06 - Работа с systemd
- урок - https://youtu.be/fmVI9Q2LavI
---
[**Задания**](./tasks/linux/systemd.md)
## 07 - bash-скрипты
урок - https://youtu.be/kEpCiCb-y1Y
---
[**Задания**](./tasks/linux/bash.md)
## 08 Работа с файловой системой (advanced)
- LVM https://youtu.be/DnUqaXJVdew
- RAID - https://youtu.be/yDqkN2ecNEU
---
[**Задания**](./tasks/linux/lvm.md)
## 09 - Запуск задач по расписанию (cron)
- урок - https://youtu.be/hTkaCE5Mz8I

## 10 - Сети
- https://youtu.be/3zCQGen6VpA
- https://youtu.be/2OljPJn3H1Q
- https://youtu.be/abmnnC4kZnI
- https://youtu.be/Bd9itUD1_aU

# Микро-проект
> [!CAUTION]
> !!! БЕЗ ДОКЕРА !!!
> Это задание для самостоятельной работы — оно не будет отмечаться в lms и выходит за рамки курса
> 
> Сроки сдачи не ограничены, разбор решений/ответы на вопросы будут, но не в ущерб основной программе
> 
> В ТЗ и readme проекта _специально_ опущены некоторые подробности, чтобы вы поизучали то, что развернули

---

## Описание задачи
Команда anestesia.tech написала приложение на python, которое представляет собой трехкомпонентную систему для логирования, тестирования и анализа веб-приложений. Репозиторий проекта находится по ссылке -> [log-analize-python](https://github.com/AnastasiyaGapochkina01/log-analize-python).
В репозитории имеется описание проекта, в тч как каждый из компонентов запускается. Вам необходимо развернуть эту систему в соответствии с требованиями:
1) Операционная система - Ubuntu 20.04+ / Debian 11+
2) Python 3.11+
3) Присутствует виртуальное окружение (python virtualenv)
4) Установлены пакеты libpq-dev build-essential
5) Корневая директория проекта - /opt/web_monitoring
6) **API-сервер (log-server.py) и дашборд запущены с помощью systemd**
7) Для запуска скрипта генерации нагрузки можно использовать
- обычный ручной запуск
- bash-скрипт (в тч однострочник) как обертка
- cron для запуска по расписанию (ставьте небольшой промежуток, чтобы проверить и не забывайте убирать после успешной отработки)
- systemd сервис типа oneshot
8) Запуск от имени пользователя www-data
9) После запуска необходимо проверить работоспособность всех компонентов

## Шпаргалка

<details>
  <summary>Установка зависимостей</summary>
  
  ```bash
  sudo -u www-data python3 -m venv /opt/web_monitoring/.venv
  sudo -u www-data /opt/web_monitoring/.venv/bin/pip install -U -r requirements.txt
  ```
  
</details>

<details>
  <summary>Запуск из systemd</summary>
  
  ```bash
  ...
  WorkingDirectory=/opt/web_monitoring
  Environment="PATH=/opt/web_monitoring/.venv/bin/"
  ExecStart=/opt/web_monitoring/.venv/bin/python3 script.py
  ...
  ```
  
</details>