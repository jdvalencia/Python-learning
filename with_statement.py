num = 1
with open(fname, 'r') as f:
    for line in f:
        print('%04d %s' % (num,line), end = '')
        num = num + 1
