#!/usr/bin/python3

# External Resources

# Internal Resources

from ADMINISTRATIVE_APPLICATIONS_SERVICES import App
from APIv1 import (
    #localizar_um_colaborador, 
    atualizar_colaborador, 
    listar_todos_colaboradores, 
    registrar_colaborador, 
)

from UTILS import function_gerenic_except_handler

def function_api_version_one_read():

    try:

        #App.core_application.include_router(localizar_um_colaborador.router, prefix='/')
        App.core_application.include_router(atualizar_colaborador.router, prefix='/')
        App.core_application.include_router(listar_todos_colaboradores.router, prefix='/')
        App.core_application.include_router(registrar_colaborador.router, prefix='/')

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'function_api_version_one_read', Error)