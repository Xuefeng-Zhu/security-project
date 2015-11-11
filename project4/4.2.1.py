name = 'xzhu15'
print name + '\x00' * (10 - len(name)) + 'A+'
