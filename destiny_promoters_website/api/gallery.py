import frappe

@frappe.whitelist(allow_guest=True)
def get_gallery_images():
    try:
        gallery_images = frappe.get_all(
            "Gallery Image",
            fields=["name"]
        )

        result = []

        for gallery in gallery_images:
            doc = frappe.get_doc("Gallery Image", gallery.name)

            # Correct child table fieldname
            for item in doc.upload_gallery_image:
                if item.is_active == 1:
                    result.append({
                        "image": item.image,
                        "alt_text": item.add_alt_text
                    })

        return {
            "status": "success",
            "data": result
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Gallery API Error")
        return {
            "status": "error",
            "message": str(e)
        }
