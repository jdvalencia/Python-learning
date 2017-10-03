def get_age():
    while True:
        try:
            n = int(input('How old are you?\n'))
            return n
        except ValueError:
            print('Please enter an integer value.')
