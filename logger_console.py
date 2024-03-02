"""
LOGGER CONSOLE

logger is nothing but a little advanced way,
it just provides us some more functionalities

* What logger does?
# it looks at the message, and it will create a LogRecord object from the message string

* for the logger and the handler, if any level is below them they will ignore it

*  What is a formatter?
# LogRecord object that is now contained in the handler, because logger, passed the object,
# LogRecord object to the handler, handler is going to transfer it to the formatter,
  and formatter which we can definitely customize, this can format the LogRecord object,
  all the message in the desired format that we want, and then it's going to return
  it back to the handler to be printed on the console or a file.
"""
#create a logger
import logging

class LoggerDemoConsole():
    def testLog(self):
# create a logger
        logger = logging.getLogger('LoggerDemoConsole')
#sample_log is the name
        logger.setLevel(logging.INFO)
#setting the level of logger

# set to INFO, it will not print the debug statement, everything else will print
# Once it creates the LogRecord object,
# it will pass it to the handler, and we will see what a handler is in the next step,
# because we are creating console handler, and set its level to INFO.

# CREATE CONSOLE HANDLER AND SET LEVEL TO INFO
        chandler = logging.StreamHandler()
    #StreamHandler() means it's going to print to the console.
        chandler.setLevel(logging.INFO)

#CREATE FORMATTER
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')

# ADD FORMATTER TO CONSOLE HANDLER -> chandler
        chandler.setFormatter(formatter)
#.setFormatter() method- under that we are providing the object that we created for formatter

# ADD CONSOLE HANDLER TO LOGGER
# because console handlers are the final thing that is responsible to output the messages
        logger.addHandler(chandler)

    #LOGGING MESSAGES

        logger.debug(" Debug message ")
        logger.info(" Info message ")
        logger.warning(" Warning message ")
        logger.error(" Error message ")
        logger.critical(" Critical message ")

demo = LoggerDemoConsole()
demo.testLog()







