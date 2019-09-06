for i in range(0, 10):
    if i == 4:
        break
    print i
print "finished"

for j in range(0, 10, 2):
    if j == 4:
        continue
    print j
else:
    print "finished"
