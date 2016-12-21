# from pyramid.response import Response
from pyramid.view import view_config
import io
import os

THIS_DIR = os.path.dirname(__file__)


@view_config(route_name='home', renderer='string')
def home_page(request):
    """View for the homepage."""
#    file_path = os.path.join(THIS_DIR, 'data', 'sample.txt')
#   file_data = io.open(file_path).read()
    # return Response(file_data)
    return "this is working. i think."


@view_config(route_name='detail', renderer='string')
def detail(request):
    """View for journal entry."""
    return ""


@view_config(route_name='create', renderer='string')
def create(request):
        return ""


@view_config(route_name='edit', renderer='string')
def edit(request):
    return ""
