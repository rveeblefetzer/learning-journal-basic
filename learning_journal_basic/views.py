from pyramid.response import Response
from pyramid.view import view_config
import io
import os

THIS_DIR = os.path.dirname(__file__)


def homepage(request):
    """View for the homepage, listing journal entries."""
    page_data = open(os.path.join(THIS_DIR, 'templates/index.html')).read()
    return Response(page_data)


def detail(request):
    """View for the details page, showing a specific journal entry."""
    page_data = open(os.path.join(THIS_DIR, 'data/20161227.html')).read()
    return Response(page_data)


def write(request):
    """View for page to write a new journal entry."""
    page_data = open(os.path.join(THIS_DIR, 'templates/write.html')).read()
    return Response(page_data)


def edit(request):
    """View for page to edit an existing journal entry."""
    page_data = open(os.path.join(THIS_DIR, 'templates/editentry.html')).read()
    return Response(page_data)


def includeme(config):
    """Connect views to their routes."""
    config.add_view(homepage, route_name='homepage')
    config.add_view(detail, route_name='detail')
    config.add_view(write, route_name='write')
    config.add_view(edit, route_name='edit')
