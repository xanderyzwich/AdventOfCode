import datetime as dt
import os
import script1, script2

if __name__ == '__main__':
    start = dt.datetime.now()
    script1.main()
    print(dt.datetime.now() - start)
    script2.main()
    print(dt.datetime.now() - start)
