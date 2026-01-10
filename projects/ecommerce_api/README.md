# dos-29-diplomas-projects
## Ecommerce API
Простой API для управления товарами интернет-магазина с использованием Go, PostgreSQL и Docker.

### Функции
- **CRUD для товаров/пользователей/заказов**
- **Метрики:**
    - product_count
    - request_count
    - uptime_sec

### Эндпоинты
- `GET|POST|PUT|DELETE /products`
- `GET|POST|PUT|DELETE /customers`
- `GET|POST|PUT|DELETE /orders`
- `GET /metrics`

### Примеры запросов
```bash
# создать товар
curl -X POST http://localhost:8080/products -H "Content-Type: application/json" -d '{"name":"Laptop","price":123.45}'

# создать пользователя
curl -X POST http://localhost:8080/customers -H "Content-Type: application/json" -d '{"name":"Vasya","email":"vasya@example.com"}'

# создать заказ
curl -X POST http://localhost:8080/orders -H "Content-Type: application/json" -d '{"customer_id":1,"product_id":2,"quantity":5}'

# получить метрики
curl -X GET http://localhost:8080/metrics

# получить заказы
curl -X GET http://localhost:8080/orders

# получить товары
curl -X GET http://localhost:8080/products
```