animals = ["pig", "dog", "cat"]
print (animals)
print (animals[0])
print (animals[-1])
print (animals[-3])
animals.append("fish")
print (animals)
age = [11, 12, 13]
animals.extend(age)
print (animals)
animals.remove("pig")
print (animals)
print (animals, age)
print (len(animals))
print (max(age))
print age * 2
print age.count(12)
print animals + age
