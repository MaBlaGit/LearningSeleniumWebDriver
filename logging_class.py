#! /usr/bin/python

"""Custom logging class."""

import logging
import os

class LoggingClass():

    def __init__(self):
        if not os.path.exists('./logs'):
            os.mkdir('./logs')        
    
    def logging_method(self, message):
        logging.basicConfig(filename='./logs/selenium_logs.log', level=logging.INFO)
        logging.info(message)

