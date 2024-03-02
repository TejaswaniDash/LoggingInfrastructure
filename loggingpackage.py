"""
LOGGING
* when do we logging, and what is logging?
# Logging is something that we print statements, we print whatever we want to print in order to say that application is doing something.
# Logging is something we really want in our application to say this statement does something, this statement did something else, this is doing something else.

* What is the limitation?
# It only prints to the console, It does not print anywhere else

"""
"""
* Need of logging?
# we can see if there are errors or warnings or critical issues, 
# or any of those kinds of things which are really helpful when we are debugging the code 
# or we are looking at the execution time. 
So this is why we really need logging.

* Logging Levels- 
Levels means that kind of information we want to write to the console or file, wherever you want to write, 
so that at the end when we can differentiate between different kinds of actions performed by the application.

# DEBUG
which is something we want when we are debugging something. 
So let's say there are some issues, some bugs, and you want to write some some kind of d
etailed information that you only want to see when you are debugging the code, and not 
other should see that.

# INFO
it acts as a confirmation that things are working as expected. 

# WARNING
This is an indication that something unexpected happened, 
or some problem may happen in the near future, 
but the software is still working as expected, 
so there are no issues with the software, 
and there are no concerns at this moment, 
but it may happen in the future. 
So for those kinds of statements, we want to log as WARNING.

# ERRORS
This is like a more serious problem
The software is not able to perform some functionality as expected, the way we thought,
if some critical thing happened, and some exception happened, 
we want to say that this is an exception, it is an error, 
So in those kinds of situations, we want to log the information as ERROR.

# CRITICAL
this is a more serious error. 
Depending on the application, depending on the kind of action that's performed, 
the program needs to tell that something really critical happened, 
and it's kind of a serious error which kind of indicates that the program itself may be unable to continue running, 
something might have happened that the program will not be able to continue to run. 

"""

# we were using print statement to print something till now

#print("This is a test using a print statement")
#It only prints to the console, It does not print anywhere else

# let's see how can we use logging instead of print statement
# module provided my python

import logging
#logging.warning(" Warning message ")
#logging.info(" Info message ")

# here it is not printing the info message
# because by default the threshold is, threshold is set to WARNING,
# so it will print only messages that are above a WARNING level.

# And what are the messages above WARNING level?
# These are the messages WARNING, ERROR, CRITICAL, because it does not print DEBUG and INFO messages for every run.

#logging.error(" Error message ")

print("*"*60)

# Let's see how we can put it into a file

logging.basicConfig(filename="test.log", level=logging.DEBUG)
# This is the method provided by logging module which we can use to provide the configuration that we want the logs to follow.
logging.warning(" Warning message ")
logging.info(" Info message ")
logging.error(" Error message ")
#file created with all the statements











