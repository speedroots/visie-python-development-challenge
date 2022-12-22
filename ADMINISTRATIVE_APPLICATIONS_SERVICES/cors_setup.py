#!/usr/bin/python3

class CORS_Setup(object):

	def function_allow_credentials():

		return True

	def function_allow_headers():

		listData = ["*"]

		return listData

	def function_allow_methods():

		listData = ["*"]

		return listData

	def function_allow_origins():

		listData = [
	    "http://localhost",
	    ]

		return listData