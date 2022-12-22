#!/usr/bin/python3

# External Resources

# Internal Resources

from ADMINISTRATIVE_APPLICATIONS_SERVICES import App
from DOCUMENTS import manifest_rootslab_json
from UTILS import function_gerenic_except_handler

def function_manifests_routes():

    try:

        App.core_application.include_router(manifest_rootslab_json.router, prefix='/html')

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'function_manifests_routes', Error)