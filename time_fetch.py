import re
from datetime import datetime
import pdb
import sys


fp = open(sys.argv[1],'r')

time_line= []
for line in fp.readlines():
    t_pat = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")
    match = re.search(t_pat,line)
    if match:
        time_stamp_tmp = match.group()
        time_stamp = datetime.strptime(time_stamp_tmp,'%Y-%m-%d  %H:%M:%S')
        time_line.append(time_stamp)

for i,v in enumerate(time_line,1):
    try:
        diff = time_line[i] - time_line[i-1]
        if diff.total_seconds() > 120.0 :
            print '\n{} === {}'.format(time_line[i-1],time_line[i])
    except IndexError:
        print "IndexError at {}".format(i)
