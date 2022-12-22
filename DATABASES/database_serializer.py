#!/usr/bin/python3


# External Resources

from configparser import ConfigParser

# Internal Resources

from UTILS import function_gerenic_except_handler

def function_mysql_serializer(filename='./DATABASES/database.ini', section='mysql'):

    try:

        parser = ConfigParser() # Create a parser

        parser.read(filename) # Read Config file

        db = {} # Get section

        if parser.has_section(section):

            params = parser.items(section)

            for param in params:

                db[param[0]] = param[1]
        else:

            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return db

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'function_mysql_serializer', Error)