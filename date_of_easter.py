import sys
from motd import IanTaylorEasterJscr

def Usage():
    print("Usage: %s <year>" % (sys.argv[0]))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            year = int(sys.argv[1])
            y, m, d = IanTaylorEasterJscr(year)
            print("You asked for the date of Easter in %d? Well, here it is:" % (year))
            print("%d-%d-%d" % (d, m, y))
        except ValueError:
            print("Please supply an integer argument! Not this: %s" % (sys.argv[1]))
            Usage()
    else:
        print 'You didn\'t give exactly one year!'
        Usage()