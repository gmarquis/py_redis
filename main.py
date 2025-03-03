#!/usr/bin/python3
import redis, json, boto3, base64, os, socket
from pprint import pprint

def isOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        is_open = s.connect_ex((ip, int(port))) == 0 # True if open, False if not
        if is_open:
            s.shutdown(socket.SHUT_RDWR)
            return True
    except Exception:
        is_open = False
    s.close()
    return is_open

if isOpen('192.168.1.184', '6379'):
   _redis = redis.Redis(host='127.0.0.1', port=6379, db=0)
else:
   _redis = redis.Redis(host='127.0.0.1', port=6379, db=0)

_redis = redis.Redis(host='192.168.1.183', port=6379, db=0)

restaurant_484272 = {
    "name": "John",
    "type": "Doe",
    "address": {
        "street": {
            "line1": "11 Ramble St",
        },
        "city": "New York",
        "state": "NY",
        "zip": 10016,
    }
}
_redis.set(484272, json.dumps(restaurant_484272))
pprint(json.loads(_redis.get("484272")))

_redis.set('someVariable', 'this string was added.')
print(_redis.get('someVariable'))

someKey = 'Portugal'
_redis.mset({f'{someKey}': "Lisbon", "Spain": "Barcelona"})
_redis.psetex("Portugal", 9900, "Lisbon")    # purge milliseconds

if _redis.exists(someKey):
    print(f"Key {someKey}, Content " + str(_redis.get(someKey)))
else:
    print(f'Cannot find {someKey}')

from cryptography.fernet import Fernet
## key = Fernet.generate_key()
## key = Fernet(key)

def get_api_key(region: str, secret_name: str):
    # import awscreds
    # aws_access_key_id = awscreds.aws_access_key_id,
    # aws_secret_access_key = awscreds.aws_secret_access_key,
    import os
    session = boto3.session.Session()
    client = session.client(
    aws_access_key_id = os.getenv('aws_access_key_id'),
    aws_secret_access_key = os.getenv('aws_secret_access_key'),
    service_name='secretsmanager',
    region_name="eu-west-1"
    )
    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )
    secrets_response = get_secret_value_response['SecretString']
    return json.loads(secrets_response)

secret = get_api_key('eu-west-1','secret-name1/prod/key')   # from Secrets Manager
secret = secret['key']  # dict-key as string

key = base64.b64encode(secret.encode())
key = Fernet(key)
# print(key)

info = {
    "card-number": 3791849528391929,
    "exp": [2026, 2],
    "cv2": 248,
}

if _redis.get("user:1002") == None:
   print('creating user1002')
   _redis.set(
    "user:1002",
    key.encrypt(json.dumps(info).encode("utf-8"))
   )      
else:
    print('exists')

print(_redis.get("user:1002"))
print(json.loads(key.decrypt(_redis.get("user:1002"))))


exit()
