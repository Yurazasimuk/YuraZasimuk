import logging
import os
import time
from datetime import datetime

# Шлях до папки для логів
log_dir = "/app/logs"
os.makedirs(log_dir, exist_ok=True)

# Налаштування логування
log_file = os.path.join(log_dir, "task.log")
logging.basicConfig(filename=log_file, filemode='w', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

start_time = time.time()  # Фіксуємо час початку

# Основний цикл роботи програми (1 хвилина)
while time.time() - start_time < 60:
    elapsed_time = round(time.time() - start_time, 2)  # Час у секундах
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Поточний час

    logging.info(f"Програма працює: {elapsed_time} секунд. Поточний час: {current_time}")

    time.sleep(5)  # Затримка 5 секунд

# Запис фінального повідомлення
logging.error("Task completed")
