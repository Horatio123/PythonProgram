import json

j = {
    'name': 'Horatio',
    'age': 18,
    'marks': [20, 30, 90],
    'pass': True
}
print(j)
print("only dumps:")
print(json.dumps(j))
print("add indent:")
print(json.dumps(j, indent=4))
print("add separator and sort:")
print(json.dumps(j, indent=4, separators=('', '='), sort_keys=True))

with open('demo.json', 'w') as jw:
    jw.write(json.dumps(j, indent=4))

with open('demo.json', 'r') as jr:
    print("read from json file:")
    print(jr.read())

with open('demo.json', 'r') as jr2:
    json_str = jr2.read()
    json_value = json.loads(json_str)
    print('name and age in json file:')
    print(json_value['name'])
    print(json_value.get('age'))
