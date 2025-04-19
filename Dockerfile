FROM python:3.7
WORKDIR /app
RUN pip install requirements.txt
COPY . . 
EXPOSE 5000
CMD["python","app.py"]
