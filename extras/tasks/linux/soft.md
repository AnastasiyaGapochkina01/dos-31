1) Установить
- `mc`
- `apache2`
2) Установить `docker` по официальной инструкции
3) Удалить `apache2` с удалением всех зависимостей и конфигов
4) Проверить, установлены ли на ВМ пакеты python3-pip и python3-venv. Если нет, то установить их
5) Установить пакет `build-essential`
6) Установить Node.js v22 по официальной инструкции
7) Установить из [deb-пакета ](https://github.com/sharkdp/bat/releases/download/v0.25.0/bat_0.25.0_amd64.deb) утилиту `bat` - аналог `cat`, но она выводит на экран текст 
с подсветкой синтаксиса и если текст не влезает в экран, то использует интерактивный режим с возможностью прокрутки страницы
Установить [mongodb](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/)
8) Установить [percona](https://docs.percona.com/percona-server/8.0/apt-repo.html#install-percona-server-for-mysql-using-apt)
9) Установить zsh из [исходников](https://github.com/zsh-users/zsh/tree/master)
> [!WARNING]  
> да, можно просто через `apt`, но нам интереснее пощупать именно такой способ