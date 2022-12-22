#!/usr/bin/python3

# External Resources

from datetime import datetime
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Union

# Internal Resources

from ADMINISTRATIVE_APPLICATIONS_SERVICES import App
from UTILS import (
    function_gerenic_except_handler, 
    function_registered_employee, 
    function_not_registered_employee,
)

from DATABASES import function_register_employee

class Register(BaseModel):

    cpf: str
    data_admissao: str
    data_nascimento: str
    funcao: Union[str, None] = None
    nome: str
    rg: str

@App.core_application.post ("/api/v1/employees/add/employee", response_class= JSONResponse)
async def adicionar_colaborador(registerData: Register) -> dict:

    """
    Descrição:
      - Adiciona um colaborador.
      - Retorno Esperado:
        - Um objeto/dicionário contendo a confirmação da requisição, com o state True ou False
      - Método: JSON
      - Parâmetros:
        - nome String (Obrigatório)
        - rg String (Obrigatório) xx.xxx.xxx-x (Fora definido como regra, que esses valores não podem se repetir na base de dados)
        - cpf String (Obrigatório) xxx.xxx.xxx-xx (Fora definido como regra, que esses valores não podem se repetir na base de dados)
        - data_admissao String (Obrigatório) YYYY-mm-dd
        - data_nascimento String (Obrigatório) YYYY-mm-dd
        - funcao: String (Opcional)
    """

    try:

        response = function_register_employee(registerData)

        if response == True:

            jsonifiedData= function_registered_employee()

        else:

            jsonifiedData= function_not_registered_employee()

        return JSONResponse(content= jsonifiedData)

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'adicionar_colaborador', Error)