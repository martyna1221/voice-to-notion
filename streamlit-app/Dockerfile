FROM python:3.9-slim
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]