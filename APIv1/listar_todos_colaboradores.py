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
from DATABASES import function_get_all_employees

class Triggers(BaseModel):

    orderBy: Union[str, None] = None
    reverse: Union[bool, None] = False

@App.core_application.post ("/api/v1/employees/return/all/employees", response_class= JSONResponse)
async def listar_todos_colaboradores(orderBy: Triggers) -> dict: #(id: str, item: Item)

    """
    Descrição:
      - Retorna todos os colaboradores registrados na base de dados.
      - Retorno Esperado:
        - Listas de objetos/dicionários, contendo o Primeiro Nome e a Data de Admissão do colaborador
      - Método: JSON
      - Parâmetros:
        - orderBy String (Opcional)
        - reverse Boolean (Opcional)
      - É possível ordenar os colaboradores pelas seguintes opções abaixo:
        - nome (Obs: Somente o Primeiro Nome será retornado)
        - rg (Bloqueado seguindo as especificações da documentação, é possível trabalhar com esses retornos, alterando-se o código-fonte)
        - cpf (Bloqueado seguindo as especificações da documentação, é possível trabalhar com esses retornos, alterando-se o código-fonte)
        - data_admissao
        - data_nascimento (Bloqueado seguindo as especificações da documentação, é possível trabalhar com esses retornos, alterando-se o código-fonte)
        - Insira uma das opções acima, como valor para orderBy
      - Caso alguma das opções disponíveis em orderBy seja aplicada, o parâmetro reverse poderá ser aplicado:
        - True: Retornará a lista de colaboradores em ordem decrescente, baseado no valor para orderBy
        - False: Retornará a lista de colaboradores em ordem crescente, baseado no valor para orderBy
    """

    try:

        fieldnames = [
        'nome',
        #'rg',
        #'cpf',
        'data_admissao',
        #'data_nascimento',
        ]

        if orderBy.orderBy in fieldnames:

            response = function_get_all_employees(orderBy.orderBy, orderBy.reverse)

        else:

            response = function_get_all_employees()

        if response != False:

            jsonifiedData = jsonable_encoder(response)

            return JSONResponse(content= jsonifiedData)

        else:

            return function_unavailable_resource(__name__, 'listar_todos_colaboradores')

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'listar_todos_colaboradores', Error)