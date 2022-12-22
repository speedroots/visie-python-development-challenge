#!/usr/bin/python3

# External Resources

from datetime import datetime

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# Internal Resources

from ADMINISTRATIVE_APPLICATIONS_SERVICES import App
from UTILS import (
    function_gerenic_except_handler, 
    function_not_patched_update_employee, 
    function_patch_update_employee, 
    function_unavailable_resource, 
    function_validate_id_hash, 
)

from DATABASES import function_get_all_employees_no_filter, function_patch_employee

class Update(BaseModel):

    data_admissao: str
    id_pessoa: str

@App.core_application.patch ("/api/v1/employees/update/employee", response_class= JSONResponse)
async def atualizar_colaborador(updateData: Update) -> dict: #(id: str, item: Item)

    """
    Descrição:
      - Atualiza a data de admissão do colaborador.
      - Retorno Esperado:
        - Um objeto/dicionário contendo a confirmação da requisição, com o state True
      - Método: JSON
      - Parâmetros:
        - data_admissao: String (Obrigatório) YYYY-mm-dd
        - id_pessoa: String (Obrigatório)
    """

    try:

        response = function_get_all_employees_no_filter()

        if response != False:

            jsonifiedData = jsonable_encoder(response)

            id_pessoa = updateData.id_pessoa if type(updateData) != dict else updateData['id_pessoa']

            employeeData = function_validate_id_hash(response, id_pessoa)

            if employeeData != None:

                data_admissao = updateData.data_admissao if type(updateData) != dict else updateData['data_admissao']

                response = function_patch_employee(data_admissao, employeeData)

                if response == True:

                    response = function_patch_update_employee()

                else:

                    response = function_not_patched_update_employee()

                return JSONResponse(content= response)

            else:

                return JSONResponse(content= function_not_patched_update_employee())

        else:

            return function_unavailable_resource(__name__, 'atualizar_colaborador')

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'atualizar_colaborador', Error)