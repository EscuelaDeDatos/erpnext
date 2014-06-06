import frappe

def execute():
	frappe.reload_doc("utilities", "doctype", "address_template")
	if not frappe.db.sql("select name from `tabAddress Template`"):
		d = frappe.new_doc("Address Template")
		d.update({"country":frappe.db.get_default("country")})
		d.insert()
