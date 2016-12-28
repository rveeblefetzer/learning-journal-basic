from pyramid.response import Response
from pyramid.view import view_config
import io
import os

THIS_DIR = os.path.dirname(__file__)

def homepage(request):
    """View for the homepage, listing journal entries."""
    file_path = os.path.join(THIS_DIR, 'templates/index.html')
    file_data = io.open(file_path).read()
    return Response(file_data)


def detail(request):
    """View for the details page, showing a specific journal entry."""
    file_path = os.path.join(THIS_DIR, 'data/entry.html')
    file_data = io.open(file_path).read()
    return Response(file_data)


def create(request):
    """View for page to write a new journal entry."""
    file_path = os.path.join(THIS_DIR, 'templates/write.html')
    file_data = io.open(file_path).read()
    return Response(file_data)


def edit(request):
    """View for page to edit an existing journal entry."""
    file_path = os.path.join(THIS_DIR, 'templates/editentry.html')
    file_data = io.open(file_path).read()
    return Response(file_data)


def assignment_entry(request):
    """View for page of assignment's journal entry."""
    file_path = os.path.join(THIS_DIR, 'data/entry.html')
    file_data = io.open(file_path).read()
    return Response(file_data)


def assignment_write(request):
    """View for page of assignment's new-post page."""
    file_path = os.path.join(THIS_DIR, 'templates/write.html')
    file_data = io.open(file_path).read()
    return Response(file_data)


def assignment_edit(request):
    """View for page of assignment's journal entry."""
    file_path = os.path.join(THIS_DIR, 'templates/editentry.html')
    file_data = io.open(file_path).read()
    return Response(file_data)


def includeme(config):
    """Connect views to their routes."""
    config.add_view(homepage, route_name='home')
    config.add_view(detail, route_name='detail')
    config.add_view(create, route_name='write')
    config.add_view(edit, route_name='edit')
    config.add_view(assignment_entry, route_name='assignment_entry')
    config.add_view(assignment_write, route_name='assignment_write')
    config.add_view(assignment_edit, route_name='assignment_edit')
