#!/usr/bin/python3

# External Resources

# Internal Resources

from ADMINISTRATIVE_APPLICATIONS_SERVICES import App
from HTML_FUNCTIONS import (
    index_html_page, 
    post_html_page, 
    edit_employee, 
    delete_employee, 
)
from UTILS import function_gerenic_except_handler

def function_html_routes():

    try:

        App.core_application.include_router(delete_employee.router, prefix='/form/delete/employee')
        App.core_application.include_router(edit_employee.router, prefix='/form/edit/employee')
        App.core_application.include_router(index_html_page.router, prefix='/')
        App.core_application.include_router(post_html_page.router, prefix='/')

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'function_html_routes', Error)