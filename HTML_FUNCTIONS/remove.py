#!/usr/bin/python3

# External Resources

from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Form, status
from typing import Union

# Internal Resources

from .body import function_index_html_page
from ADMINISTRATIVE_APPLICATIONS_SERVICES import App
from UTILS import function_gerenic_except_handler
from APIv1 import deletar_colaborador

@App.core_application.post("/form/delete/employee", response_class= HTMLResponse, include_in_schema= False)
async def delete_employee(
    id_pessoa: str = Form(...),
    description= "Descrição de teste"
    ):

    try:

        dictData = {
        "id_pessoa": id_pessoa,
        }

        await deletar_colaborador(dictData)

        response =  RedirectResponse(
            url= App.core_application.url_path_for(name="index_html_page"),
            status_code=status.HTTP_302_FOUND, #status.HTTP_302_FOUND
        )

        return response

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'edit_employee', Error)