
FROM python:3.12


WORKDIR /task


COPY . .

#
CMD ["python", "logger_task.py"]
