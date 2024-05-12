FROM python:3.8
COPY requirement.txt requirement.txt
RUN pip install --no-cache-dir -r requirement.txt
COPY . code
WORKDIR / code
EXPOSE 8000
ENTRYPOINT ["python","fruitables2.0/manage.py"]
CMD ["runserver","0.0.0.0:8000"]