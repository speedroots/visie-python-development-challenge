#!/usr/bin/python3

# External Resources

# Internal Resources

from ADMINISTRATIVE_APPLICATIONS_SERVICES import App
from HTML_FUNCTIONS import return_default_favicon
from UTILS import function_gerenic_except_handler

def function_icons_routes():

    try:

        App.core_application.include_router(return_default_favicon.router, prefix='/')

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'function_icons_routes', Error)