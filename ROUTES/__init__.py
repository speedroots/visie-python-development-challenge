#!/usr/bin/python3

# External Resources

# Internal Resources

from .api_version_one_routes import function_api_version_one_read
from .html_routes import function_html_routes
from .icon_routes import function_icons_routes
from .manifests_routes import function_manifests_routes
from UTILS import function_init_alert_loaded_status

function_init_alert_loaded_status(__name__)