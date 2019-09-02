# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "grampanchayat"
app_title = "Gram Panchayat"
app_publisher = "FinForce Consulting LLP"
app_description = "Gram Panchayat System"
app_icon = "fa fa-home"
app_color = "green"
app_email = "ramjan@finforce.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/grampanchayat/css/grampanchayat.css"
# app_include_js = "/assets/grampanchayat/js/grampanchayat.js"

# include js, css files in header of web template
# web_include_css = "/assets/grampanchayat/css/grampanchayat.css"
# web_include_js = "/assets/grampanchayat/js/grampanchayat.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "grampanchayat.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "grampanchayat.install.before_install"
# after_install = "grampanchayat.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "grampanchayat.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events


fixtures = [{"doctype":"Notification", "filters": [{"is_standard":0}]}, 'Auto Email Report', "Translation", {"doctype":"Print Format", "filters": [{"module":"GramPanchayat"}]}, {"doctype":"Report", "filters": [{"module":"GramPanchayat"}]} ]
#fixtures = ["Custom Field", "Custom Script", "Property Setter", {"doctype":"Naming Series", "filters": [{"doctype":"Daily Checklist"}]}, 'Workflow', 'Workflow State', 'Workflow Action', {"doctype":"Notification", "filters": [{"is_standard":0}]}, 'Auto Email Report', "Translation", {"doctype":"Print Format", "filters": [{"module":"Property Management Solution"}]}, {"doctype":"Report", "filters": [{"module":"Property Management Solution"}]} ]

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"grampanchayat.tasks.all"
# 	],
# 	"daily": [
# 		"grampanchayat.tasks.daily"
# 	],
# 	"hourly": [
# 		"grampanchayat.tasks.hourly"
# 	],
# 	"weekly": [
# 		"grampanchayat.tasks.weekly"
# 	]
# 	"monthly": [
# 		"grampanchayat.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "grampanchayat.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "grampanchayat.event.get_events"
# }

