#!/usr/bin/python3

# External Resources

# Internal Resources

from .database_connect import Proxy
from SQL_TEMPLATES import Employees
from UTILS import (
    function_gerenic_except_handler, 
)

def function_delete_employee(id_pessoa):

    try:

        proxy = Proxy()

        if proxy.proxy[0] != False:

            cursor = proxy.cursor

            if cursor != False:

                cursor.execute(Employees.function_delete_employee(id_pessoa['id_pessoa']))

                response = proxy.proxy[1].commit()

                cursor.close()
                proxy.proxy[1].close()

                return True

        else:

            return dict(proxy.proxy[1])

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'function_delete_employee', Error)