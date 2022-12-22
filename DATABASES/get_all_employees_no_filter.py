#!/usr/bin/python3

# External Resources

import hashlib

# Internal Resources

from .database_connect import Proxy
from SQL_TEMPLATES import Employees
from UTILS import (
    function_gerenic_except_handler, 
    function_no_results_found,
)

from SERIALIZERS import function_serializer_to_json

def function_get_all_employees_no_filter():

    try:

        proxy = Proxy()

        if proxy.proxy[0] != False:

            cursor = proxy.cursor

            if cursor != False:

                cursor.execute(Employees.function_select_all_from_employees())
                response = cursor.fetchall()
                fieldnames = cursor.column_names

                if cursor.rowcount > 0:

                    serializedResponse = function_serializer_to_json(fieldnames, response)

                    return serializedResponse

                else:

                    return function_no_results_found()

        else:

            return dict(proxy.proxy[1])

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'function_get_all_employees_no_filter', Error)