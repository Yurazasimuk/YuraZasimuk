# Використовуємо офіційний Python-образ
FROM python:3.12

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файл скрипта до контейнера
COPY logger.py .

# Створюємо папку для логів
RUN mkdir -p /app/logs

# Запускаємо наш скрипт
CMD ["python", "logger.py"]
