#!/usr/bin/python3

# External Resources

# Internal Resources

from UTILS import function_gerenic_except_handler

def function_contact():

    try:

    	dictData = {
        "name": "Rafael Marques de Almeida",
        "url": "https://www.linkedin.com/in/speedroots/",
        "email": "rafael_almeida2015@outlook.com",
        }

    	return dictData

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'function_contact', Error)