#!/usr/bin/python3

# External Resources

from datetime import datetime
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Union

# Internal Resources

from ADMINISTRATIVE_APPLICATIONS_SERVICES import App
from UTILS import function_gerenic_except_handler, function_unavailable_resource
from DATABASES import function_get_filtered_employee
from SERIALIZERS import function_serializer_employee_params

class Employee(BaseModel):

    #cpf: Union[str, None] = None
    data_admissao: Union[str, None] = None
    #data_nascimento: Union[str, None] = None
    #id_pessoa: Union[int, None] = None
    nome: Union[str, None] = None
    #rg: Union[str, None] = None

@App.core_application.post ("/api/v1/employees/find/a/employee", response_class= JSONResponse)
async def localizar_um_colaborador(employee: Employee) -> dict:

    """
    Descrição:
      - Tentará retornar um colaborador específico, registrados na base de dados.
      - Método: JSON
      - Parâmetros:
        - cpf String(Opcional): xxx.xxx.xxx-xx
        - data_admissao String(Opcional)
        - data_nascimento String(Opcional)
        - id_pessoa INT(Opcional)
        - nome String(Opcional)
        - rg String(Opcional): xx.xxx.xxx-x
    """

    try:

        employee = employee.dict()

        if len(employee.keys()) > 0: 

            serializedEmployee = function_serializer_employee_params(employee)

            if len(serializedEmployee.keys()) > 0:

                response = function_get_filtered_employee(serializedEmployee)

                if response != False:

                    jsonifiedData = jsonable_encoder(response)

                    return JSONResponse(content= jsonifiedData)

                else:

                    return function_unavailable_resource(__name__, 'localizar_um_colaborador')

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'localizar_um_colaborador', Error)