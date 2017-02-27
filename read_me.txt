Parsing a logfile in below format to fetch the time difference.If there is time difference of 2 mins in consecutive log entry , it will output the difference.  

2017-02-26 06:38:48,972 - PYLOG - WARNING - items is not in logicaltophysical, keep this dictonary the same.
2017-02-26 06:38:49,040 - PYLOG - WARNING - XXXXXX is not in logicaltophysical, keep this dictonary the same.
2017-02-26 06:38:50,310 - PYLOG - WARNING - vrsvm6 is not in logicaltophysical, keep this dictonary the same.

[root@xxxxxx-yy user]# python time_diff.py /tmp/xxx_sanity_log_root_2017_02_25_23_41_58

2017-02-25 23:45:48 === 2017-02-25 23:58:15
2017-02-25 23:58:17 === 2017-02-26 00:14:47
2017-02-26 00:30:38 === 2017-02-26 00:34:38
2017-02-26 00:36:18 === 2017-02-26 00:39:49
IndexError at 2344
[root@xxxxxx-yy user]#
