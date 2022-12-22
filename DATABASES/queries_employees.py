#!/usr/bin/python3

# External Resources

import hashlib

# Internal Resources

from .database_connect import Proxy
from SQL_TEMPLATES import Employees
from UTILS import (
    function_gerenic_except_handler, 
    function_no_results_found,
    function_type_dir_and_content_check,
)

from SERIALIZERS import function_serializer_to_json

def function_get_all_employees(orderBy= None, reverse= False):

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

                    if orderBy != None:

                        serializedResponse = sorted(serializedResponse, key = lambda k: k[orderBy], reverse = reverse)

                    formattedResponse = [{
                    "id_pessoa": hashlib.md5(str(employee['id_pessoa']).encode()).hexdigest(),
                    #"cpf": employee['cpf'],
                    "data_admissao": employee['data_admissao'].strftime("%d/%m/%Y"),
                    #"data_nascimento": employee['data_nascimento'].strftime("%d/%m/%Y"),
                    "nome": employee['nome'].lstrip().rstrip().split(" ")[0],
                    #"rg": employee['rg'],
                    } for employee in serializedResponse]

                    cursor.close()
                    proxy.proxy[1].close()

                    return formattedResponse

                else:

                    return function_no_results_found()

        else:

            return dict(proxy.proxy[1])

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'function_get_all_employees', Error)