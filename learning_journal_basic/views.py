# from pyramid.response import Response
from pyramid.view import view_config
import io
import os

THIS_DIR = os.path.dirname(__file__)

@view_config(route_name='home', renderer='string')
def home_page(request):
    """View for the homepage."""
    file_path = os.path.join(THIS_DIR, 'data', 'sample.txt')
    file_data = io.open(file_path).read()
    # return Response(file_data)
    return file_data


@view_confit(route_name='detail', 'renderer', )
def detail(request):
    return ""


@view_config(route_name='create', 'renderer', )
    def create(request):
        return ""


@view_config(route_name='edit', 'renderer')
    def edit(request)
    return ""
