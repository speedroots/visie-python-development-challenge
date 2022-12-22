#!/usr/bin/python3

# External Resources

import pprint

# Internal Resources

def function_type_dir_and_content_check(content):

	dictData = {
	"content": content, 
	"dir": dir(content), 
	"type": type(content), 
	}

	pprint.pprint(
		dictData,
		indent= 4, 
	)