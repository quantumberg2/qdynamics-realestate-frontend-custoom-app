import frappe
import json

@frappe.whitelist(allow_guest=True)
def send_suggestion():
    """Save suggestion and send email"""
    data = frappe.local.form_dict

    # If frontend sends JSON, parse it
    if isinstance(data, str):
        data = json.loads(data)

    name = data.get("name")
    email = data.get("email")
    contact = data.get("contact")
    subject = data.get("subject")
    message = data.get("message")

    # Save in Suggestion DocType
    doc = frappe.get_doc({
        "doctype": "Suggestion",
        "name1": name,
        "email": email,
        "contact_number": contact,
        "subject": subject,
        "message": message
    })
    doc.insert(ignore_permissions=True)
    frappe.db.commit()

    # Send email
    frappe.sendmail(
        recipients=["wequantumberg@gmail.com"],   # ✅ your inbox
        sender="wequantumberg@gmail.com",         # ✅ must match Email Account login_id
        reply_to=email,                           # ✅ user email for replies
        subject=f"Suggestion from {name}: {subject or '-'}",
        message=f"""
            <b>Name:</b> {name}<br>
            <b>Email:</b> {email}<br>
            <b>Contact:</b> {contact}<br>
            <b>Message:</b> {message or '-'}
        """,
        delayed=False   # ✅ force send now
    )

    return {"status": "success", "message": "Suggestion submitted successfully!"}

