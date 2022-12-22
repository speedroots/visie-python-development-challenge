#!/usr/bin/python3

from ADMINISTRATIVE_APPLICATIONS_SERVICES import App

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from .manifest_files import function_rootslab_management_tools_json

from UTILS import function_gerenic_except_handler

@App.core_application.get("/rootslab/links/documents/manifests/rootslab_management_tools.json", tags= ['RootsLab'], response_class= JSONResponse)
def manifest_rootslab_json():

    try:

        json_compatible_item_data = jsonable_encoder(function_rootslab_management_tools_json())
        return JSONResponse(content=json_compatible_item_data)

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'function_manifests_data', Error)
