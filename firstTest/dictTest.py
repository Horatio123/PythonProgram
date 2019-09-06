d = {'name': 'Tom', 'age': 10}
print d
print d['name']
print d.get('age')
print len(d)
d['hometown'] = "Now york"
print d
d['name'] = 'spike'
d.update({'age': 11})
print d
print d.keys()
print d.values()
print d.items()
d.popitem()
print d.items()
