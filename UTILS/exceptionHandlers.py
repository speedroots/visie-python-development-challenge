#!/usr/bin/python3

# External Resources

from datetime import datetime
import logging

# Internal Resources

def function_gerenic_except_handler(name, function, Error):

    logger = logging.getLogger(name)

    error = {
    "file": name,
    "function": function,
    "error": str(Error),
    "datetime": str(datetime.now()),
    }

    logger.warning(Error)

    error.pop('file')

    return error

def function_mysql_not_connected(name, function):

    logger = logging.getLogger(name)

    error = {
    "file": name,
    "function": function,
    "error": 'The system cannot connect with configured MySQL database, please review the database configuration and the MySQL Service status.',
    "datetime": str(datetime.now()),
    }

    logger.warning(error['error'])

    error.pop('file')

    return error

def function_unavailable_resource(name, function):

    logger = logging.getLogger(name)

    error = {
    "file": name,
    "function": function,
    "error": "Oh no, something is wrong! Please, be patient 'cause our developers already working to fix the issue.",
    "datetime": str(datetime.now()),
    }

    logger.warning(error['error'])

    error.pop('file')

    return error

def function_mysql_error(error):

    dictResponse = {
    "code": error.errno, 
    "error": f"{error.errno} ({error.sqlstate}) Can't connect to MySQL server.", 
    "message": "Can't connect to MySQL server. For security purposes, the database address and port has been removed from log.", 
    "value": error.sqlstate, 
    }

    return dictResponse