import frappe
from frappe import _


# ==========================================================
# GET ALL PROJECTS (USED FOR HOME / NEW / SOLD OUT PAGES)
# ==========================================================

@frappe.whitelist(allow_guest=True)
def get_projects(tag=None, status=None):
    """
    Fetch Real Estate Projects
    Optional filters:
    - tag: Featured-Properties
    - status: New / Sold Out / Upcoming / Ready to Occupy / Sale
    Sorted by order_by DESC
    """

    filters = {}

    # --------------------------------------------------
    # 🔹 STATUS FILTER
    # --------------------------------------------------
    if status:
        filters["status"] = status

    # --------------------------------------------------
    # 🔹 TAG FILTER (Frappe Tag System)
    # --------------------------------------------------
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

    # --------------------------------------------------
    # 🔹 FETCH PROJECTS (NO GALLERY FILTER HERE)
    # --------------------------------------------------
    projects = frappe.get_all(
        "Real Estate Project",
        filters=filters,
        fields=[
            "name",
            "project_name",
            "url",
            "order_by",
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
        ],
        order_by="order_by desc"
    )

    # --------------------------------------------------
    # 🔹 ATTACH CHILD TABLE DATA
    # --------------------------------------------------
    for project in projects:
        project["id"] = project["name"]

        # Carousel Images
        project["carousel_images"] = frappe.get_all(
            "Project Carousel Image",
            filters={"parent": project["name"]},
            fields=["name", "image", "idx"],
            order_by="idx asc"
        )

        # Existing Gallery Images
        project["gallery_images"] = frappe.get_all(
            "Project Gallery Image",
            filters={"parent": project["name"]},
            fields=["name", "image", "idx"],
            order_by="idx asc"
        )

    return projects


# ==========================================================
# GET PROJECTS ONLY FOR GALLERY PAGE
# (ONLY PROJECTS HAVING GALLERY CHILD RECORDS)
# ==========================================================

@frappe.whitelist(allow_guest=True)
def get_gallery_projects():
    """
    Fetch only projects that have at least one record
    in Gallery child doctype.
    Used only for Gallery Page.
    """

    # Get unique project names from Gallery child table
    gallery_projects = frappe.get_all(
        "Gallery",
        fields=["parent"],
        group_by="parent"
    )

    project_names = [g.parent for g in gallery_projects]

    if not project_names:
        return []

    # Fetch only those projects
    projects = frappe.get_all(
        "Real Estate Project",
        filters={"name": ["in", project_names]},
        fields=[
            "name",
            "project_name",
            "url",
            "thumbnail",
            "order_by"
        ],
        order_by="order_by desc"
    )

    # Attach Custom Gallery (Grouped by select_tag)
    for project in projects:

        gallery_rows = frappe.get_all(
            "Gallery",
            filters={"parent": project["name"]},
            fields=["select_tag", "image", "idx"],
            order_by="idx asc"
        )

        gallery_grouped = {}

        for row in gallery_rows:
            tag_name = row.select_tag or "Untagged"

            if tag_name not in gallery_grouped:
                gallery_grouped[tag_name] = {
                    "select_tag": tag_name,
                    "images": []
                }

            if row.image:
                gallery_grouped[tag_name]["images"].append(row.image)

        project["custom_gallery"] = list(gallery_grouped.values())

    return projects


# ==========================================================
# GET SINGLE PROJECT BY URL
# ==========================================================

@frappe.whitelist(allow_guest=True)
def get_project(url):
    """
    Fetch SINGLE Real Estate Project by URL
    """

    if not url:
        frappe.throw(_("Project URL is required"))

    project_name = frappe.db.get_value(
        "Real Estate Project",
        {"url": url},
        "name"
    )

    if not project_name:
        return None

    project = frappe.get_doc("Real Estate Project", project_name)

    data = {
        "name": project.name,
        "project_name": project.project_name,
        "url": project.url,
        "order_by": project.order_by,
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

    # Carousel Images
    data["carousel_images"] = frappe.get_all(
        "Project Carousel Image",
        filters={"parent": project.name},
        fields=["name", "image", "idx"],
        order_by="idx asc"
    )

    # Existing Gallery Images
    data["gallery_images"] = frappe.get_all(
        "Project Gallery Image",
        filters={"parent": project.name},
        fields=["name", "image", "idx"],
        order_by="idx asc"
    )

    # Custom Gallery
    gallery_rows = frappe.get_all(
        "Gallery",
        filters={"parent": project.name},
        fields=["select_tag", "image", "idx"],
        order_by="idx asc"
    )

    gallery_grouped = {}

    for row in gallery_rows:
        tag_name = row.select_tag or "Untagged"

        if tag_name not in gallery_grouped:
            gallery_grouped[tag_name] = {
                "select_tag": tag_name,
                "images": []
            }

        if row.image:
            gallery_grouped[tag_name]["images"].append(row.image)

    data["custom_gallery"] = list(gallery_grouped.values())

    return data
