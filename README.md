
# Get, replace/encrypt Redis values using 'key' from AWS Secrets Manager 
# https://github.com/redis/redis-py/blob/master/README.md <br/>
# https://cryptography.io/en/latest/fernet/ <br/>
# python redis_functions <br/>



main.py <br/>
requirements.txt <br/>

Dockerfile = <br/>
FROM python:3.11-alpine <br/>
ENV PYTHONUNBUFFERED=1 \ <br/>
    PIP_NO_CACHE_DIR=1 <br/>
WORKDIR /app <br/>
COPY . /app <br/>
RUN pip install --upgrade pip setuptools wheel <br/>
COPY requirements.txt . <br/>
RUN pip install -r requirements.txt <br/>
RUN pip3 install cryptography <br/>
EXPOSE 5000 <br/>
ENTRYPOINT ["python", "main.py"] <br/>

docker build -t redis_functions  -f Dockerfile . <br/>
docker run -it redis_functions <br/>

docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest <br/>

Redis Insights - <br/>
http://127.0.0.1:8001/redis-stack/browser <br/>

Redis Cli - <br/>
docker exec -it container-name redis-cli <br/>
SET GlenMarquis redis EX 60 NX <br/>
DEL GlenMarquis <br/>
