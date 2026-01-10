# dos-29-diplomas-projects
## Agritech Catalog
Каталог сельскохозяйственной техники с интерфейсом для просмотра, поиска и управления оборудованием. Приложение реализовано на Node.js с использованием Express и MongoDB на серверной части и React на клиентской.

### Структура
```
├── backend/ # Backend на Node.js (Express, Mongoose)
├── frontend/ # Frontend на React
```

## Функции
- **CRUD**
- **Поиск** по названию, производителю, модели и описанию техники

## Примеры запросов
```bash
# создание техники
curl -X POST -H 'Content-Type: application/json' http://localhost:5000/api/equipment  \
-d '{
  "name": "Трактор МТЗ-82",
  "category": "Трактор",
  "manufacturer": "Беларусь",
  "model": "MTZ-82",
  "price": 1500000,
  "power": 80,
  "description": "Надёжный и мощный трактор для сельхозработ"
}'

# получить список всей техники
curl -X GET http://localhost:5000/api/equipment

# получить список техники по категории
curl -X GET http://localhost:5000/api/equipment?category=Комбайн
```