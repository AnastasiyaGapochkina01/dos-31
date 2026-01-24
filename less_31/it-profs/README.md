# IT Professions Web App
Приложение на FastAPI, демонстрирующее IT-профессии через интерактивные плитки.

Главная страница — 6 анимированных плиток (DevOps, Backend, Frontend, PM, Design, QA).
Каждая открывает страницу с описанием профессии

<img width="1290" height="741" alt="image" src="https://github.com/user-attachments/assets/d19f0160-e535-4189-8f6f-34f9b6addf68" />

<img width="1435" height="569" alt="image" src="https://github.com/user-attachments/assets/afd7a672-8a5c-4d69-a3dd-67fb355c62d3" />


## Запуск
#### 1. Клонировать/создать структуру
```bash
mkdir it-professions && cd it-professions
mkdir templates static
```
#### 2. Установить зависимости
```bash
python3 -m pip3 install fastapi jinja2 uvicorn
```
#### 3. Запустить
```bash
python3 main.py
```
ИЛИ
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
