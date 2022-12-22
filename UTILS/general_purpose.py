#!/usr/bin/python3

# External Resources

from datetime import datetime
import hashlib

# Internal Resources

def function_init_alert_loaded_status(name):

	print(f"- {datetime.now()}: [{name}] module has been successfuly loaded.")

def function_validate_id_hash(employees, id_pessoa):

	try:

		for employee in employees:

			hashedData = hashlib.md5(str(employee['id_pessoa']).encode()).hexdigest()

			if hashedData == id_pessoa:

				dictData = {
				'id_pessoa': employee['id_pessoa']
				}

				return dictData

		return None

	except Exception as Error:

		print(Error)