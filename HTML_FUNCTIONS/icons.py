#!/usr/bin/python3

# External Resources

from starlette.responses import FileResponse

# Internal Resources

from ADMINISTRATIVE_APPLICATIONS_SERVICES import App

from UTILS import function_gerenic_except_handler

@App.core_application.get('/favicon.ico', include_in_schema=False)
async def return_default_favicon(description= "Return default favicon!"):

    try:

        favicon_path = './STATIC/icons/logo_rootslab.ico'

        return FileResponse(favicon_path)

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'return_default_favicon', Error)