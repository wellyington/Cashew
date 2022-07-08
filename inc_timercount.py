from time import sleep
def timecount(seconds):
    while seconds:
        min, sec = divmod(seconds, 60)
        count = 'Wait {:d}min:{:d}sec'.format(min, sec)
        print(count, end='\r')
        sleep(1)
        seconds -= 1