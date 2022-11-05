from operator import itemgetter

sample = [[4,'c'], [10, 'b'], [13, 'b'], [1, 'd'], [10, 'a']]

temp = sorted(sample, key=itemgetter(1), reverse = False)
result = sorted(temp, key=itemgetter(0), reverse = True)

print( result)