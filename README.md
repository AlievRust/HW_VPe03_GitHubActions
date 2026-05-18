# FastAPI Server Time Backend

Простой тестовый бэкэнд на FastAPI.

## Запуск

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Эндпоинты

- `GET /` - статус и текущее время сервера
- `GET /time` - только текущее время сервера
- `GET /date` - только текущая дата сервера
