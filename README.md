
Python collects aws-credentials from bash environment variables or via docker run --env-file <br/>
The code -
# gets/encrypts/replaces Redis values using an AWS Secrets Manager 'key' <br/>
https://github.com/redis/redis-py/blob/master/README.md <br/>
https://cryptography.io/en/latest/fernet/ <br/>

main.py <br/>
Dockerfile <br/>
requirements.txt <br/>

docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest <br/>
docker pull virtualvessel/public:redis_functions <br/>
Or build locally - <br/>
docker build -t redis_functions  -f Dockerfile . <br/>
docker tag redis_functions:latest virtualvessel/public:redis_functions <br/>
docker push virtualvessel/public:redis_functions <br/>
1. Set linux environment variables for AWS access - <br/>
aws_access_key_id=AKIA... <br/>
aws_secret_access_key=... <br/>
docker run -it redis_functions <br/>
2. Alternativley - <br/>
docker run -it --env-file ~/.aws/credentials redis_functions <br/>

Redis Insights - <br/>
http://127.0.0.1:8001/redis-stack/browser <br/>

Redis Cli - <br/>
docker exec -it redis-stack-server redis-cli <br/>
SET GlenMarquis redis EX 60 NX <br/>
DEL GlenMarquis <br/>
