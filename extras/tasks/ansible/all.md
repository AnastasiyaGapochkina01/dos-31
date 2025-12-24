1) Написать плейбук, который создает системного пользователя с именем appuser с домашней директорией (`/home/appuser`) и оболочкой /bin/bash
2) Написать плейбук, который копирует публичный SSH-ключ с управляющей машины (`files/appuser.pub`) в файл `authorized_keys` пользователя `appuser` на удаленных узлах (`/home/appuser/.ssh/authorized_keys`).
Убедиться, что у директории `.ssh` правильные права (`700`), а у файла `authorized_keys` - права (`600`).
3) Написать плейбук, который копирует шаблон файла `mod` с управляющей машины (`templates/motd.j2`) на удаленные узлы в `/etc/motd`. Использовать переменную `{{ inventory_hostname }}` в шаблоне, чтобы в файле motd отображалось имя хоста.
Шаблон (`templates/motd.j2`)
```j2
Welcome to server {{ inventory_hostname }}!
Provided by Ansible.
```
4) Написать плейбук, который проверит, установлен ли `git` на удаленных узлах и склонирует репозиторий https://gitlab.com/devops201206/it-mtb-blog в директорию `/var/www/simple-blog`
5) Написать плейбук для сбора системной информации об управляемых узлах
- размер оперативной памяти
- размер диска, смонтированного в `/`
- версия ОС
6) Написать роль (роли?) для развертывания приложения https://gitlab.com/devops201206/visits НЕ в docker
7) Написать роль для установки node-exporter НЕ в docker
8) Написать роль для настройки времени и часового пояса с помощью chrony или ntpd
9) Написать роль для установки и настройки auditd; роль должна включать
- настройку основного конфигурационного файла /etc/audit/auditd.conf через шаблон Jinja2
  - log_file
  - max_log_file
  - num_logs
  - space_left_action
  - admin_space_left
- управление правилами аудита: размещение правил в /etc/audit/rules.d/security.rules с помощью шаблона и переменных
```yaml
auditd_rules:
  - "-a always,exit -F arch=b64 -S open,openat -F success=1"
  - "-w /etc/passwd -p wa -k identity"
  - "-w /etc/sudoers -p wa -k scope"
```
10) Написать роль `logrotate_config`, которая генерирует конфиг для демона `logrotate` на основе переменных
- logrotate_paths
- rotate_count

Роль должна перед применением конфига проверять его с помощью `logrotate -dv /etc/logrotate.d/your_config_file` и перезапускать демон через handler

11) Зашифровать с помощью ansible vault переменные
```yaml
api_token: "s3cr3t_t0k3n"
api_user: ecom
```
Написать плейбук, который на основе этих переменных генерирует файл `/opt/app/.env` с правами `0600` и содержимым вида
```ini
APP_TOKEN={{ api_token }}
API_USER={{ api_user }}
ENVIRONMENT=production
```
12) _Опциональная задача_

Для плейбука из задачи №2 инициализировать структуру molecule для тестирования и прогнать базовые тесты

4) Написать роль `sys_utils_manager`, которая устанавливает инструменты
- мониторинга: atop, iotop
- сетевые: nmap, tcpdump, mtr
- отладочные: strace

Роль должна использовать теги
- monitoring - для установки утилит мониторинга
- network - для установки сетевых утилит
- debug - для установки отладочных утилит
- config_atop - для настройки утилиты atop -> изменение времени сбора метрик с 10 минут на значение, указанное в переменной `atop_time`