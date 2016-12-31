from pyramid.view import view_config
import io
import os

THIS_DIR = os.path.dirname(__file__)


ENTRIES = {
    5: {"id": 5, "title": "Moving on and building", "creation_date": "20161229", "body": "Wrapping this, and getting ready for databases."},
    4: {"id": 4, "title": "Letting it jell.", "creation_date": "20161228", "body": "Making it solid."},
    3: {"id": 3, "title": "Getting it together.", "creation_date": "20161227", "body": "Making headway with Pyramid."},
    2: {"id": 2, "title": "Spending the time.", "creation_date": "20161226", "body": "Reading, and doing."},
    1: {"id": 1, "title": "'Drinking from a firehose'", "creation_date": "20161225", "body": "After faceplanting on servers, here's Pyramid."},
}


@view_config(route_name="homepage", renderer="templates/index.jinja2")
def homepage(request):
    """View the list page, displaying a list of journal entries."""
    return {"ENTRIES": ENTRIES}


@view_config(route_name="detail", renderer="templates/entry.jinja2")
def detail(request):
    """View an entry's page, displaying a certain entry."""
    return {"ENTRIES": ENTRIES[int(request.matchdict['id'])]}


@view_config(route_name="write", renderer="templates/write.jinja2")
def write(request):
    """View the form page, displaying a form to write new blog posts."""
    return {"ENTRIES": ENTRIES}


@view_config(route_name="edit", renderer="templates/editentry.jinja2")
def edit(request):
    """View page for editing entries, displaying a form."""
    return {"ENTRIES": ENTRIES[int(request.matchdict['id'])]}
