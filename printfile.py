#printfile.py
def print_file1(fname):
    f = open(fname, 'r')
    for line in f:
        print(line, end = '')
    f.close() # optional

#easier print(open(fname, 'r').read())
