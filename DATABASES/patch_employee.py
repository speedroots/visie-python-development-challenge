#!/usr/bin/python3

# External Resources

# Internal Resources

from .database_connect import Proxy
from SQL_TEMPLATES import Employees
from UTILS import (
    function_gerenic_except_handler, 
    function_no_results_found,
    function_type_dir_and_content_check,
)

from SERIALIZERS import function_serializer_to_json

def function_patch_employee(data_admissao, id_pessoa):

    try:

        proxy = Proxy()

        if proxy.proxy[0] != False:

            cursor = proxy.cursor

            if cursor != False:

                cursor.execute(Employees.function_update_employee(data_admissao, id_pessoa['id_pessoa']))

                response = proxy.proxy[1].commit()

                cursor.close()
                proxy.proxy[1].close()

                return True

        else:

            return dict(proxy.proxy[1])

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'function_get_all_employees_no_filter', Error)