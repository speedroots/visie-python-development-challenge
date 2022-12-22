#!/usr/bin/python3

# External Resources

# Internal Resources

from .database_connect import Proxy
from SQL_TEMPLATES import Employees
from UTILS import (
    function_gerenic_except_handler, 
)

def function_register_employee(employee):

    try:

        proxy = Proxy()

        if proxy.proxy[0] != False:

            cursor = proxy.cursor

            if cursor != False:

                cursor.execute(Employees.function_register_employee(employee))

                response = proxy.proxy[1].commit()

                responseValue = cursor.rowcount

                cursor.close()
                proxy.proxy[1].close()

                if responseValue == 1:

                    return True

                else:

                    return False

        else:

            return dict(proxy.proxy[1])

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'function_register_employee', Error)