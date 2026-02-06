import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_projects(tag=None):
    """
    tag example: 'Featured-Properties'
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
            "thumbnail",
            "order_by"   # optional but good for debugging
        ],
        order_by="order_by desc"   # 🔥 THIS IS THE KEY LINE
    )

    for project in projects:
        project["id"] = project["name"]

        project["carousel_images"] = frappe.get_all(
            "Project Carousel Image",
            filters={"parent": project["name"]},
            fields=["name", "image", "idx"],
            order_by="idx asc"
        )

        project["gallery_images"] = frappe.get_all(
            "Project Gallery Image",
            filters={"parent": project["name"]},
            fields=["name", "image", "idx"],
            order_by="idx asc"
        )

    return projects
