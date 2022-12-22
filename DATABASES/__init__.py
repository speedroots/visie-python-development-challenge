#!/usr/bin/python3

# External Resources

# Internal Resources

from .delete_employee import function_delete_employee
from .get_all_employees_no_filter import function_get_all_employees_no_filter
from .patch_employee import function_patch_employee
from .queries_employees import function_get_all_employees
from .queries_find_a_employee import function_get_filtered_employee
from .register_employee import function_register_employee

from UTILS import function_init_alert_loaded_status

function_init_alert_loaded_status(__name__)