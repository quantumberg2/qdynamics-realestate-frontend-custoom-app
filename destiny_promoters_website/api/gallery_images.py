import frappe
from frappe import _


# -------------------------------------------------------------------
# 1️⃣ GET PROJECTS THAT HAVE GALLERY IMAGES
# Returns: project (id), project_name, thumbnail
# -------------------------------------------------------------------
@frappe.whitelist(allow_guest=True)
def get_gallery_projects():
    """
    Get unique projects that have gallery images
    """

    projects = frappe.db.sql("""
        SELECT DISTINCT
            p.name AS project,
            p.project_name,
            p.url,
            p.thumbnail
        FROM `tabGallery Image` gi
        INNER JOIN `tabReal Estate Project` p
            ON p.name = gi.project
        ORDER BY p.project_name ASC
    """, as_dict=True)

    return projects


# -------------------------------------------------------------------
# 2️⃣ GET TAGS FOR A SPECIFIC PROJECT
# -------------------------------------------------------------------
@frappe.whitelist(allow_guest=True)
def get_project_gallery_tags(project):
    """
    Get all unique tags for a given project
    """

    if not project:
        frappe.throw(_("Project is required"))

    tags = frappe.db.sql("""
        SELECT DISTINCT tl.tag
        FROM `tabTag Link` tl
        INNER JOIN `tabGallery Image` gi
            ON gi.name = tl.document_name
        WHERE tl.document_type = 'Gallery Image'
          AND gi.project = %s
        ORDER BY tl.tag ASC
    """, project)

    return [t[0] for t in tags]


# -------------------------------------------------------------------
# 3️⃣ GET GALLERY IMAGES BY PROJECT (+ OPTIONAL TAG)
# -------------------------------------------------------------------
@frappe.whitelist(allow_guest=True)
def get_gallery_images(project, tag=None):
    """
    Get gallery images for a project
    Optional filter by tag
    """

    if not project:
        frappe.throw(_("Project is required"))

    filters = {
        "project": project
    }

    # 🔹 Filter by system tag
    if tag:
        tagged = frappe.get_all(
            "Tag Link",
            filters={
                "document_type": "Gallery Image",
                "tag": tag
            },
            pluck="document_name"
        )

        if not tagged:
            return []

        filters["name"] = ["in", tagged]

    images = frappe.get_all(
        "Gallery Image",
        filters=filters,
        fields=[
            "name",
            "image"
        ],
        order_by="creation ASC"
    )

    return images
