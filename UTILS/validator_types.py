#!/usr/bin/python3

# External Resources

from UTILS import function_gerenic_except_handler

# Internal Resources

def function_proxy_validator(setConnection):

    try:

        classType = "<class 'mysql.connector.connection_cext.CMySQLConnection'>"

        return True if classType in str(type(setConnection)) \
        and setConnection.is_connected() == True else False

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'function_mysql_connect', Error)