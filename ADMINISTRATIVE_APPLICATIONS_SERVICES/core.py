#!/usr/bin/python3


# External Resources

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from pathlib import Path

# Internal Resources

from .contact import function_contact
from .cors_setup import CORS_Setup
from .metadata import function_meta_data
from .parameters import function_swagger_ui_parameters
from .terms import function_terms_of_service_url
from .description import function_description

from UTILS import function_gerenic_except_handler

class App(object):

    try:

        teste = function_description()

        core_application = FastAPI(
            contact= function_contact(),
            description= function_description(),
            openapi_tags= function_meta_data(),
            swagger_ui_parameters= function_swagger_ui_parameters(),
            terms_of_service= function_terms_of_service_url(),
            title = "Employees Management Tool",
            version="2022-12-16",
        )

        BASE_DIR = Path('STATIC').resolve().parent

        core_application.mount("/STATIC", StaticFiles(directory=Path(BASE_DIR, 'STATIC')), name="STATIC")

        core_application.add_middleware (
            CORSMiddleware,
            allow_credentials= CORS_Setup.function_allow_credentials(),
            allow_headers= CORS_Setup.function_allow_headers(),
            allow_methods= CORS_Setup.function_allow_methods(),
            allow_origins= CORS_Setup.function_allow_origins(),
        )

        SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

        core_application.add_middleware (
            SessionMiddleware, 
            secret_key= SECRET_KEY
        )

    except Exception as Error:

        function_gerenic_except_handler(__name__, 'App', Error)