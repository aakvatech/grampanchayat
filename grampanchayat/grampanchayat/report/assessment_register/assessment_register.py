# Copyright (c) 2013, FinForce Consulting LLP and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import numpy as np
import pandas as pd

def execute(filters=None):
	columns = get_columns()
	data = []
	properties = get_property_list(filters)
	# frappe.msgprint("Properties are: " + str(properties))
	
	if properties:
		colnames = [key for key in properties[0].keys()]
		df = pd.DataFrame.from_records(properties, columns=colnames)
		pvt = pd.pivot_table(
			df,
			values='amount',
			index=['street_name', 'property_number','property_category','property_type','owner_name','occupier_name'],
			columns='tax',
			fill_value=0
		)
		pvt.sort_values(by='property_number', ascending=True, inplace=True)
		data = pvt.reset_index().values.tolist()
		columns += pvt.columns.values.tolist()
	return columns, data
	


def get_columns():
	columns = [
		{"label": _("Street Name"), "fieldname": "street_name", "width": 200},
		{"label": _("property_number"), "fieldname": "property_number", "width": 100},
		{"label": _("property_category"), "fieldname": "property_category", "width": 100},
		{"label": _("property_type"), "fieldname": "property_type", "width": 100},
		{"label": _("owner_name"), "fieldname": "owner_name", "width": 100},
		{"label": _("occupier_name"), "fieldname": "occupier_name", "width": 100},
	]

	return columns

def get_property_list(filters):
	conditions = ""
	return frappe.db.sql("""SELECT 	p.street_name,
									p.property_number,
									p.property_category,
									p.property_type,
									p.owner_name,
									p.occupier_name,
									pt.tax,
									pt.amount,
									pt.idx
							FROM `tabProperty` p 
								LEFT JOIN `tabProperty Tax` pt on p.name = pt.parent
							ORDER BY p.name, pt.idx"""\
		.format(conditions=conditions), filters, as_dict=1)