## Директории
1) В домашней директории создать папку `linux`
2) В директории `linux` создать директорию `films`
3) В директории `films` создать директории `western`, `action`, `drama`, `comedy`
4) Перейти в директорию `western`
5) Не выходя из директории `western` создать в директории action файлы `JohnWick`, `Gentlemen` и директорию `FastFurious`
6) Не выходя из директории western создать в директории `drama` файлы `Intouchables`, `TheGreenMile`, `Hachi`
7) Перейти в директорию `films`
8) В директории `comedy` создать директории `movies` и `TVseries`
9) В директории `movies` создать файлы `HomeAlone`, `TheMask`
10) В директории `TVseries` создать файлы `Friends`, `MiracleWorkers`, `TheOffice`
11) В директории `linux` создать директорию `films_archive`
12) Скопировать *содержимое* директории `films` в `films_archive`
13) Переименовать директорию `films_archive/western` в `films_archive/westernCopy`
## Файлы
1) В директории `linux` создать директорию `text_processing` и перейти в нее
2) Создать файл `info.csv` с таким содержимым
```csv
Name:Company:Price:Ganre:Multiplayer
Item1:Company1:60000$:Ganre1:Yes
Item2:Company2:70000$:Ganre2:Yes
Item3:Company3:90000$:Ganre1:Yes
Item4:Company4:90000$:Ganre1:No
Item5:Company5:110000$:Ganre1:Yes
Item6:Company6:410000$:Ganre2:Yes
Item7:Company1:60000$:Ganre1:Yes
Item8:Company4:40000$:Ganre2:No
Item9:Company3:90000$:Ganre1:Yes
```
3) В файле `info.csv` найти строки, которые содержат слово `No`
4) В файле `info.csv` найти все строки, в которых встречается слово `Ganre2`
5) В файле `info.csv` найти все строки, в которых встречается слово `Ganre2` и вывести только 3 поле
4) Создать файл `metrics` с содержимым
```txt
metric_name:metric_type:interval
cache_disk_use:gauge:1
cache_use:gauge:0
key_buffer_bytes_used:byte:3
table.rows.read:count:10
disk_use:gauge:10
data_size:gauge:1
rows_deleted:count:1
bytes_received:byte:1
```
6) В файле `metrics` найти все строки, в которых встречается слово `gauge` и вывести только первое поле
7) В файле `metrics` найти все строки, в которых встречается слово `byte` и вывести только 3 поле
8) В файле `metrics` найти все строки, в которых встречается слово `disk` и вывести только 2 поле
9)  В файле `metrics` найти все строки, которые *начинаются* с `cache`
10)  В файле `info.csv` найти все строки, которые содержат слово `Company4`
11) Вывести список имен пользователей из файла `/etc/passwd`
12) В директории text_proxessing создать файл `logs.log` с содержимым
```
2024-10-27 08:15:23 INFO [Server] Application started successfully
2024-10-27 08:17:45 DEBUG [UserService] User login attempt: john_doe@example.com
2024-10-27 08:17:46 INFO [UserService] User john_doe@example.com logged in successfully
2024-10-27 08:20:12 WARN [DatabaseService] High database load detected
2024-10-27 08:22:30 ERROR [PaymentService] Transaction failed for user: alice@example.com
2024-10-27 08:22:31 INFO [PaymentService] Retrying transaction for alice@example.com
2024-10-27 08:22:32 INFO [PaymentService] Transaction successful for alice@example.com
2024-10-27 08:25:00 DEBUG [CacheService] Cache hit ratio: 0.75
2024-10-27 08:35:15 INFO [BackupService] Daily backup started
2024-10-27 08:35:22 ERROR [NetworkService] Connection timeout: 192.168.1.105
2024-10-27 08:35:25 WARN [NetworkService] Retrying connection to 192.168.1.105
2024-10-27 08:35:30 INFO [NetworkService] Connection established with 192.168.1.105
2024-10-27 08:40:00 DEBUG [MemoryManager] Current memory usage: 2.5GB
2024-10-27 08:45:12 INFO [UpdateService] Checking for system updates
2024-10-27 08:45:15 INFO [UpdateService] No new updates available
2024-10-27 08:50:30 WARN [SecurityService] Multiple failed login attempts for user: eve@example.com
2024-10-27 08:50:35 ERROR [SecurityService] Account locked: eve@example.com
2024-10-27 08:55:00 INFO [MonitoringService] All systems operating normally
2024-10-27 09:00:00 INFO [SchedulerService] Running hourly tasks
2024-10-27 09:05:23 DEBUG [APIService] API request received from 10.0.0.15
2024-10-27 09:05:24 ERROR [APIService] Invalid API key from 10.0.0.15
2024-10-27 09:10:00 INFO [LoadBalancer] Traffic distribution: Server1: 40%, Server2: 35%, Server3: 25%
2024-10-27 09:15:30 WARN [DiskService] Low disk space on /dev/sda1: 85% used
2024-10-27 09:20:00 INFO [BackupService] Daily backup completed successfully
2024-10-27 09:25:45 DEBUG [CacheService] Cache invalidation triggered
2024-10-27 09:30:00 INFO [ReportGenerator] Monthly report generation started
```
13) Найти в файле `logs.log` строки, содержащие ERROR и вывести к какому сервису они относятся (название сервиса записано в квадратных скобках)
14) Найти в файле `logs.log` строки, содержащие `PaymentService` и вывести из этих строк только email
15) Найти в файле `logs.log` записи о запросах к `APIService`, найти `ERROR` и вывести ip-адрес
16) Найти в файле `logs.log` записи о backup и вывести время, когда бэкап запустился и когда завершился
17) Из вывода команды `df -Th` получить файловые системы с типом ext4
18) Из вывода команды `free -h` получить только столбец available
19) Из вывода команды `lsmem` получить значение Memory block size
20) Из вывода команды `lscpu` получить значение Vendor ID
21) Получить из вывода команды `uptime` _значения_ load-average
22) Получить из вывода команды `lscpu` количество ядер
23) Из вывода команды `env` получить значения SHELL, PWD и USER
24) Выполнить `sudo netstat -tulpn` и отфильтровать вывод по ssh (если netstat не сработал, то использовать `sudo ss -tulpn`)
25) Удалить все комментарии (строки, начинающиеся с #) из файла `/etc/ssh/sshd_config`
26) Извлечь IPv4-адреса из вывода `ip a`