import frappe
from frappe import _


# =========================================================
# LIST PROJECTS (Listing Page)
# =========================================================
@frappe.whitelist(allow_guest=True)
def get_projects(tag=None):
    """
    Fetch all Real Estate Projects
    Optional tag filter: 'Featured-Properties'
    """

    filters = {}

    if tag:
        tagged_projects = frappe.get_all(
            "Tag Link",
            filters={
                "document_type": "Real Estate Project",
                "tag": tag
            },
            pluck="document_name"
        )

        if not tagged_projects:
            return []

        filters["name"] = ["in", tagged_projects]

    projects = frappe.get_all(
        "Real Estate Project",
        filters=filters,
        fields=[
            "name",
            "project_name",
            "heading_project_location",
            "status",
            "project_location",
            "heading_project_area",
            "project_area",
            "builder",
            "super_built_up_area",
            "project_type",
            "floors",
            "bath",
            "bhk",
            "full_location",
            "heading_first",
            "description",
            "thumbnail"
        ]
    )

    for project in projects:
        project["id"] = project["name"]

        # 🔹 Carousel Images
        project["carousel_images"] = frappe.get_all(
            "Project Carousel Image",
            filters={"parent": project["name"]},
            fields=["name", "image", "idx"],
            order_by="idx asc"
        )

        # 🔹 Gallery Images
        project["gallery_images"] = frappe.get_all(
            "Project Gallery Image",
            filters={"parent": project["name"]},
            fields=["name", "image", "idx"],
            order_by="idx asc"
        )

    return projects


# =========================================================
# SINGLE PROJECT (Listing Details Page)
# =========================================================
@frappe.whitelist(allow_guest=True)
def get_project(id):
    """
    Fetch SINGLE Real Estate Project by DocType name
    """

    if not id:
        frappe.throw(_("Project ID is required"))

    if not frappe.db.exists("Real Estate Project", id):
        frappe.throw(_("Project not found"))

    project = frappe.get_doc("Real Estate Project", id)

    data = {
        "name": project.name,
        "project_name": project.project_name,
        "status": project.status,
        "floors": project.floors,
        "bath": project.bath,
        "bhk": project.bhk,
        "full_location": project.full_location,
        "project_area": project.project_area,
        "builder": project.builder,
        "super_built_up_area": project.super_built_up_area,
        "project_type": project.project_type,
        "heading_project_location": project.heading_project_location,
        "heading_first": project.heading_first,
        "description": project.description,
        "project_location": project.project_location,
        "thumbnail": project.thumbnail,
    }

    # 🔹 Carousel Images
    data["carousel_images"] = frappe.get_all(
        "Project Carousel Image",
        filters={"parent": project.name},
        fields=["name", "image", "idx"],
        order_by="idx asc"
    )

    # 🔹 Gallery Images
    data["gallery_images"] = frappe.get_all(
        "Project Gallery Image",
        filters={"parent": project.name},
        fields=["name", "image", "idx"],
        order_by="idx asc"
    )

    return data
