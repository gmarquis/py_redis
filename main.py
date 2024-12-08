#!/usr/bin/python
import redis, json
from pprint import pprint

_redis = redis.Redis(host='192.168.1.184', port=6379, db=0)

restaurant_484272 = {
    "name": "Ravagh",
    "type": "Persian",
    "address": {
        "street": {
            "line1": "11 E 30th St",
            "line2": "APT 1",
        },
        "city": "New York",
        "state": "NY",
        "zip": 10016,
    }
}
_redis.set(484272, json.dumps(restaurant_484272))
pprint(json.loads(_redis.get("484272")))
someKey = 'Portugal'
_redis.set('someVariable', 'Some variable was set.')
_redis.mset({f'{someKey}': "Lisbon", "Spain": "Barcelona"})
_redis.psetex("Portugal", 9900, "Lisbon")    # purge milliseconds
if _redis.exists(someKey):
    print(f"Key {someKey}, Content " + str(_redis.get(someKey)))
else:
    print(f'Cannot find {someKey}')

print(_redis.get('someVariable'))

from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key) ; key = Fernet(key)

info = {
    "card-number": 2211849528391929,
    "exp": [2025, 8],
    "cv2": 842,
}

_redis.set(
    "user:1000",
    key.encrypt(json.dumps(info).encode("utf-8"))
)

print(_redis.get("user:1000")) # cipher
print(json.loads(key.decrypt(_redis.get("user:1000"))))


