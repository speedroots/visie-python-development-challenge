#!/usr/bin/python3

# External Resources

from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Form, status
from typing import Union

# Internal Resources

from .body import function_index_html_page
from ADMINISTRATIVE_APPLICATIONS_SERVICES import App
from UTILS import function_gerenic_except_handler
from APIv1 import adicionar_colaborador

@App.core_application.get("/", response_class= HTMLResponse, include_in_schema= False)
async def index_html_page(description= "Carrega a interface de gestão dos colaboradores"):

    try:

        response = function_index_html_page()

        return response

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'index_html_page', Error)

@App.core_application.post("/", response_class= HTMLResponse, include_in_schema= False)
async def post_html_page(
    cpf: str = Form(...),
    data_admissao: str = Form(...),
    data_nascimento: str = Form(...),
    funcao: Union[str, None] = Form(None),
    nome: str = Form(...),
    rg: str = Form(...),
    description= "Redireciona a requisição para o endpoint de cadastro de um colaborador e redireciona para a página index"
    ):

    try:

        dictData = {
        "cpf": cpf,
        "data_admissao": data_admissao,
        "data_nascimento": data_nascimento,
        "funcao": funcao,
        "nome": nome,
        "rg": rg,
        "description": description,
        }

        await adicionar_colaborador(dictData)

        response =  RedirectResponse(
            url= App.core_application.url_path_for(name="index_html_page"),
            status_code=status.HTTP_302_FOUND, #status.HTTP_302_FOUND
        )

        return response

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'post_html_page', Error)