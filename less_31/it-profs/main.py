from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Профессии IT")

# Подключаем папки для шаблонов и статики
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Данные о профессиях
PROFESSIONS = {
    "devops": {
        "title": "DevOps Инженер",
        "description": "DevOps инженер занимается автоматизацией процессов разработки, развертывания и эксплуатации приложений. Использует инструменты CI/CD, контейнеризацию (Docker, Kubernetes), инфраструктуру как код (Terraform, Ansible) и мониторинг (Prometheus, Grafana)."
    },
    "backend": {
        "title": "Backend Разработчик",
        "description": "Backend разработчик создает серверную логику приложений. Работает с базами данных (PostgreSQL, MongoDB), API (REST, GraphQL), фреймворками (FastAPI, Django, Spring) и микросервисами."
    },
    "frontend": {
        "title": "Frontend Разработчик",
        "description": "Frontend разработчик отвечает за пользовательский интерфейс. Использует HTML, CSS, JavaScript, фреймворки React, Vue.js, Angular и инструменты сборки Webpack, Vite."
    },
    "pm": {
        "title": "Project Manager",
        "description": "Project Manager управляет проектами разработки ПО. Координирует команды, планирует сроки, управляет рисками, использует методологии Agile, Scrum, Kanban и инструменты Jira, Trello."
    },
    "design": {
        "title": "UI/UX Designer",
        "description": "Дизайнер создает удобные и красивые интерфейсы. Работает в Figma, Sketch, Adobe XD, проводит исследования пользователей, создает прототипы и дизайн-системы."
    },
    "qa": {
        "title": "QA Инженер",
        "description": "QA инженер тестирует ПО на качество. Пишет автотесты (Selenium, Pytest), проводит ручное тестирование, работает с баг-трекерами и обеспечивает покрытие тестами."
    }
}

@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@app.get("/profession/{prof_key}", response_class=HTMLResponse)
async def profession_page(request: Request, prof_key: str):
    if prof_key not in PROFESSIONS:
        return templates.TemplateResponse("404.html", {"request": request})
    
    profession = PROFESSIONS[prof_key]
    return templates.TemplateResponse("profession.html", {
        "request": request, 
        "profession": profession,
        "prof_key": prof_key
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

