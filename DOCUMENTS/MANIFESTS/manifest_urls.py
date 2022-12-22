#!/usr/bin/python3

from ADMINISTRATIVE_APPLICATIONS_SERVICES import App

from UTILS import function_gerenic_except_handler

def function_url_path_for(functionName):

    try:

        return App.core_application.url_path_for(functionName)


    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'function_url_path_for', Error)

def function_manifests_data():

    try:

        manifestData = {
        "default_rootslab_manifest": function_url_path_for("manifest_rootslab_json"),
        } 

        return manifestData

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'function_manifests_data', Error)