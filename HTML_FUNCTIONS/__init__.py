#!/usr/bin/python3

# External Resources

# Internal Resources

from .edit import edit_employee
from .icons import return_default_favicon
from .index import index_html_page, post_html_page
from .remove import delete_employee

from UTILS import function_init_alert_loaded_status

function_init_alert_loaded_status(__name__)