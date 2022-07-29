
FROM python:3.7-slim

COPY requirements.txt /

RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

WORKDIR /app
ADD . /app

RUN pip install .

# ENTRYPOINT ["python", "./srs/main.py" ,  ,"Berlin" , "--duration" , "10"]
 
