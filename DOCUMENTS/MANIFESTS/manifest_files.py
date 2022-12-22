#!/usr/bin/python3

from UTILS import function_gerenic_except_handler

def function_rootslab_management_tools_json():

    try:

        manifestFile = {
        "manifest_version": 2,
        "version": "versionString",
        "short_name": "RMA",
        "name": "Rafael Marques de Almeida",
        "author": "Rafael Marques de Almeida",
        "icons": [
        {
          "src": "",
          "type": "",
          "sizes": ""
        },
        ],
        "lang": "en-US",
        "default_locale": "en",
        "current_locale": "en",
        "dir": "ltr",
        "display": "browser",
        "start_url": "http://localhost:80",
        "homepage_url": "http://localhost/",
        }

        return manifestFile

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'function_rootslab_management_tools_json', Error)