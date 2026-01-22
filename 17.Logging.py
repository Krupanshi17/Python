"""
Logging Module
------------------
This module provides functionality for logging messages with different severity levels.
Logging is essential for tracking events that happen during program execution, which can help in 
debugging and monitoring applications.
The logging module in Python allows you to log messages to various outputs, such as the console or 
files, with different levels of importance.
The primary logging levels are DEBUG, INFO, WARNING, ERROR, and CRITICAL. Each level indicates the
severity of the logged message.
You can configure the logging module to set the logging level, format of the log messages, and output
destination.

DEBUG → detailed info

INFO → normal messages

WARNING → something odd

ERROR → error occurred

CRITICAL → serious failure


"""

import logging

# Configure logging
"""logging.basicConfig(level=logging.INFO)

logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")"""

logging.basicConfig(filename='app.log',level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s')

logging.info("Application started")

try:
    number = int(input("Enter a number: "))
    result =100 / number
    logging.info("Calculation Successful")
except ValueError:
    logging.error("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    logging.critical("Error! Division by zero is not allowed.")
logging.info("Application ended")
