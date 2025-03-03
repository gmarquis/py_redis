
# Python collects aws-credentials from bash environment variables populated via docker run --env-file
# Get, encrypt/replace Redis values using AWS Secrets Manager 'key'
# https://github.com/redis/redis-py/blob/master/README.md <br/>
# https://cryptography.io/en/latest/fernet/ <br/>
# python3 redis_functions <br/>

main.py <br/>
Dockerfile <br/>
requirements.txt <br/>

docker pull virtualvessel/public:redis_functions <br/>

Build locally - <br/>
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
docker exec -it container-name redis-cli <br/>
SET GlenMarquis redis EX 60 NX <br/>
DEL GlenMarquis <br/>
