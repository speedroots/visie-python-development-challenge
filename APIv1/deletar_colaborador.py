#!/usr/bin/python3

# External Resources

from datetime import datetime
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# Internal Resources

from ADMINISTRATIVE_APPLICATIONS_SERVICES import App
from UTILS import (
    function_deleted_employee, 
    function_gerenic_except_handler, 
    function_not_deleted_employee, 
    function_unavailable_resource, 
    function_validate_id_hash, 
)

from DATABASES import function_get_all_employees_no_filter, function_delete_employee

class Delete(BaseModel):

    id_pessoa: str

@App.core_application.delete ("/api/v1/employees/delete/employee", response_class= JSONResponse)
async def deletar_colaborador(deleteData: Delete) -> dict: #(id: str, item: Item)

    """
    Descrição:
      - Deleta um colaborador.
      - Retorno Esperado:
        - Um objeto/dicionário contendo a confirmação da requisição, com o state True
      - Método: JSON
      - Parâmetros:
        - id_pessoa: String (Obrigatório)
    """

    try:

        response = function_get_all_employees_no_filter()

        if response != False:

            id_pessoa = deleteData.id_pessoa if type(deleteData) != dict else deleteData['id_pessoa']

            employeeData = function_validate_id_hash(response, id_pessoa)

            if employeeData != None:

                response = function_delete_employee(employeeData)

                if response == True:

                    return function_deleted_employee()

                else:

                    return function_not_deleted_employee()

            else:

                return function_not_deleted_employee()

        else:

            return function_unavailable_resource(__name__, 'deletar_colaborador')

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'deletar_colaborador', Error)