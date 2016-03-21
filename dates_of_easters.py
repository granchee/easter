import sys
from motd import IanTaylorEasterJscr

def Usage():
    print("Usage: %s <year> <year>*" % (sys.argv[0]))
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        print 'You asked for the dates of Easters? Well, here they are:'
        try:
            for year_s in sys.argv[1:]:
                year_i = int(year_s)
                y, m, d = IanTaylorEasterJscr(year_i)
                print("%d-%d-%d" % (d, m, y))
        except ValueError:
            print("Please supply integer arguments! Not this: %s" % (year_s))
            Usage()
    else:
        print 'You didn\'t give any years!'
        Usage()