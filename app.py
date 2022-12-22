#!/usr/bin/python3

# External Resources

import uvicorn

# Internal Resources

from ROUTES import (
    function_html_routes, 
    manifests_routes, 
    function_icons_routes,
)

from UTILS import function_gerenic_except_handler

def runner():

    try:

        host = "127.0.0.1"
        #host = "0.0.0.0"

        uvicorn.run (
        "ADMINISTRATIVE_APPLICATIONS_SERVICES:App.core_application", 
        host= host,
        port= 80, 
        log_level= "info", 
        reload= True, 
        debug= True,
        access_log= True,
        #ssl_keyfile= "/STATIC/CERTS/.key",
        #ssl_certfile= "/STATIC/CERTS/.pem",
        )

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'runner', Error)

def main():

    try:

        runner()

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'main', Error)

if __name__ == '__main__':

    main()