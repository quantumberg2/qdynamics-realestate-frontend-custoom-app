import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def subscribe(email):
    if not email:
        return {
            "status": "error",
            "message": _("Email is required")
        }

    # Check if email already exists
    existing = frappe.db.get_value(
        "Destiny-Promoters-Newsletter",
        {"email": email},
        ["name", "subscribed_or_not"],
        as_dict=True
    )

    # If record exists
    if existing:
        if existing.subscribed_or_not == "Yes":
            return {
                "status": "exists",
                "message": _("You are already subscribed")
            }
        else:
            return {
                "status": "pending",
                "message": _("You have subscribed successfully. Our admin will contact you shortly.")
            }

    # If new email → create record
    doc = frappe.get_doc({
        "doctype": "Destiny-Promoters-Newsletter",
        "email": email
    })

    doc.insert(ignore_permissions=True)
    frappe.db.commit()

    return {
        "status": "success",
        "message": _("You have subscribed successfully. Our admin will contact you shortly.")
    }
