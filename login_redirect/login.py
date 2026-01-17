import frappe

def redirect_customer(login_manager):
    user = frappe.session.user

    if user == "Guest":
        return

    roles = frappe.get_roles(user)

    if "Customer" in roles:
        frappe.local.response["home_page"] = "/helpdesk/my-tickets"
