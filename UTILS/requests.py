#!/usr/bin/python3

def function_no_results_found():

	dictData = {
	"state": False,
	"message": "Sorry, no one results found."
	}

	return dictData

def function_patch_update_employee():

	dictData = {
	"method": "PATCH", 
	"state": True,
	"message": "The employee data_admissao has been updated successfully.", 
	}

	return dictData

def function_not_patched_update_employee():

	dictData = {
	"method": "PATCH", 
	"state": False,
	"message": "No one employee has been updated.", 
	}

	return dictData

def function_deleted_employee():

	dictData = {
	"method": "DELETE", 
	"state": True,
	"message": "The employee has been deleted.", 
	}

	return dictData

def function_not_deleted_employee():

	dictData = {
	"method": "DELETE", 
	"state": False,
	"message": "No one employee has been deleted.", 
	}

	return dictData

def function_registered_employee():

	dictData = {
	"method": "POST", 
	"state": True,
	"message": "The employee has been created successfully.", 
	}

	return dictData

def function_not_registered_employee():

	dictData = {
	"method": "POST", 
	"state": False,
	"message": "No one employee has been created, review your payload data and try again.", 
	}

	return dictData