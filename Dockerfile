# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Устанавливаем точку входа для контейнера
ENTRYPOINT ["python", "bot.py"]
