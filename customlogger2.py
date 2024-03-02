import logging
import LoggingInfrastructure.custom_logger as cl

class custom_logger2():

    log = cl.customLogger(logging.DEBUG)


    def method1(self):
        self.log.debug(" Debug message ")
        self.log.info(" Info message ")
        self.log.warning(" Warning message ")
        self.log.error(" Error message ")
        self.log.critical(" Critical message ")

    def method2(self):
#log out seperately completely defferent file
        m2log = cl.customlogger(logging.INFO)
        m2log.debug(" Debug message ")
        m2log.info(" Info message ")
        m2log.warning(" Warning message ")
        m2log.error(" Error message ")
        m2log.critical(" Critical message ")

    def method3(self):
        m3log = cl.customlogger(logging.INFO)
        m3log.debug(" Debug message ")
        m3log.info(" Info message ")
        m3log.warning(" Warning message ")
        m3log.error(" Error message ")
        m3log.critical(" Critical message ")

demo = custom_logger2()
demo.method1()
demo.method2()
demo.method3()

