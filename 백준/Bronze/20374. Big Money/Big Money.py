a = open(0).read().rstrip()
print('%.2f'%sum(map(float,a.split('\n'))))
