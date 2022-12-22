#!/usr/bin/python3

# External Resources

# Internal Resources

from DOCUMENTS import manifest_rootslab_json, function_manifests_data
from UTILS import function_gerenic_except_handler

def function_head_content():

	try:

		htmlData = f'''
		<head>
			<meta charset="utf-8">
			<meta http-equiv="x-ua-compatible" content="ie=edge">
			<title>RootsLab</title>
			<meta name="description" content="">
			<meta name="viewport" content="width=device-width, initial-scale=1">

			<link rel="manifest" href="{function_manifests_data()['default_rootslab_manifest']}">
			<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.1/css/jquery.dataTables.min.css">
			<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
		</head>
		'''

		return htmlData

	except Exception as Error:

		return function_gerenic_except_handler(__name__, 'function_head_content', Error)