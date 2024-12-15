
# Python collects aws-credentials from bash environment variables populated via docker run --env-file
# Get, encrypt/replace Redis values using AWS Secrets Manager 'key'
# https://github.com/redis/redis-py/blob/master/README.md <br/>
# https://cryptography.io/en/latest/fernet/ <br/>
# python3 redis_functions <br/>

main.py <br/>
Dockerfile <br/>
requirements.txt <br/>
docker-compose.yml <br/>

docker build -t redis_functions  -f Dockerfile . <br/>
docker run -it --env-file ~/.aws/credentials redis_functions <br/>
docker tag redis_functions:latest virtualvessel/public:redis_functions <br/>
docker push docker tag virtualvessel/public:redis_functions

Alternatively - <br/>
docker pull virtualvessel/public:redis_functions <br/>

Redis Insights - <br/>
http://127.0.0.1:8001/redis-stack/browser <br/>

Redis Cli - <br/>
docker exec -it container-name redis-cli <br/>
SET GlenMarquis redis EX 60 NX <br/>
DEL GlenMarquis <br/>
