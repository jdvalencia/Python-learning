#allover.py
import re
def is_done(s):
    return s == 'done' or s == 'quit'
def is_done2(s):
    return re.match('done|quit', s) != None
