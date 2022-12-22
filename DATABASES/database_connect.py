#!/usr/bin/python3

# External Resources

import mysql.connector

# Internal Resources

from .database_serializer import function_mysql_serializer

from UTILS import (
    function_mysql_error, 
    function_mysql_not_connected, 
    function_proxy_validator, 
)

class Proxy(object):

    def __init__(self):

        
        self.proxy = self.function_proxy()

        if self.proxy[0] != False:

            self.cursor = self.proxy[1].cursor()

        else:

            self.cursor = False

    def function_proxy(self):

        params = function_mysql_serializer()

        try:

            self.setConnection = mysql.connector.connect(
                database= params['mysql_db'],
                host= params['mysql_host'],
                password= params['mysql_pass'],
                user= params['mysql_user'],
            )

            if function_proxy_validator(self.setConnection) != False:

                return True, self.setConnection

            else:

                function_mysql_not_connected(__name__, 'Proxy')

                self.setConnection= False

                return False, self.setConnection

        except mysql.connector.Error as error:

            print(function_mysql_error(error))

            return False, function_mysql_error(error)