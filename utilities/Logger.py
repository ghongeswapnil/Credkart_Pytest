import inspect
import logging


class Logging_Class:
    @staticmethod
    def log_generator():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("E:\\Automation\\Practice_Pytest_Credkart\\Logs\\Credkart_Logfile.log")
        format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger


# File
# Format
# file-->format
# add log
# log level

# Log Level --------
# Debug
# Info
# Warning
# error
# critical







































































