import logging
import time
import os


os.makedirs("logs", exist_ok=True)


logging.basicConfig(
    filename="logs/task.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

start_time = time.time()
logging.info("Task started")

while True:
    elapsed_time = time.time() - start_time
    if elapsed_time > 60:
        break
    logging.info(f"Program running for {elapsed_time:.2f} seconds")
    time.sleep(5)

logging.error("Task completed")
