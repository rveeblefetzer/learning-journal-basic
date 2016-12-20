from pyramid.response import Response
import io
import os

THIS_DIR = os.path.dirname(__file__)


def home_page(request):
    """View for the homepage."""
    file_path = os.path.join(THIS_DIR, 'data', 'sample.txt')
    file_data = io.open(file_path).read()
    return Response(file_data)


def includeme(config):
    """The configurator willl attach my views to routes."""
    config.add_view(home_page, route_name='home')
