s = {1, 2, 2, 3, 9, 5}
print s
print len(s)
s.add(13)
print s
s.update([11, 21, 9])
print s
s.remove(11)
# 100 is not in s set, discard will not error, but remove will
s.discard(100)
s.pop()
print s
s.clear()
print s
s = {1, 2, 2, 3, 9, 5}


t = set([1, 2, 7])
print "t:"
print t
print "s:"
print s
print "union:"
print s | t
print s.union(t)
print "intersection:"
print s & t
print s.intersection(t)
print "difference:"
print s - t
print t - s
print s.difference(t)
print "symmetric difference"
print s ^ t
print s.symmetric_difference(t)


