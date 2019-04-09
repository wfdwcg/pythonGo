import json


map = {'key1':'va1', 'key9':'va9', 'key3':'va3'}
jsonStr = json.dumps(map)
print(jsonStr)

jsonMap = json.loads(jsonStr)
print(jsonMap)