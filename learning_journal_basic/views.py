from pyramid.response import Response
from pyramid.view import view_config
import io
import os

THIS_DIR = os.path.dirname(__file__)


ENTRIES = {
    1: {"id": 1, "title": "Today, Dec. 16, I learned.", "creation_date": "12/17/2016", "body": "Sample text"},
    2: {"id": 2, "title": "Today, Dec. 17, I learned.", "creation_date": "12/18/2016", "body": "Sample text"},
    3: {"id": 3, "title": "Today, Dec. 18, I learned.", "creation_date": "12/19/2016", "body": "Sample text"},
    4: {"id": 4, "title": "Today, Dec. 19, I learned.", "creation_date": "12/20/2016", "body": "Sample text"},
    5: {"id": 5, "title": "Today, Dec. 20, I learned.", "creation_date": "12/21/2016", "body": "Sample text"},
}


@view_config(route_name="index", renderer="templates/index.jinja2")
def register(request):
    """View the list page, displaying a list of journal entries."""
    return {"ENTRIES": ENTRIES}


@view_config(route_name="detail", renderer="templates/entry.jinja2")
def detail(request):
    """View an entry's page, displaying a certain entry."""
    return {"ENTRIES": ENTRIES[int(request.matchdict['id'])]}


@view_config(route_name="form", renderer="templates/write.jinja2")
def create(request):
    """View the form page, displaying a form to write new blog posts."""
    return {"ENTRIES": ENTRIES}


@view_config(route_name="edit_form", renderer="templates/editentry.jinja2")
def update(request):
    """View the update/edit-form page, displaying a form to update/edit blog posts."""
    return {"ENTRIES": ENTRIES[int(request.matchdict['id'])]}
