#!/usr/bin/python3

# External Resources

# Internal Resources

from .exceptionHandlers import (
	function_gerenic_except_handler, 
	function_mysql_not_connected,
	function_unavailable_resource,
	function_mysql_error,
)

from .general_purpose import (
	function_init_alert_loaded_status, 
	function_validate_id_hash, 
)

from .requests import (
	function_deleted_employee, 
	function_no_results_found, 
	function_not_deleted_employee, 
	function_not_patched_update_employee, 
	function_not_registered_employee, 
	function_patch_update_employee, 
	function_registered_employee, 
)

from .unit_tests import function_type_dir_and_content_check
from .validator_types import function_proxy_validator

function_init_alert_loaded_status(__name__)