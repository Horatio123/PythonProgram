fh = open('demo.txt', 'w')

try:
    for i in range(100):
        fh.write("this is line no %d \n" % (i + 1))
finally:
    fh.close()

with open('demo.txt', 'a') as fh2:
    for i in range(20):
        fh2.write("this is line no %d\n" %(i + 1))

with open('demo.txt', 'r') as fhr:
    print(fhr.read(7))
    print(fhr.readline())
    print(fhr.readline())
    print(fhr.readlines()[5])

with open('demo.txt', 'r') as fhr:
    for line in fhr:
        print(line.split(' '))
