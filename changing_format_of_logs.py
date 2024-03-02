"""
CHANGING THE FORMAT OF LOGS

* how do we change the format of the log messages that are displayed to us, right, either in the files or the console.

# https://docs.python.org/3/library/logging.html#logrecord-attributes
# https://docs.python.org/3/library/time.html#time.strftime
"""
#import logging
#logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
# This is the method provided by logging module which we can use to provide the configuration that we want the logs to follow.
#logging.warning(" Warning message ")
#logging.info(" Info message ")
#logging.error(" Error message ")

# how we can add time to the logging
# because most of the time we have seen the time, starting, the starting of the log is the time that when the log started, when was the message logged, so the time is always in the starting, in the beginning of the log message,

#import logging
#logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.DEBUG)
# This is the method provided by logging module which we can use to provide the configuration that we want the logs to follow.
#logging.warning(" Warning message ")
#logging.info(" Info message ")
#logging.error(" Error message ")

# to change the time format

import logging
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p' , level=logging.DEBUG)

logging.warning(" Warning message ")
logging.info(" Info message ")
logging.error(" Error message ")

